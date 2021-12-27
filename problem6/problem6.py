def genericparse(file, data):
    file = open(file, 'r')
    
    for line in file:
        line.rstrip()
        line.lstrip()
        line = line.replace("\n", "")
        line = line.split(',')
        data.append(line)
    
    return data


def solution(data):
    data = data[0]
    # data = [3,4,3,1,2]
    num = 0
    while num < len(data):
        data[num] = int(data[num])
        num += 1
    data2 = {}
    for num in data:
        if num not in data2:
            data2[num] = 1
        else:
            data2[num] += 1
    count = 0
    while count < 256:
        newDict = {}
        for num in range(8,-1, -1):
            if num in data2:
                if num > 0:
                    newDict[num-1] = data2[num]
                else:
                    if 6 in newDict:
                        newDict[6] += data2[num]
                    else:
                        newDict[6] = data2[num]
                    if 8 in newDict:
                        newDict[8] += data2[num]
                    else:
                        newDict[8] = data2[num]
        data2 = newDict

        count += 1
    sum1 = 0
    for val in list(data2.values()):
        sum1 += val
    return sum1


print(solution(genericparse("problem6.txt", [])))