import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from brain.links.graph import build_graph
from brain.links.normalize import (
    multiset_covers,
    stem_to_counter,
    target_raw_to_counter,
)
from brain.links.parse import parse_wikilinks, strip_for_prose_scan


class TestNormalize(unittest.TestCase):
    def test_stem_to_counter_dup(self) -> None:
        self.assertEqual(dict(stem_to_counter("foo-foo")), {"foo": 2})

    def test_multiset_covers(self) -> None:
        from collections import Counter

        body = Counter({"a": 2, "b": 1})
        self.assertTrue(multiset_covers(body, Counter({"a": 1})))
        self.assertTrue(multiset_covers(body, Counter({"a": 2})))
        self.assertFalse(multiset_covers(body, Counter({"a": 3})))

    def test_target_raw_matches_stem(self) -> None:
        self.assertEqual(stem_to_counter("Contract-Amazon"), target_raw_to_counter("Contract Amazon"))


class TestParse(unittest.TestCase):
    def test_strip_code(self) -> None:
        text = "Hello `skip` world.\n```py\n[[fake]]\n```\nMore."
        s = strip_for_prose_scan(text)
        self.assertNotIn("fake", s)
        self.assertNotIn("skip", s)
        self.assertIn("Hello", s)
        self.assertIn("More", s)

    def test_wikilinks(self) -> None:
        self.assertEqual(parse_wikilinks("See [[A]] and [[B|bee]]."), ["A", "B"])


class TestGraph(unittest.TestCase):
    def test_auto_and_wiki(self) -> None:
        with TemporaryDirectory() as tmp:
            d = Path(tmp)
            (d / "Contract-Amazon.md").write_text("body", encoding="utf-8")
            (d / "Meeting.md").write_text(
                "We discussed contract amazon today.\n[[Contract-Amazon]]\n",
                encoding="utf-8",
            )
            edges, unresolved, stems = build_graph(d, "md")
            self.assertEqual(stems, ["Contract-Amazon", "Meeting"])
            self.assertEqual(unresolved, [])
            kinds = {(e.source, e.target): e.kind for e in edges}
            self.assertEqual(kinds.get(("Meeting", "Contract-Amazon")), "wiki")

    def test_many_notes_link_same_target_word(self) -> None:
        with TemporaryDirectory() as tmp:
            d = Path(tmp)
            (d / "Amazon.md").write_text("stub", encoding="utf-8")
            for i in range(3):
                (d / f"Note{i}.md").write_text("We bought from amazon.", encoding="utf-8")
            edges, unresolved, _ = build_graph(d, "md")
            self.assertEqual(unresolved, [])
            to_amazon = [e for e in edges if e.target == "Amazon" and e.kind == "auto"]
            self.assertEqual(len(to_amazon), 3)
            self.assertEqual({e.source for e in to_amazon}, {"Note0", "Note1", "Note2"})


if __name__ == "__main__":
    unittest.main()
