import re
import unicodedata
from collections import Counter

_STEM_SPLIT = re.compile(r"[-_/]+")
_TARGET_SPLIT = re.compile(r"[\s\-_/]+")


def normalize_letters(s: str) -> str:
    return "".join(ch for ch in s if unicodedata.category(ch).startswith("L")).casefold()


def _counter_from_parts(parts: list[str]) -> Counter[str]:
    c: Counter[str] = Counter()
    for p in parts:
        if not p:
            continue
        w = normalize_letters(p)
        if w:
            c[w] += 1
    return c


def target_raw_to_counter(raw: str) -> Counter[str]:
    return _counter_from_parts([p for p in _TARGET_SPLIT.split(raw.strip()) if p])


def stem_to_counter(stem: str) -> Counter[str]:
    return _counter_from_parts([p for p in _STEM_SPLIT.split(stem) if p])


def extract_normalized_words(text: str) -> list[str]:
    out: list[str] = []
    buf: list[str] = []
    for ch in text:
        if unicodedata.category(ch).startswith("L"):
            buf.append(ch)
        else:
            if buf:
                out.append("".join(buf).casefold())
                buf = []
    if buf:
        out.append("".join(buf).casefold())
    return out


def multiset_covers(body: Counter[str], required: Counter[str]) -> bool:
    return not required or all(body.get(k, 0) >= n for k, n in required.items())
