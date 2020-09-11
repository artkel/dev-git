

lst = [round(x ** (1/4), 4) for x in range(1, 101, 3) if x % 2 != 0]
print(sum(lst) / len(lst))

