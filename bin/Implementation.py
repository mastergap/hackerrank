from math import sqrt, ceil
import itertools
from bin.utils.Decorators import measure_decorator


# Implementation: Angry professor
def check_present_students(students, k):
    """
    :type students: list[int]
    :type k: int
    :rtype: str
    """
    present_students = sum(1 for x in students if x < 0)
    return "YES" if present_students >= k else "NO"


# Implementation: Sherlock and the beast
def find_decent_number(n):
    """
    :type n: int
    :rtype: str
    """
    digits_5 = 0
    digits_3 = 0
    if n % 3 == 0:
        digits_5 = n
    elif n % 3 == 1 and n > 9:
        digits_3 = 10
        digits_5 = int(n / 3) * 3 - 9
    elif n % 3 == 2 and n > 4:
        digits_3 = 5
        digits_5 = int(n / 3) * 3 - 3
    elif n % 5 == 0:
        digits_3 = n
    else:
        return -1

    return int(
        "".join("5" for _ in range(digits_5)) +
        "".join("3" for _ in range(digits_3))
    )


# Implementation: Utopian Tree
def grow_utopian_tree(n):
    """
    :type n: int
    :rtype: int
    """
    # height = 1
    # for i in range(n):
    #     height = height * 2 if i % 2 == 0 else height + 1

    height = 2 ** ((n + 3) // 2) - 2 + (n + 1) % 2

    return height


# Implementation: Find digits
def find_digits(n):
    """
    :type n: int
    :rtype: int
    """
    return sum(1 for d in n if int(d) != 0 and int(n) % int(d) == 0)


# Implementation: Sherlock and Squares
def find_squares(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    squares = [x ** 2 for x in range(int(sqrt(b)) + 1) if a <= x ** 2 <= b]
    return len(squares)


# Implementation: Service Lane
def max_vehicle(service_lane, i, j):
    """
    :type service_lane: list[int]
    :type i: int
    :type j: int
    :rtype: int
    """
    return min(service_lane[i:j])


# Implementation: Cut the sticks
def cut_sticks(sticks, n):
    """
    :type sticks: list[int]
    :type n: int
    :rtype: list[int]
    """
    results = []
    for _ in range(n):
        sticks = list(map(lambda x: x - min(sticks), sticks))
        sticks = [x for x in sticks if x > 0]
        results.append(len(sticks))

    return results


# Implementation: Chocolate Feast
def calculate_chocolates(n, c, m):
    """
    :type n: int
    :type c: int
    :type m: int
    :rtype: int
    """
    result = envelops = n // c

    while envelops >= m:
        trade = envelops // m
        result += trade
        envelops = envelops % m + trade

    return result


# Implementation: Chocolate Feast Alternative
def calculate_chocolates_alt(n, c, m):
    """
    :type n: int
    :type c: int
    :type m: int
    :rtype: int
    """
    result = envelops = n // c

    while envelops >= m:
        envelops += 1 - m  # Every time i give m chocolates to get a new one
        result += 1  # Add the new one chocolate

    return result


# Implementation: Caesar Cipher
def caesar(c, x):
    """
    :type c: str
    :type x: int
    :rtype: str
    """
    ic = ord(c)

    if not 97 <= ic <= 122 and not 65 <= ic <= 90:
        return c

    if 97 <= ic <= 122 and 97 <= ic + x % 26 <= 122:
        return chr(ic + x % 26)
    elif 65 <= ic <= 122 and 65 <= ic + x % 26 <= 90:
        return chr(ic + x % 26)
    else:
        return chr(ic + x % 26 - 26)


# Implementation: The Grid Search
def grid_search(g, p):
    """
    :type g: list[list[int]]
    :type p: list[list[int]]
    :rtype: bool
    """
    pattern_found = False

    for i in range(0, len(g) - len(p) + 1):
        for j in range(0, len(g[i]) - len(p[0]) + 1):
            for p_i in range(len(p)):
                row_pattern_found = False
                for p_j in range(len(p[p_i])):
                    if g[i + p_i][j + p_j] != p[p_i][p_j]:
                        break
                else:
                    row_pattern_found = True
                if not row_pattern_found:
                    break
            else:
                pattern_found = True
            if pattern_found:
                break
        if pattern_found:
            break
    return pattern_found


# Implementation: Cavity Map
def find_cavities(grid):
    """
    :type grid: list[list[str]]
    :rtype: list[list[str]]
    """
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if (
                (grid[i - 1][j] != 'X' and
                    int(grid[i][j]) > int(grid[i - 1][j])) and
                (grid[i][j + 1] != 'X' and
                    int(grid[i][j]) > int(grid[i][j + 1])) and
                (grid[i + 1][j] != 'X' and
                    int(grid[i][j]) > int(grid[i + 1][j])) and
                (grid[i][j - 1] != 'X' and
                    int(grid[i][j]) > int(grid[i][j - 1]))
            ):
                grid[i] = grid[i][:j] + "X" + grid[i][j + 1:]
                j += 1
    return grid


# Implementation: Manasa and Stones
@measure_decorator
def find_final_stones(n, a, b):
    """
    :type n: int
    :type a: int
    :type b: int
    :rtype: list[int]
    """
    final_stones = set()

    combinations = set(itertools.combinations_with_replacement("10", n))

    steps = (a, b)

    for combination in combinations:
        final_stone = 0
        for i in range(1, n):
            final_stone += steps[int(combination[i])]
        final_stones.add(final_stone)

    return sorted(list(final_stones))


@measure_decorator
def find_final_stones_most_efficient(n, a, b):
    """
    :type n: int
    :type a: int
    :type b: int
    :rtype: list[int]
    """
    s = set()
    for i in range(n):
        s.add(b * i + (n - i - 1) * a)
    return sorted(list(s))


# Implementation: Library Fine
def calculate_fine(d1, d2):
    """
    :type d1: list[int]
    :type d2: list[int]
    :rtype: int
    """
    if d1[2] > d2[2]:
        return 10000
    if d1[2] == d2[2] and d1[1] > d2[1]:
        return 500 * (d1[1] - d2[1])
    if d1[2] == d2[2] and d1[1] == d2[1] and d1[0] > d2[0]:
        return 15 * (d1[0] - d2[0])
    return 0


# Implementation: ACM ICPC Team
def known_topics_number(person1, person2):
    """
    :type person1: str
    :type person2: str
    :rtype: int
    """
    return sum(1 if x[0] == '1' or x[1] == '1' else 0 for x in zip(person1, person2))


def max_known_topics_teams(persons):
    """
    :type persons: list[str]
    :rtype: (int, int)
    """
    max_known_topics = 0
    max_known_topics_teams_count = 0

    for i, person1 in enumerate(persons):
        for person2 in persons[i + 1:]:
            temp = known_topics_number(person1, person2)
            if temp > max_known_topics:
                max_known_topics_teams_count = 1
                max_known_topics = temp
            elif temp == max_known_topics:
                max_known_topics_teams_count += 1

    return max_known_topics, max_known_topics_teams_count


# Implementation: Extra long factorials
def factorial(n):
    """
    :type n: int
    :rtype: int
    """
    f = n
    for i in range(n - 1, 0, -1):
        f = f * i
    return f


# Implementation: Taum and B'day
def calculate_min_gifts_cost(b_count, w_count, b_cost, w_cost, conversion_cost):
    """
    :type b_count: int
    :type w_count: int
    :type b_cost: int
    :type w_cost: int
    :type conversion_cost: int
    :rtype: int
    """
    real_b_cost = b_cost if b_cost <= conversion_cost + w_cost else conversion_cost + w_cost
    real_w_cost = w_cost if w_cost <= conversion_cost + b_cost else conversion_cost + b_cost

    return (real_b_cost * b_count) + (real_w_cost * w_count)


# Omplementation: The time in words
def time_to_words(h, m):
    """
    :type h: int
    :type m: int
    :rtype: str
    """
    hours = {
        0: "o' clock",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve"
    }

    minutes = {
        0: "o' clock",
        1: "one minute",
        2: "two minutes",
        3: "three minutes",
        4: "four minutes",
        5: "five minutes",
        6: "six minutes",
        7: "seven minutes",
        8: "eight minutes",
        9: "nine minutes",
        10: "ten minutes",
        11: "eleven minutes",
        12: "twelve minutes",
        13: "thirteen minutes",
        14: "fourteen minutes",
        15: "quarter",
        16: "sixteen minutes",
        17: "seventeen minutes",
        18: "eighteen minutes",
        19: "nineteen minutes",
        20: "twenty minutes",
        21: "twenty one minutes",
        22: "twenty two minutes",
        23: "twenty three minutes",
        24: "twenty four minutes",
        25: "twenty five minutes",
        26: "twenty six minutes",
        27: "twenty seven minutes",
        28: "twenty eight minutes",
        29: "twenty nine minutes",
        30: "half",
        45: "quarter"
    }

    if m == 0:
        return hours[h] + " " + minutes[m]
    if m == 45:
        return minutes[m] + " to " + hours[(h + 1) % 12]
    elif 0 < m <= 30:
        return minutes[m] + " past " + hours[h]
    else:
        return minutes[60 - m] + " to " + hours[(h + 1) % 12]


# Implementation: Modified Kaprekar Numbers
def find_kaprecar_numbers(p, q):
    """
    :type p: int
    :type q: int
    :rtype: list[int]
    """
    kaprecar_numbers = list()
    for i in range(p, q + 1):
        square = str(i ** 2)
        l_piece = square[:len(square) // 2] if len(square) > 1 else "0"
        r_piece = square[len(l_piece):] if len(square) > 1 else square
        if int(l_piece) + int(r_piece) == i:
            kaprecar_numbers.append(i)
    return kaprecar_numbers


# Implementation: Encryption
def encrypt(text):
    """
    :type text: str
    :rtype: str
    """
    text = text.replace(" ", "")
    # num_rows = floor(sqrt(len(text)))
    num_columns = ceil(sqrt(len(text)))
    grid = list()
    for i in range(0, len(text), num_columns):
        grid.append(list(text[i:i + num_columns].ljust(num_columns)))

    result = list(map(" ".join, list(map(list, list(zip(*grid))))))
    result = [s.replace(" ", "") for s in result]

    return result


# Implementation: Matrix Rotation
def rotate_matrix(m, n):
    """
    :type m: list[list[int]]
    :type n: int
    :rtype:  list[list[int]]
    """
    max_c = min(len(m), len(m[0])) // 2 if min(len(m), len(m[0])) % 2 == 0 else min(len(m), len(m[0])) // 2 + 1

    for c in range(max_c):
        for _ in range(n % ((len(m) - 2 * c) * 2 + (((len(m[0]) - 2 * c) * 2) - 4))):
            temp = m[c][c]

            # rotate upper row
            for j in range(c + 1, len(m[0]) - c):
                m[c][j - 1] = m[c][j]

            # rotate right column
            for i in range(c + 1, len(m) - c):
                m[i - 1][len(m[0]) - c - 1] = m[i][len(m[0]) - c - 1]

            # rotate unless we are in the middle row of a matrix with odd rows
            if len(m) - c * 2 != 1:

                # rotate bottom row
                for j in range(len(m[0]) - c - 1, c, -1):
                    m[len(m) - c - 1][j] = m[len(m) - c - 1][j - 1]

                if len(m[0]) - c - 1 != c:

                    # rotate left column
                    for i in range(len(m) - c - 1, c + 1, -1):
                        m[i][c] = m[i - 1][c]

                if len(m[0]) - c * 2 != 1:
                    m[c + 1][c] = temp
                # if we are in the middle column of a matrix with odd colums do vertical rotation
                else:
                    m[len(m) - c - 1][c] = temp
            else:
                m[c][len(m[0]) - c - 1] = temp
    return m
