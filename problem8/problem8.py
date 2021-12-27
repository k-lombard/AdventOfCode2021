
def genericparse(file, data):
    file = open(file, 'r')
    
    for line in file:
        line.rstrip()
        line.lstrip()
        line = line.replace("\n", "")
        line = line.split(" | ")
        line = line[1]
        data.append(line)
    
    return data


def solution(data):
    print(data)
    oneSet = set(['c', 'f'])
    fourSet = set(['b', 'c', 'd', 'f'])
    sevenSet = set(['a', 'c', 'f'])
    eightSet = set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    count = 0
    for line in data:
        nums = line.split()
        for num in nums:
            numSet = set(num)
            print(len(numSet.difference(oneSet)))
            if len(numSet) == 2 or len(numSet) == 3 or len(numSet) == 4 or len(numSet) == 7:
                count += 1
    return count

def solution2(data):
    print(data)
    numMap = {frozenset(list('cdfbe')): 5, frozenset(list('gcdfa')): 2, frozenset(list('fbcad')): 3, frozenset(list('cefabd')): 9, frozenset(list('cdfgeb')): 6, frozenset(list('cagedb')): 0}
    count = 0
    for line in data:
        nums = line.split()
        currStr = ""
        for num in nums:
            if len(num) == 7:
                currStr = currStr + '8'
            elif len(num) == 2:
                currStr = currStr + '1'
            elif len(num) == 4:
                currStr = currStr + '4'
            elif len(num) == 3:
                currStr = currStr + '7'
            else:
                currStr = currStr + str(numMap[frozenset(list(num))])
        count += int(currStr)
    return count
print(solution2(genericparse("problem8.txt", [])))