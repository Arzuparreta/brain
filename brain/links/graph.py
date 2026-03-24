from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from brain.links.normalize import (
    extract_normalized_words,
    multiset_covers,
    stem_to_counter,
    target_raw_to_counter,
)
from brain.links.parse import parse_wikilinks, strip_for_prose_scan


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    kind: str  # "wiki" | "auto"


@dataclass(frozen=True)
class UnresolvedWiki:
    source: str
    target_raw: str
    reason: str  # "missing" | "ambiguous"


def _resolve_wikilink(
    target_raw: str,
    stems: set[str],
    stem_counters: dict[str, Counter[str]],
) -> tuple[str | None, str | None]:
    t = target_raw.strip()
    if not t:
        return None, "missing"

    if t in stems:
        return t, None

    casefold_matches = [s for s in stems if s.casefold() == t.casefold()]
    if len(casefold_matches) == 1:
        return casefold_matches[0], None
    if len(casefold_matches) > 1:
        return None, "ambiguous"

    tc = target_raw_to_counter(t)
    if not tc:
        return None, "missing"

    matches = [s for s in stems if stem_counters[s] == tc]
    if len(matches) == 1:
        return matches[0], None
    if len(matches) == 0:
        return None, "missing"
    return None, "ambiguous"


def build_graph(
    notes_dir: Path,
    ext: str,
) -> tuple[list[Edge], list[UnresolvedWiki], list[str]]:
    pattern = f"*.{ext}"
    stems_list = sorted(f.stem for f in notes_dir.glob(pattern) if f.is_file())
    stems_set = set(stems_list)
    stem_counters = {s: stem_to_counter(s) for s in stems_list}

    contents: dict[str, str] = {}
    for s in stems_list:
        contents[s] = (notes_dir / f"{s}.{ext}").read_text(encoding="utf-8", errors="replace")

    pair_best: dict[tuple[str, str], str] = {}

    def add_edge(src: str, tgt: str, kind: str) -> None:
        if src == tgt:
            return
        key = (src, tgt)
        if key not in pair_best:
            pair_best[key] = kind
        elif pair_best[key] == "auto" and kind == "wiki":
            pair_best[key] = "wiki"

    unresolved: list[UnresolvedWiki] = []

    for source, text in contents.items():
        prose = strip_for_prose_scan(text)
        body = Counter(extract_normalized_words(prose))

        for target_raw in parse_wikilinks(prose):
            resolved, err = _resolve_wikilink(target_raw, stems_set, stem_counters)
            if resolved is not None:
                add_edge(source, resolved, "wiki")
            else:
                reason = err or "missing"
                unresolved.append(
                    UnresolvedWiki(source=source, target_raw=target_raw, reason=reason)
                )

        for target in stems_list:
            if source == target:
                continue
            req = stem_counters[target]
            if not req:
                continue
            if not multiset_covers(body, req):
                continue
            add_edge(source, target, "auto")

    edges: list[Edge] = [
        Edge(source=s, target=t, kind=pair_best[(s, t)]) for (s, t) in sorted(pair_best.keys())
    ]
    return edges, unresolved, stems_list
