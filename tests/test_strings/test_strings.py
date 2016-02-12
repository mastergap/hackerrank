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


    def test_find_character_index_to_remove_to_make_palindrome(self):
        with open("../assets/text/sherlock_and_anagrams_input.txt", "r",) as input_file, \
                open("../assets/text/sherlock_and_anagrams_output.txt", "r") as output_file:
            t = int(input_file.readline().strip())
            for _ in range(t):
                result = find_character_index_to_remove_to_make_palindrome(input_file.readline().strip())
                assert_equal(int(output_file.readline()), result)


    def test_lex_smallest_string(self):
        with open("../assets/text/shuffle_merge_input.txt", "r",) as input_file, \
            open("../assets/text/shuffle_merge_output.txt", "r") as output_file:
            input = input_file.readline().strip()
            output = output_file.readline().strip()
            result = lex_smallest_string(input)
            assert_equal(output, result)
