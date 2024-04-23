import heapq


class ip_address:

    def __init__(self):
        # this dictionary  maps the address to its count
        # ex: { '10.0.0.0' : 1, '10.0.0.1' : 1, '10.0.0.2': 2 }
        self.address_to_count = {}
        # maps the count to the addresses associated with that count using a nested dictionary
        # ex: {1: '{10.0.0.0': 0, '10.0.0.1: 0},  2: {'10.0.0.2': 0}}
        self.count_to_address = {}
        # min heap to keep track of the top 100
        self.heap = []

    """
    This function takes in the ipAddress, increments its count and then calls helper functions to ensure
    it is properly mapped between address_to_count and count_too_address and adds the count to a heap
    """

    def requestHandled(self, ipAddress: str):
        if ipAddress in self.address_to_count:
            self.address_to_count[ipAddress] += 1
        else:
            self.address_to_count[ipAddress] = 1
        self.add_count(ipAddress)
        self.add_to_heap(ipAddress)

    """
    this is a helper function to ensure that the count is mapped to the proper address in the
    count_to_address dictionary.

    if there is a new count we place that count in the dictionary and I map it to its address.
    Since there can be multiple counts tied to several ip addresses I use a dictionary to represent all the
    addresses tied to a count. I used a dictionary instead of a list because it is faster to delete a key from a 
    dictionary than it would be  to remove an element from list (O(1) vs O(n))

    if the count is not in the dictionary I add it to the dictionary.

    After that I need to deal with the previous key that the ip_address was tied to. I delete the ip address from
    the dictionary tied to the previous count.
    I then check to see if the dictionary tied to the previous count has any other keys remaining. if it does not I delete that key from
    the count_to_addr key.
    I then remove that count from the heap since there are no addresses with that count.
    """

    def add_count(self, ip_address: str):
        count = self.address_to_count[ip_address]

        if count not in self.count_to_address:
            self.count_to_address[count] = {ip_address: 0}
        else:
            self.count_to_address[count][ip_address] = 0
        if count - 1 in self.count_to_address:
            del self.count_to_address[count - 1][ip_address]
            if len(self.count_to_address[count - 1]) == 0:
                del self.count_to_address[count - 1]
                if count - 1 in self.heap:
                    self.heap.remove(count - 1)

    """ 
    Add to heap is a little more simple. My heap will only have 100 entries at once. Each entry in the heap is a count. Each count is 
    unique.

    if the size is less than 100 and the count is not in the heap I will simply push it to the heap.

    In the case where the heap is greater than the size of 100 I will cheeck to see if the smallest count in the heap is 
    less than the current count I have. If it is and that count isn't already in the heap I can replace that count with my new count.
    This lets me use a min heap while ensuring that I only have the 100 largest counts in the heap at once

    """

    def add_to_heap(self, ip_address: str):
        count = self.address_to_count[ip_address]
        if len(self.heap) < 100 and count not in self.heap:
            heapq.heappush(self.heap, count)
        elif self.heap[0] < count and count not in self.heap:
            heapq.heappushpop(self.heap, count)

    """ 
    For the top100 I know that each entry in my heap are the top 100 counts, however, it is possible that a count will have more than
    one IP address tied to it. 

    I start off by geting the n largest elements in the heap in this case 100 which is also the amount of counts in the heap. 
    With each count I get all of the IP addresses tied to that specific count in the count_to_address dictionary. I use the variable
    size to make sure that I don't grab more than 100 ip addresses. This is useful in the case where there is more than 1 address tied
    to a specific count. 
    """

    def top100(self) -> list[int]:
        if len(self.heap) == 0:
            return []
        response = []
        iter = heapq.nlargest(100, self.heap)
        size = 100
        i = 0
        while size > 0 and i < len(iter):
            for ip_address in self.count_to_address[iter[i]]:
                response.append(ip_address)
                size -= 1
                if size == 0 or i >= len(iter):
                    break
            i += 1
        return response

    """ 
    clear just deletes everything out of the heap  and the two dictionaries.
    """

    def clear(self):
        del self.heap[:]
        self.count_to_address.clear()
        self.address_to_count.clear()

    # just a function to print our the top 100 for testing
    def print_top_100(self):
        top_100 = self.top100()
        response = "Top 100:\n"
        for ip in top_100:
            response += f"\naddress: {ip} request count: {self.address_to_count[ip]}"
        print(response)

    def __str__(self) -> str:
        return f"{self.address_to_count=}\n{self.count_to_address=}\n{self.heap=}"
