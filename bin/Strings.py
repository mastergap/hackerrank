from string import ascii_lowercase


# Strings: Pangrams
def is_pangram(s):
    char_count = {c: 0 for c in ascii_lowercase}
    s = s.lower()
    for c in s:
        char_count[c] = 1

    return sum(char_count.values()) == len(char_count)


def is_funny(s):
    r = s[::-1]
    for i in range(1, len(s) - 1):
        if (abs(ord(s[i]) - ord(s[i -1])) != abs(ord(r[i]) - ord(r[i -1]))):
            return False
    return True
