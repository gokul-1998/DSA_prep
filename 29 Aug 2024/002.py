s = "]"

output = True

#   SOLUTION 1
def isValid( s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping and stack:
            top_element = stack.pop()
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
        
print(isValid(s))


#  SOLUTION 2
# https://chatgpt.com/share/880b17fe-e7f3-4ac6-990b-de6806d5f23e
def isValid(s):
    if len(s) % 2 != 0:  # Early exit if length is odd
        return False
    
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            if stack and stack[-1] == mapping[char]:
                stack.pop()  # Pop if there is a matching pair
            else:
                return False  # Early exit on mismatch
        else:
            stack.append(char)
    
    return not stack  # Valid if stack is empty at the end

# Example usage
s = "({[]})"
print(isValid(s))  # Output: True
