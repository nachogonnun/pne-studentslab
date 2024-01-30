def sum_n(n):
    res = 0

    for i in range(1, n+1):
        res += i

    return res

print("The sum of the first 20 integers is: ", sum_n(20))
print("The sum of the first 400 integers is: ", sum_n(400))