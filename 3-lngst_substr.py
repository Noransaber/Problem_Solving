#!/usr/bin/python3
"""
This module prints the longest substring NOT subsequence in a string
This string is to be entered by the user
For Instance:
- Input: s = "abcabcbb"
    Output: 3
  Explanation: The answer is "abc", with the length of 3.

- Input: s = "bbbbb"
    Output: 1
  Explanation: The answer is "b", with the length of 1.

- Input: s = "pwwkew"
    Output: 3
  Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and
    not a substring.

- input s = "12344567890"
    Output: 7
  Explanation: The answer is "4567890" with the length of 7.
"""


def longest_substring():
    # receive input from user
    user_input = input("Please enter any text: ")

    res_substr = ""
    checks = ""

    # loop through the string entered by user
    for char in user_input:
        # check if character is already in checks string
        if char in checks:
            # if it is check if the len is greater than the variable
            # holding our longst substr
            if len(res_substr) < len(checks):
                # if it is, assign checks to longest substring
                res_substr = checks
            # reset checks
            checks = ""
            # assign the substring breaker to checks
            checks = char
            # move to the next char
            continue
        # if char is not yet in checks add it to checks
        checks += char

    if (len(res_substr) < len(checks)):
        res_substr = checks
    print(len(res_substr))


if __name__ == "__main__":
    longest_substring()
