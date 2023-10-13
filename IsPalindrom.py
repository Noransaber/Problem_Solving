# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

def isPalindrome(x):
    
    if x < 0:
        return False
    # Convert int to array
    num_str = str(x)
    num_arr = [int(char) for char in num_str]
    

    # Initialize an empty list for the reversed array
    reversed_num_arr = []

    for i in range(len(num_arr) - 1, -1, -1):
        reversed_num_arr.append(num_arr[i])  # Append elements from the end to the start
        # print(f"num_arra {num_arr}")
        # print(f" revernum_arra {reversed_num_arr}")

    # Check if the original array and the reversed array are the same
    if num_arr == reversed_num_arr:
        return True
    else:
        return False

# Test cases
print(isPalindrome(121))  # Output: True
print(isPalindrome(10))   # Output: False
print(isPalindrome(-121)) # Output: False
