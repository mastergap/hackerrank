from unittest import TestCase
from nose.tools import assert_equal, assert_list_equal
from bin.Strings import *


class TestStrings(TestCase):

    def test_min_deletions_to_make_anagram(self):
        result = min_deletions_to_make_anagram("abc", "cde")
        assert_equal(4, result)

    def test_min_changes_to_make_anagram(self):
        result = min_changes_to_make_anagram("aaabbb")
        assert_equal(3, result)
        result = min_changes_to_make_anagram("ab")
        assert_equal(1, result)
        result = min_changes_to_make_anagram("abc")
        assert_equal(-1, result)
        result = min_changes_to_make_anagram("mnop")
        assert_equal(2, result)
        result = min_changes_to_make_anagram("xyyx")
        assert_equal(0, result)
        result = min_changes_to_make_anagram("xaxbbbxx")
        assert_equal(1, result)

    def test_find_anagram_pairs(self):
        inputs = [
            "abba",
            "abcd",
            "ifailuhkqq",
            "hucpoltgty",
            "ovarjsnrbf",
            "pvmupwjjjf",
            "iwwhrlkpek"
        ]
        outputs = [
            4,
            0,
            3,
            2,
            2,
            6,
            3
        ]
        results = [find_anagram_pairs(s) for s in inputs]
        assert_list_equal(outputs, results)


    def test_find_anagram_pairs_dictionary(self):
        inputs = [
            "abba",
            "abcd",
            "ifailuhkqq",
            "hucpoltgty",
            "ovarjsnrbf",
            "pvmupwjjjf",
            "iwwhrlkpek"
        ]
        outputs = [
            4,
            0,
            3,
            2,
            2,
            6,
            3
        ]
        results = [find_anagram_pairs_dictionary(s) for s in inputs]
        assert_list_equal(outputs, results)
