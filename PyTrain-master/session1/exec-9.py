list_1 = [10, 11, 12, 13]
list_2 = [1, 2, 3, 4]

# result = [11, 13, 2, 4]

result = []

for i in list_1:
    if i % 2 != 0:
        result.append(i)


for i in list_2:
    if i % 2 == 0:
        result.append(i)


print(result)