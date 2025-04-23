def decodeString(s: str):
    current_string = ""
    k = 0
    stack = []

    for char in s:
        if char.isdigit():
            k = k * 10 + int(char)  # handles multi-digit numbers

        elif char == "[":
           stack.append((current_string, k))
           current_string = ""
           k = 0

        elif char == "]":
            popped_vals = stack.pop()
            current_string = popped_vals[0]+ current_string * popped_vals[1]  
        
        else: 
            current_string += char 
    return current_string        

print(decodeString("2[abc]3[cd]ef"))