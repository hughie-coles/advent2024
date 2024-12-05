
import re


file = open("input.txt", "r")

input = file.read()

sum = 0

results = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', input)
for res in results:
    m =  re.match(r'mul\((\d+),(\d+)\)',res)
    x = int(m.group(1))
    y = int(m.group(2))
    
    sum = sum + (x * y)
print(sum)
    
