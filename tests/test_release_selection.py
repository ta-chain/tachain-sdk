"""Selection rules for the manually dispatched SDK release."""

import unittest

from scripts.release_selection import select_languages


LANGUAGES = (
    "typescript", "python", "java", "csharp", "go", "php", "ruby", "swift"
)


def selection(**enabled):
    return {key: enabled.get(key, False) for key in ("all", *LANGUAGES)}


class ReleaseSelection(unittest.TestCase):
    def test_all_selects_every_language_once(self):
        self.assertEqual(select_languages(selection(all=True)), list(LANGUAGES))

    def test_multiple_languages_keep_canonical_order(self):
        self.assertEqual(
            select_languages(selection(swift=True, python=True, go=True)),
            ["python", "go", "swift"],
        )

    def test_single_language(self):
        self.assertEqual(select_languages(selection(php=True)), ["php"])

    def test_empty_selection_is_rejected(self):
        with self.assertRaises(ValueError):
            select_languages(selection())

    def test_all_cannot_be_combined_with_individual_languages(self):
        with self.assertRaises(ValueError):
            select_languages(selection(all=True, ruby=True))

    def test_non_boolean_values_are_rejected(self):
        for key, value in (("all", "true"), ("python", "false"), ("go", 1), ("swift", None)):
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                select_languages(selection(**{key: value}))


if __name__ == "__main__":
    unittest.main()
