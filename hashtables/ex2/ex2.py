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

    '''
    1st solution
    '''

    # cache = dict()

    # for ii in tickets:
    #     cache[ii.source] = ii.destination

    # route = [cache["NONE"]]

    # for idx in range(len(tickets)-2):
    #     loop = cache[route[idx]]
    #     route.append(loop)

    #     if idx == len(tickets)-3:
    #         route.append("NONE")

    # return route

    '''
    2nd solution
    '''

    ticket_source = {t.source: t for t in tickets}
    ticket_destination = {t.destination: t for t in tickets}

    first = ticket_source['NONE']
    last = ticket_destination['NONE']

    result = []
    current = first

    while current is not last:
        result.append(current.destination)
        current = ticket_source[current.destination]

    result.append('NONE')

    return result
