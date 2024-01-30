def fibonnaci(n):
    series = [0, 1]
    for i in range(2, n):
        next_number = series[-1] + series[-2]
        series.append(next_number)
    return series

def sum_n_fibonnaci_numbers(n):
    s = fibonnaci(n)
    addition = 0
    for i in s:
        addition += i
    return addition
print("The sum of the first 5 terms is", sum_n_fibonnaci_numbers(6))
print("The sum of the first 10 terms is", sum_n_fibonnaci_numbers(11))