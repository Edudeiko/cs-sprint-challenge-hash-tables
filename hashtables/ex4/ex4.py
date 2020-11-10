def has_negatives(a):
    """
    get positive numbers that have corresponding negative numbers in the list
    """
    positive = []
    for ii in a:
        result = abs(ii)
        positive.append(result)

    cache = dict()
    for ii in positive:
        if ii not in cache:
            cache[ii] = 1
        else:
            cache[ii] += 1

    cached = list(cache.items())

    result = []
    for k, v in cached:
        if v > 1:
            result.append(k)
        else:
            pass

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
