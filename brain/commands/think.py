import click

from brain import logic
from brain.links.graph import build_graph
from brain.settings import settings


def _format_report(edges, unresolved, all_stems) -> str:
    lines: list[str] = []
    by_source: dict[str, dict[str, list[str]]] = {
        s: {"wiki": [], "auto": []} for s in all_stems
    }

    for e in edges:
        by_source[e.source][e.kind].append(e.target)

    for src in sorted(by_source.keys()):
        lines.append(f"## {src}")
        wiki = sorted(set(by_source[src]["wiki"]))
        auto = sorted(set(by_source[src]["auto"]))
        if wiki:
            lines.append("  wiki -> " + ", ".join(wiki))
        if auto:
            lines.append("  auto -> " + ", ".join(auto))
        if not wiki and not auto:
            lines.append("  (no outgoing links)")
        lines.append("")

    lines.append("## Unresolved wikilinks")
    if not unresolved:
        lines.append("  (none)")
    else:
        for b in sorted(unresolved, key=lambda x: (x.source, x.target_raw, x.reason)):
            lines.append(f"  {b.source}: [[{b.target_raw}]] ({b.reason})")

    return "\n".join(lines).rstrip() + "\n"


@click.command(name="think")
def think():
    """List links between notes (wikilinks + word multiset)."""
    ext = settings["NOTE_EXTENSION"]
    edges, unresolved, stems = build_graph(logic.notes_dir(), ext)
    click.echo(_format_report(edges, unresolved, stems), nl=False)
