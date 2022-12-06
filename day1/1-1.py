from input import input

mostCalories = 0
currentCalories = 0

for food in input.splitlines():
    if food != '':
        currentCalories += int(food)
        continue

    if currentCalories > mostCalories:
        mostCalories = currentCalories
    
    currentCalories = 0


print(mostCalories)