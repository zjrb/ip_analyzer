* How does your code work?

For this problem I decided to use a min heap, and two dictionaries called address_to_count and count_to_addresss. The purpose of these dictionaries is to keep track of which address is tied to which count and vice versa. I use a min heap to keep track of the top 100 counts. The min-heap is helpful because it allows me to quickly get the smallest count in the top 100 and remove it and add a new count if an IP addresses ends up with a count large enough to land itself in the top 100. 

Each time requestHandled() is called it makes sure that the count is updated and the address is tied to the right count and then looks to see if the count for this ip address would need to be in the top 100 or not. Since the top 100 is a min heap of the top 100 it is easy to check the smallest element as it is stored at index 0 of the heap. The heap s is unique so there will never be the same count in there multiple times. This makes it much easier to insert and delete from the heap and to eventually sort the heap when it is time to get the top 100 ip addresses. Since there can be multiple ip addresses with the same count, the dictionary I use for count_to_address uses count as a key and then a dictionary as the value. I use a dictionary instead of a list because I will frequently be deleting keys from a dictionary when a count for an ip address is increased. It may look slighly uglier but it is faster to remove a key from a dictionary than it is to remove an element from a list. 

Top100 uses the heap to get the highest counts. It sorts them using the heapq operation to get the 100 largest elements (this is the max size of the heap as well). Using the count it accesses the ip addresses that correspond to that count by using the count_to_address dictionary and iterating over the keys that correspond to the dictionary at that count.

Example:

{1: '{10.0.0.0': 0, '10.0.0.1: 0},  2: {'10.0.0.2': 0}}

You can see that the key is the count and then the key for the nested dictionary is the ip address with a value of zero (its value is arbitrary and doesnt matter).

Top100 keeps track of the amount of elements it has already added to its response to make sure it does not add more than 100 ip addresses. It will stop iterating as soon as it hits 100 so it never iterates over more than 100 ip addresses. 

I built a small function that will print out the top 100 after running the function along with each ip_addresses count. 

Clear just clears both dictionaries and the heap. It is the slowest function. Since it is only ran once a day I decided to not go crazy trying to optimize it.


* What is the runtime complexity of each function?
def requestHandled(self, ipAddress: str)'s time complexity with itself and its helper functions for handling a single request is O(1). Worst case it would have to remove 1 item from the heap and preform a pushpop that also removes and adds an item to the heap. Since the heap is always going to be of size 100 or less it runs closer to constant time. However, if you measured N as the amount of times this function was called it would have a worse-case runtime of O(N) because of the remove called for the heap where it would have to do N removes for N requests on a heap of a size of 100 or less. This is worse case, because many requests will share the same amount of request counts it is less likely it would reach this level of complexity. The heappush and heappop are only done on an array of size 100 or less so they also would not increase the time complexity and are not nested with the remove.

top100 is a constant time function. It only uses the top 100 requests and then will only iterate over at most 100 elements to get the count. The sort at the beginning to get the N largest elements is done on a list of size 100 or less so it will be O(1) as well. It returns an array of the top 100 ip_addresses

Clear will have a runtime efficiency of about (k*n) where k is the number of unique counts and k is the number of unique ip addresses. Since they are both stored in dictionaries clearing them will mean it has to iterate over each of these counts and ip addresses

* What other approaches did you decide not to pursue?
I wanted to use a binary search tree at first but I decided that updating an element that was already in the tree to change its count would be way too. I also thought about just using a pandas dataframe but that is closer to a database and I thought that would be cheating so I decided to not do that.


* How would you test this?

I actually wrote some rough tests to get an idea of how fast my code was running. I maybe spent a little too much time obsessing over this but I wrote an initial test that would call requestHandled() 20 million times giving it a new unique ip address each time (I just gave it a string number for each one to make it easy). I timed it to see what kind of speed I would get. 20 million ran in about 20-30 seconds. I was happy with this because python loops are slow on their own. I then tested how quickly it would take me to get the top 100 with this same object that had 20 million records in it. I got around .0008 seconds for that test. I then called requestHandled() on some existing ip_addresses to make sure I would get the correct top100 back after I called the function. I tested with random inserts where it inserted a random amount of times for  ip addresses 10,000-20,000 where I thought I could get it to have to run a bunch of changes to the count where it would have to delete elements from the heap frequently and I tested the counts to make sure they were accurate. I tested running it 1000 times on an existing ip address, and I tested a single insert. I also tested the clear function which was the slowest other than running requestHandled() 20 million times. I'll include some screenshots of the test results below, the tests themselves are in stress_test.py.  I ran all these on a 2021 M1 macbook pro. I think more testing would be required but for now this is a good measure to see where its at.

