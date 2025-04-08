# Return True if all elements of the iterable are truthy
nums = [2, 6, 12, 8]
all([num % 2 == 0 for num in nums])

# Return True if any elements in the iterable are truthy
nums2 = [2, 6, 12, 9]
print(any([num % 2 == 0 for num in nums]))