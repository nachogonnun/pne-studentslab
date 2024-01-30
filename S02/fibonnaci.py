N = 11
s = [0, 1]
for i in range(2, N):
    next_number = s[-1] + s[-2]
    s.append(next_number)
print(s)

