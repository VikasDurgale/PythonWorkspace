"""
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Input Format:
The first line contains a string consisting of space separated words.

Output Format:
Print the formatted string as explained above.
"""

def split_and_join(line):
    line_list = line.split(" ")
    line = "-".join(line_list)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)