from collections import defaultdict
from functools import reduce
from collections import Counter

def counter_counter(items):
    # Using collections.Counter
    # counter = dict(Counter(items))
    # OR manual one-pass:
    counts = {}
    for x in items:
        counts[x] = counts.get(x, 0) + 1
        print(f"Counting {x}: {counts[x]}")
        print(counts.get(x, 0))
    return counts
        
        
        
def dict_counter(items):
    # Using dict comprehension
    return {item: items.count(item) for item in set(items)}

def dict_counter_defaultdict(items):
    # Using defaultdict
    counter = defaultdict(int)
    for item in items:
        counter[item] += 1
    return dict(counter) 

def dict_counter_map_reduce(items):
    # Using map and reduce
    def reducer(acc, item):
        acc[item] = acc.get(item, 0) + 1
        return acc
    return reduce(reducer, items, {})

def dict_counter_filter(items):
    # Using filter and dict comprehension (not efficient, but for demonstration)
    return {item: len(list(filter(lambda x: x == item, items))) for item in set(items)}

if __name__ == "__main__":
    data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

    print("Dict comprehension:", dict_counter(data))
    print("Defaultdict:", dict_counter_defaultdict(data))
    print("Map/Reduce:", dict_counter_map_reduce(data))
    print("Filter:", dict_counter_filter(data))
    print("Counter:", counter_counter(data))
    