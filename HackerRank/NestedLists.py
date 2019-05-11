"""
Problem Statement:
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format:
The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

Constraints:
2 <= N <= 5
There will always be one or more students having the second lowest grade.

Output Format:
Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
"""

from operator import itemgetter

if __name__ == '__main__':
    student = list()
    for _ in range(int(input())):
        student.append([input(), float(input())])

student.sort(key=itemgetter(1))

lowest = student[0][1]
count = True
second_lowest = 0
names = list()
for s in student:
    if lowest == s[1]:
        continue

    if count:
        second_lowest = s[1]
        count = False

    if second_lowest == s[1]:
        names.append(s[0])
    else:
        break

names.sort()
for n in names:
    print(n)