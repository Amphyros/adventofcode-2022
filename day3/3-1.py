from input import input

def getCompartmentContent(rucksack: str) -> list:
    rucksackCut = int(len(rucksack) / 2)
    return [rucksack[:rucksackCut], rucksack[rucksackCut:]]

def getDuplicatesInCompartments(compartment1: str, compartment2: str) -> list:
    duplicates = []
    for itemIn1 in compartment1:
        for itemIn2 in compartment2:
            if itemIn1 == itemIn2 and itemIn1 not in duplicates:
                duplicates.extend(itemIn1)
    return duplicates

def getDuplicatePriority(duplicates: list) -> int:
    priorityList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priorityScore = 0
    for duplicate in duplicates:
        priorityScore += (priorityList.index(duplicate) + 1)
    return priorityScore


sumOfPriorityScore = 0
for rucksack in input.splitlines():
    rucksackCompartments = getCompartmentContent(rucksack)
    compartmentDuplicates = getDuplicatesInCompartments(rucksackCompartments[0], rucksackCompartments[1])
    sumOfPriorityScore += getDuplicatePriority(compartmentDuplicates)

print(sumOfPriorityScore)

