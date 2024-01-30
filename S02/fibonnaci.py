N = 11
series = [0, 1]
for i in range(2, N):
    next_number = series[-1] + series[-2]
    series.append(next_number)
print(series)

