"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

Input Format:
A single line containing a string S.

Constraints:
0 < len(s) < 1000

Output Format:
Print the modified string S.
"""

"""Method 1


def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
"""

"""Method 2"""


def swap_case(s):
    new_string = ''
    for a in s:
        if a.islower():
            new_string += a.upper()
        elif a.isupper():
            new_string += a.lower()
        else:
            new_string += a

    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)