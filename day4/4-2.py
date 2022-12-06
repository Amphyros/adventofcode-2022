from input import input

def getSectionList(sectionRange: str) -> list:
    sectionRangeList = sectionRange.split("-")
    sectionList = []

    for ID in range( int(sectionRangeList[0]), (int(sectionRangeList[1]) + 1) ):
        sectionList.append(ID)
    
    return sectionList

def hasSectionOverlap(sectionList1: list, sectionList2: list) -> bool:
    for ID in sectionList1:
        if ID in sectionList2:
            return True

    return False


overlappedGroupAmount = 0

for pair in input.splitlines():
    pairList = pair.split(",")
    elf1 = getSectionList(pairList[0])
    elf2 = getSectionList(pairList[1])

    if hasSectionOverlap(elf1, elf2):
        overlappedGroupAmount += 1

print(overlappedGroupAmount)