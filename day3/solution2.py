
import re


file = open("input.txt", "r")

input = file.read()

sum = 0
active = True

results = re.findall(r'(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\))', input)
for res in results:
    
    if res == "do()":
        active = True
    elif res == "don't()":
        active = False
    else:
        if active == True:
            m =  re.match(r'mul\((\d+),(\d+)\)',res)
            x = int(m.group(1))
            y = int(m.group(2))
        
            sum = sum + (x * y)
print(sum)
    
