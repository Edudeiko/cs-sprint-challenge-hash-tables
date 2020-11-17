# from hashtable import HashTable, HashTableEntry


def get_indices_of_item_weights(weights, length, limit):
    """
    get indices of an item weight
    """
    # cache = dict()
    # for idx in range(len(weights)):
    #     if weights[idx] in cache and weights[idx] == cache[weights[idx]][1]:
    #         return idx, cache[weights[idx]][0]

    #     else:
    #         cache[weights[idx]] = (idx, limit - weights[idx])

    # d = list(cache.items())
    # d.sort(reverse=True, key=lambda pair: pair[1][0])

    # for ii in d:
    #     if ii[1][1] in cache:
    #         result = ii[1][0], cache[ii[1][1]][0]
    #         return result

    # return None

    weight_ind = {w: ii for ii, w in enumerate(weights)}
    for ii, w in enumerate(weights):
        if limit - w in weight_ind:
            return [weight_ind[limit - w], ii]
    return None
