num_command = int(input())
total = 0
for i in range(num_command):
    command = input()
    if command == "X++" or command == "++X":
        total += 1
    elif command == "X--" or command == "--X":
        total -= 1
print(total)