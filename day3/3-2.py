from input import input

def getGroupDuplicates(elf1: str, elf2: str, elf3: str) -> list:
    duplicates = []
    for itemFrom1 in elf1:
        if elf2.find(itemFrom1) >= 0 and elf3.find(itemFrom1) >= 0 and itemFrom1 not in duplicates:
            duplicates.extend(itemFrom1)
    return duplicates

def getDuplicatePriority(duplicates: list) -> int:
    priorityList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priorityScore = 0
    for duplicate in duplicates:
        priorityScore += (priorityList.index(duplicate) + 1)
    return priorityScore


sumOfPriorityScore = 0
elfGroup = []

for rucksack in input.splitlines():
    elfGroup.append(rucksack)

    if len(elfGroup) == 3:
        groupDuplicates = getGroupDuplicates(elfGroup[0], elfGroup[1], elfGroup[2])
        sumOfPriorityScore += getDuplicatePriority(groupDuplicates)
        elfGroup = []

print(sumOfPriorityScore)
