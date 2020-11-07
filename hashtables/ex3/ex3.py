import time

start = time.time()


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = dict()

    for ii in arrays:
        for jj in ii:
            if jj not in cache:
                cache[jj] = 1

            else:
                cache[jj] += 1

    result = []

    for ii in list(cache.items()):
        if ii[1] == len(arrays):
            result.append(ii[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

end = time.time()

print(f'{end-start}')
