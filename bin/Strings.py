from string import ascii_lowercase
from collections import Counter


# Strings: Pangrams
def is_pangram(s):
    """
    :type s: str
    :rtype: bool
    """
    char_count = {c: 0 for c in ascii_lowercase}
    s = s.lower()
    for c in s:
        char_count[c] = 1

    return sum(char_count.values()) == len(char_count)


# Strings: Funny String
def is_funny(s):
    """
    :type s: str
    :rtype: bool
    """
    r = s[::-1]
    for i in range(1, len(s) - 1):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            return False
    return True


# Strings: Alternating characters
def deletions_number(s):
    """
    :type s: str
    :rtype: int
    """
    char_list = list(s)
    c, del_count = char_list[0], 0
    for next_c in char_list[1:]:
        if next_c == c:
            del_count += 1
        else:
            c = next_c
    return del_count


# Strings: Two Strings
def common_substring(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: str
    """
    s1 = set(s1)
    s2 = set(s2)
    for c in s1:
        if c in s2:
            return True
    return False


# Strings: Game of Thrones: I
def can_have_palindrome_anagram(s):
    """
    :type s: str
    :rtype: bool
    """
    characters_occurrences_count = Counter(s)
    odd_occurrences_count = sum(1 for x in characters_occurrences_count.values() if x % 2 == 0)
    if len(s) % 2 == 0:
        if odd_occurrences_count == len(characters_occurrences_count):
            return True
    else:
        if odd_occurrences_count == len(characters_occurrences_count) - 1:
            return True
    return False


# Strings: Gemstones
def count_common_letters(strings):
    """
    :type strings: list[str]
    :rtype: int
    """
    if len(strings) < 2:
        return 0
    common_elements = set(strings[0])
    for s in strings[1:]:
        common_elements = common_elements.intersection(set(s))
    return len(common_elements)


# Strings: Make it Anagram
def min_deletions_to_make_anagram(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: int
    """
    freq_difference = Counter(s1)
    freq_difference.subtract(s2)
    return sum(abs(x) for x in freq_difference.values())


# Strings: Anagram
def min_changes_to_make_anagram(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) % 2 != 0:
        return -1
    else:
        s1 = Counter(s[:len(s) // 2])
        s2 = Counter(s[len(s) // 2:])
        s1.subtract(s2)
        return sum([abs(x) for x in s1.values()]) // 2


# Strings: Sherlock and Anagrams
def is_anagram(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    return Counter(s1) == Counter(s2)


def factorial(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 1:
        return 1
    return n * factorial(n - 1)


# Slowest - doesn't pass the test due to timeout
def find_anagram_pairs(s):
    """
    :type s: str
    :rtype: int
    """
    counter = sum(factorial(x) // (2 * factorial(x - 2)) for x in Counter(s).values() if x > 1)
    for i in range(2, len(s)):
        for j in range(0, len(s)):
            for k in range(j + 1, len(s) - i + 1):
                s1 = s[j:j+i]
                s2 = s[k:k+i]
                if is_anagram(s1, s2):
                    counter += 1
    return counter


# Fastest - passes the test
def find_anagram_pairs_dictionary(s):
    """
    :type s: str
    :rtype: int
    """
    counter = sum(factorial(x) // (2 * factorial(x - 2)) for x in Counter(s).values() if x > 1)
    for i in range(2, len(s)):
        substrings = Counter()
        for j in range(0, len(s) - i + 1):
            substrings[str(sorted(s[j:j+i]))] += 1
        counter += sum(factorial(x) // (2 * factorial(x - 2)) for x in substrings.values() if x > 1)
    return counter


# Strings: Palindrome Index
def is_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


def find_character_index_to_remove_to_make_palindrome(s):
    """
    :type s: str
    :rtype: int
    """
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            if is_palindrome(s[:i] + s[i + 1:]):
                return i
            else:
                return len(s) - i - 1
        # For a nonsense reason if we can remove a character we have to remove it (palindrome with even chars)
        elif len(s) % 2 == 0 and i == len(s) // 2 - 1:
            return i + 1
    return -1


# Strings: Reverse Shuffle Merge
def lex_smallest_string(s):
    """
    :type s: str
    :rtype: str
    """
    char_counter = Counter(s)
    # "".join(item[0] for item in Counter.items() for x in range(item[1])])
    smallest_s = ""
    for item in char_counter.items():
        for _ in range(item[1] // 2):
            smallest_s += item[0]

    smallest_s = "".join(sorted(list(smallest_s)))

    return smallest_s
