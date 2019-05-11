"""
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format:
A single line containing a string S.

Constraints:
0 < lens(S) < 1000

Output Format:
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
"""

if __name__ == '__main__':
    s = input()

lower_alpha, upper_alpha, alpha, digit = False, False, False, False
for a in s:
    if a.isalpha():
        alpha = True
        if a.islower():
            lower_alpha = True
        if a.isupper():
            upper_alpha = True
    if a.isdigit():
        digit = True
    if lower_alpha and upper_alpha and digit:
        break

if s.isalnum():
    print("True")
else:
    print("False")
print(alpha)
print(digit)
print(lower_alpha)
print(upper_alpha)