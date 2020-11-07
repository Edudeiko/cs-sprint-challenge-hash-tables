#  Hint:  You may not need all of these.  Remove the unused functions.
# from hashtable import HashTable


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # cache = HashTable(length)
    # route = [None] * length

    # for ii in tickets:
    #     cache.put(ii.source, ii.destination)

    # find = cache.get("NONE")
    # idx = 0
    # curr = find
    # route[idx] = curr
    # while curr != "NONE":
    #     idx += 1
    #     get = cache.get(curr)
    #     route[idx] = get
    #     curr = get
    # route[idx] = "NONE"

    # return route

    cache = dict()

    for ii in tickets:
        cache[ii.source] = ii.destination

    route = [cache["NONE"]]

    for idx in range(len(tickets)-2):
        loop = cache[route[idx]]
        route.append(loop)

        if idx == len(tickets)-3:
            route.append("NONE")

    return route
