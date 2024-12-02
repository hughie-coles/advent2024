


sum = 0
list1 = []
list2 = []

file = open("input.txt", "r")
for line in file:
    numbers = line.split()
    list1.append(int(numbers[0]))
    list2.append(int(numbers[1]))

list1.sort()
list2.sort()

for i, _ in enumerate(list1):
    sum = sum + abs(list1[i] - list2[i])
    
print(sum)


