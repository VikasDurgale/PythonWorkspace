"""
Given an integer, n, print the following values for each integer i from 1 to n:
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary
The four values must be printed on a single line in the order specified above for each i from 1 to n. Each value should
be space-padded to match the width of the binary value of n.

Input Format:
A single integer denoting n.

Constraints:
1 <= n <= 99

Output Format:
Print  lines where each line  (in the range ) contains the respective decimal, octal, capitalized hexadecimal, and binary values of . Each printed value must be formatted to the width of the binary value of .
"""


def print_formatted(number):
    width = len("{0:b}".format(n))
    for i in range(number):
        decimal = i + 1
        octal = oct(decimal)
        hexa = str(hex(decimal)).upper()
        binary = bin(decimal)
        print(str(decimal).rjust(width, ' ') + " " + str(octal)[2:].rjust(width, ' ') + " " + hexa[2:].rjust(width, ' ')
              + " " + str(binary)[2:].rjust(width, ' '))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)