from string import ascii_lowercase
from collections import Counter


# Strings: Pangrams
def is_pangram(s):
    char_count = {c: 0 for c in ascii_lowercase}
    s = s.lower()
    for c in s:
        char_count[c] = 1

    return sum(char_count.values()) == len(char_count)


# Strings: Funny String
def is_funny(s):
    r = s[::-1]
    for i in range(1, len(s) - 1):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            return False
    return True


# Strings: Alternating characters
def deletions_number(s):
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
    s1 = set(s1)
    s2 = set(s2)
    for c in s1:
        if c in s2:
            return True
    return False


# Strings: Game of Thrones: I
def can_have_palindrome_anagram(s):
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
    if len(strings) < 2:
        return 0
    common_elements = set(strings[0])
    for s in strings[1:]:
        common_elements = common_elements.intersection(set(s))
    return len(common_elements)


# Strings: Make it Anagram
def min_deletions_to_make_anagram(s1, s2):
    freq_difference = Counter(s1)
    freq_difference.subtract(s2)
    return sum(abs(x) for x in freq_difference.values())


# Strings: Anagram
def min_changes_to_make_anagram(s):
    if len(s) % 2 != 0:
        return -1
    else:
        s1 = Counter(s[:len(s) // 2])
        s2 = Counter(s[len(s) // 2:])
        s1.subtract(s2)
        return sum([abs(x) for x in s1.values()]) // 2


# Strings: Sherlock and Anagrams
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)


def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n - 1)


def find_anagram_pairs(s):
    counter = sum(factorial(x) / (2 * factorial(x - 2)) for x in Counter(s).values() if x > 1)
    for i in range(2, len(s)):
        for j in range(0, len(s)):
            for k in range(j + 1, len(s) - i + 1):
                s1 = s[j:j+i]
                s2 = s[k:k+i]
                if is_anagram(s1, s2):
                    counter += 1
    return counter