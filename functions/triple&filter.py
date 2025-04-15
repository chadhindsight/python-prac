def triple_and_filter(li):
   return [num * 3 for num in li if num % 4 == 0]

# Alternative solution 
def triple_and_filter(lst):
    return list(map(lambda x: x * 3, filter(lambda x: x % 4 == 0, lst)))   