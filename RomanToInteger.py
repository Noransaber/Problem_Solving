def romanToInteger(s):
    roman_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    prev_value = 0

    for c in s[::-1]:  # Iterate the string in reverse order
        value = roman_to_int[c]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result

print(romanToInteger("III"))      # Output: 3
print(romanToInteger("LVIII"))    # Output: 58
print(romanToInteger("MCMXCIV"))  # Output: 1994
