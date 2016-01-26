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
def calculate_chocolates(n, c, m):
    result = envelops = n // c

    while envelops >= m:
        envelops += 1 - m #Every time i give m chocolates to get a new one
        result += 1 #Add the new one chocolate

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


