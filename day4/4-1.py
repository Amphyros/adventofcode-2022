from input import input

def getSectionList(sectionRange: str) -> list:
    sectionRangeList = sectionRange.split("-")
    sectionList = []

    for ID in range( int(sectionRangeList[0]), (int(sectionRangeList[1]) + 1) ):
        sectionList.append(ID)
    
    return sectionList

def isSectionFullyOverlapped(sectionList1: list, sectionList2: list) -> bool:
    biggerList = sectionList1
    smallerList = sectionList2
    if len(sectionList1) < len(sectionList2):
        biggerList = sectionList2
        smallerList = sectionList1
    
    for ID in smallerList:
        if ID not in biggerList:
            return False

    return True


overlappedGroupAmount = 0

for pair in input.splitlines():
    pairList = pair.split(",")
    elf1 = getSectionList(pairList[0])
    elf2 = getSectionList(pairList[1])

    if isSectionFullyOverlapped(elf1, elf2):
        overlappedGroupAmount += 1

print(overlappedGroupAmount)