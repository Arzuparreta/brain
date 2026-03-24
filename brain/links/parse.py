import re

_FENCED = re.compile(r"```[\s\S]*?```")
_INLINE_CODE = re.compile(r"`([^`\n]+)`")
_WIKI = re.compile(r"\[\[([^\]]+)\]\]")


def strip_for_prose_scan(text: str) -> str:
    t = _FENCED.sub(" ", text)
    return _INLINE_CODE.sub(" ", t)


def parse_wikilinks(text: str) -> list[str]:
    targets: list[str] = []
    for m in _WIKI.finditer(text):
        inner = m.group(1).strip()
        if "|" in inner:
            targets.append(inner.split("|", 1)[0].strip())
        else:
            targets.append(inner)
    return targets
