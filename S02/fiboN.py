def fibonnacin(n):
    series = [0, 1]
    for i in range(2, n):
        next_number = series[-1] + series[-2]
        series.append(next_number)
    return series
n = fibonnacin(20)
print("The 5th Fibonnaci number is:", n[5])
print("The 10th Fibonnaci number is:", n[10])
print("The 15th Fibonnaci number is:", n[15])