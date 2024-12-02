


list1 = []
list2 = []
similarity_score = 0

file = open("input.txt", "r")
for line in file:
    numbers = line.split()
    list1.append(int(numbers[0]))
    list2.append(int(numbers[1]))


list2_frequency_map = {}

for x in list2:
    if list2_frequency_map.get(x) is not None:
        list2_frequency_map[x] = list2_frequency_map[x] + 1
    else:
        list2_frequency_map[x] = 1


for x in list1:
    occurances = list2_frequency_map.get(x,0)
    similarity_score = similarity_score +  (x * occurances)
    
print(similarity_score)


