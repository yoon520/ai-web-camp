li = [1, 2, 3, 4, 5, 3, 3, 4, 5, 2, 2, 6]
li_a = []

for i in li:
    if i not in li_a:
        li_a.append(i)

print(li_a)     # [1, 2, 3, 4, 5, 6]