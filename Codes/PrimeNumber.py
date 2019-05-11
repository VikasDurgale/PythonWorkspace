number = 19

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, " is not a prime number.")
            break
    else:
        print(number, " is a prime number.")
else:
    print(number, " is a prime number.")
"""arr = [-4, -5, -3, -5, -2]
n=5
runner_up = max(arr)
for i in range(n):
    if runner_up == max(arr):
        arr.remove(max(arr))

print(max(arr))"""