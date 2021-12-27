import math
def genericparse(file, data):
    file = open(file, 'r')
    
    for line in file:
        line.rstrip()
        line.lstrip()
        line = line.replace("\n", "")
        line = line.split(',')
    
    return line


def solution(data):
    i = 0
    while i < len(data):
        data[i] = int(data[i])
        i += 1
    intSet = set(data)
    minDist = float("inf")
    for num in range(min(intSet), max(intSet)+1):
        tot = 0
        for pos in data:
            tot += sum(range(0, abs(pos-num)+1))
        minDist = min(tot, minDist)
    return minDist

print(solution(genericparse("problem7.txt", [])))