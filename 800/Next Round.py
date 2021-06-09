num_of_par, avg = list(input().split())
scores = list(input().split())
average = int(avg)-1 
total = 0
n = 0
for i in scores:
    if int(i) >= int(scores[average]) and int(i) > 0:
        total += 1
    n += 1
print(total)
