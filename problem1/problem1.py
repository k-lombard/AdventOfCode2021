def genericparse(file, data):
    file = open(file, 'r')
    
    for line in file:
        line.rstrip()
        line.lstrip()
        line = int(line.replace("\n", ""))
        data.append(line)

    
    return data



def solution(data):
    print(data)
    i = 0
    count = 0
    while i < len(data) - 1:
        if data[i+1] > data[i]:
            count += 1
        i += 1
    return count

def solution2(data):
    i = 0
    count = 0
    while i < len(data)-3:
        if data[i+1] + data[i+2] + data[i+3] > data[i] + data[i+1] + data[i+2]:
            count += 1
        i += 1
    return count


print(solution(genericparse("problem1.txt", [])))
print(solution2(genericparse("problem1.txt", [])))