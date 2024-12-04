
INCREASING = 1
DECREASING = -1

GRADUAL_MAX = 3
GRADUAL_MIN = 1


def changeIsGradual(magnitude):
    return magnitude >= GRADUAL_MIN and magnitude <= GRADUAL_MAX

def directionChanges(levelDirection, diff):
    return (levelDirection == INCREASING and diff > 0) or (levelDirection == DECREASING and diff < 0)


def reportIsSafe(levels):
    levelDirection = 0
    index = 0
    
    if levels[0] - levels[1] > 0:
        levelDirection = DECREASING
    else:
        levelDirection = INCREASING
    
    
    while(index < len(levels) - 1):
        
        diff = levels[index] - levels[index + 1]
        
        if changeIsGradual(abs(diff)) is False or directionChanges(levelDirection, diff):
            return False

        index = index + 1
    return True
        
safeCount = 0

file = open("input.txt", "r")
for line in file:
    numbers = list(map(lambda x: int(x), line.split()))
    if reportIsSafe(numbers) == True:
        safeCount = safeCount + 1
              
print(safeCount)