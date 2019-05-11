"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring
occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format:
The first line of input contains the original string. The next line contains the substring.

Constraints:
1 <= len(string) <= 200
Each character in the string is an ascii character.

Output Format:
Output the integer number indicating the total number of occurrences of the substring in the original string.
"""


def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)
    string_len = len(string)
    for i in range(0, (string_len-sub_len)+1):
        temp = string[i:sub_len+i]
        if temp == sub_string:
            count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)