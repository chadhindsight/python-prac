# Return True if all elements of the iterable are truthy
nums = [2, 6, 12, 8]
all([num % 2 == 0 for num in nums])

# Return True if any elements in the iterable are truthy
nums2 = [2, 6, 12, 9]
print(any([num % 2 == 0 for num in nums]))

# implement a function is_all_strings  that accepts a single iterable and returns True if it contains ONLY strings.  
def is_all_strings(strs):
    return all(type(ting) == str for ting in strs)