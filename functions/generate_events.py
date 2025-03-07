def generate_evens():
    ans = []
        
    for num in range(1, 50):
        if num % 2 == 0:
            ans.append(num)
    return ans