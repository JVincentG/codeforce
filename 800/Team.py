num_of_problem = int(input())
total = 0
for i in range(num_of_problem):
    decision = input()
    if decision.count('1') >= 2:
        total +=1
print (total)