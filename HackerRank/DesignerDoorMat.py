"""Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Sample Designs

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

Input Format:
A single line containing the space separated values of N and M.

Constraints:
5 < N < 101
15 < M < 303

Output Format:
Output the design pattern.
"""

if __name__ == '__main__':
    line = input()
    rows, cols = map(int, line.split())

width = cols
patterns = list()
mid = rows//2
# Top
for n in range(mid):
    pattern = [('.|.'*(2*n + 1)).center(width, '-')]
    patterns.append(pattern)
    print('\n'.join(pattern))

# Middle
print('WELCOME'.center(width, '-'))

# Bottom
for n in range(mid, rows-1):
    print("\n".join(patterns[mid-1]))
    mid -= 1