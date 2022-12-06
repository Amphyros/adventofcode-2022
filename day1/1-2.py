from input import input

mostCalories = 0
secondMostCalories = 0
thirdMostCalories = 0
currentCalories = 0

def rankCalories(calories) -> None:
    global mostCalories
    global secondMostCalories
    global thirdMostCalories
    
    if calories > mostCalories:
        thirdMostCalories = secondMostCalories
        secondMostCalories = mostCalories
        mostCalories = calories
        return
    if calories > secondMostCalories:
        thirdMostCalories = secondMostCalories
        secondMostCalories = calories
        return
    if calories > thirdMostCalories:
        thirdMostCalories = calories


inCalculation = False

for food in input.splitlines():
    if food == '':
        rankCalories(currentCalories)
        currentCalories = 0
        inCalculation = False
        continue

    currentCalories += int(food)
    inCalculation = True

if inCalculation:
    rankCalories(currentCalories)
    currentCalories = 0
    inCalculation = False

print(mostCalories + secondMostCalories + thirdMostCalories)