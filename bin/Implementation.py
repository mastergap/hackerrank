from math import sqrt
import itertools
from Decorators import measure_decorator


# Implementation: Angry professor
def check_present_students(students, k):
    present_students = sum(1 for x in students if x < 0)
    return "YES" if present_students >= k else "NO"


# Implementation: Sherlock and the beast
def find_decent_number(n):
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

        return int("".join("5" for _ in range(digits_5)) + "".join("3" for _ in range(digits_3)))


# Implementation: Utopian Tree
def grow_utopian_tree(n):
    # height = 1
    # for i in range(n):
    #     height = height * 2 if i % 2 == 0 else height + 1

    height = 2 ** ((n + 3) // 2) - 2 + (n + 1) % 2

    return height


# Implementation: Find digits
def find_digits(n):
    return sum(1 for d in n if int(d) != 0 and int(n) % int(d) == 0)


# Implementation: Sherlock and Squares
def find_squares(a, b):
    squares = [x ** 2 for x in range(int(sqrt(b)) + 1) if a <= x ** 2 <= b]
    return len(squares)


# Implementation: Service Lane
def max_vehicle(service_lane, i, j):
    return min(service_lane[i:j])


# Implementation: Cut the sticks
def cut_sticks(sticks, n):
    results = []
    for _ in range(n):
        sticks = list(map(lambda x: x - min(sticks), sticks))
        sticks = [x for x in sticks if x > 0]
        results.append(len(sticks))

    return results


# Implementation: Chocolate Feast
def calculate_chocolates(n, c, m):
    result = envelops = n // c

    while envelops >= m:
        trade = envelops // m
        result += trade
        envelops = envelops % m + trade

    return result


# Implementation: Chocolate Feast Alternative
def calculate_chocolates_alt(n, c, m):
    result = envelops = n // c

    while envelops >= m:
        envelops += 1 - m  # Every time i give m chocolates to get a new one
        result += 1  # Add the new one chocolate

    return result


# Implementation: Caesar Cipher
def caesar(c, x):
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
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if (
                    (grid[i - 1][j] != 'X' and int(grid[i][j]) > int(grid[i - 1][j])) and
                    (grid[i][j + 1] != 'X' and int(grid[i][j]) > int(grid[i][j + 1])) and
                    (grid[i + 1][j] != 'X' and int(grid[i][j]) > int(grid[i + 1][j])) and
                    (grid[i][j - 1] != 'X' and int(grid[i][j]) > int(grid[i][j - 1]))
            ):
                grid[i] = grid[i][:j] + "X" + grid[i][j + 1:]
                j += 1
    return grid


# Implementation: Manasa and Stones
@measure_decorator
def find_final_stones(n, a, b):
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
    s = set()
    for i in range(n):
        s.add(b * i + (n - i - 1) * a)
    return sorted(list(s))


# Implementation: Library Fine
def calculate_fine(d1, d2):
    if d1[2] > d2[2]:
        return 10000
    if d1[2] == d2[2] and d1[1] > d2[1]:
        return 500 * (d1[1] - d2[1])
    if d1[2] == d2[2] and d1[1] == d2[1] and d1[0] > d2[0]:
        return 15 * (d1[0] - d2[0])
    return 0


