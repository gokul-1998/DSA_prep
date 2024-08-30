s = "III"
output=3
s = "LVIII"
output=58
s = "MCMXCIV"
output=1994

#   SOLUTION 1
def romanToInt(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0
    for i in s:
        if roman_dict[i] > prev:
            result += roman_dict[i] - 2 * prev
        else:
            result += roman_dict[i]
        print(result,i,roman_dict[i],prev)
        prev = roman_dict[i]
    return result

print(romanToInt(s))


#   SOLUTION 2
def romanToInt(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s) - 1):
        current = roman_dict[s[i]]
        next = roman_dict[s[i + 1]]
        if current < next:
            result -= current
        else:
            result += current
    result += roman_dict[s[-1]]
    return result

# Test cases
print(romanToInt("III"))      # Output: 3
print(romanToInt("LVIII"))    # Output: 58
print(romanToInt("MCMXCIV"))  # Output: 1994


# Explanation of the changes:
# Iteration over s with indices: Instead of checking the previous value during the iteration, we can directly compare the current value with the next value using the index. This avoids the need for the prev variable.

# Simplified logic: The logic is simplified by directly subtracting the current value if it's less than the next value, and adding it otherwise. Finally, we add the value of the last character in the string to the result.

# Efficiency: The time complexity remains O(n), where n is the length of the string, but the code is now cleaner and slightly faster due to the reduced number of operations.

# This version is more concise and just as efficient, with the added benefit of being easier to understand.