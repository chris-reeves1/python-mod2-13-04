# collections of values - storing data.
# lists, dictionaries, sets, tuples.

# lists - ordered(indexed), mutable, duplicate ok, any data type. 
# dictionaries - unordered(no index), key:value pair, any datatype fine + no key duplicates.

# x = hash("hello"): 1
# print(x)
# mem = x%(16 - 1)

# import sys
# d = {}
# for i in range(80):
#     d[i] = i
#     print(sys.getsizeof(d))

# import time 

# large_dict = {num : True for num in range(10_000_000)}
# large_list = list(range(10_000_000))

# target = 9_999_990

# start = time.time()
# search = target in large_list
# finish = time.time()
# print(f"list: {finish - start:.10f}")

# start = time.time()
# search = target in large_dict
# finish = time.time()
# print(f"dict: {finish - start:.10f}")

drinks = {"still": "water", "fizzy": "cola"}

# print(drinks["stilll"])
print(drinks.get("stilll", ))
string method
.join()

exercise:
    - make a dictionary with keys as authors and 3 books per author.
    - input asking the user for an author name (think about ux here).
    - print the authors books AS A STRING!!!!!!!!!!!!!!!!!!!!!!!!!!
    - error handling for author names.
    - use built-ins/methods and only things we have covered.
    - JUSTIFY YOUR CHOICES!
    - later full schema design.  

