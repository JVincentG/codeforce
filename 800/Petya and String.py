one = input().lower()
two = input().lower()
total = 0
for i in range(len(one)):
    if one[i] > two[i]:
        total += 1
    elif one[i] < two[i]:
        total -= 1
    if total == 1 or total == -1:
        break
print(total)