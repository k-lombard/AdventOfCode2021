def genericparse(file, data):
    file = open(file, 'r')
    
    for line in file:
        line.rstrip()
        line.lstrip()
        line = line.replace("\n", "")
        line = line.split(" -> ")
        commaIdx1 = line[0].index(',')
        commaIdx2 = line[1].index(',')
        line2 = [(int(line[0][:commaIdx1]), int(line[0][commaIdx1+1:])), (int(line[1][:commaIdx2]), int(line[1][commaIdx2+1:]))]
        data.append(line2)
    
    return data


def solution(data):
    max_x = 0
    max_y = 0
    for vec in data:
        if vec[0][0] > max_x:
            max_x = vec[0][0]
        if vec[0][1] > max_y:
            max_y = vec[0][1]
        if vec[1][0] > max_x:
            max_x = vec[1][0]
        if vec[1][1] > max_y:
            max_y = vec[1][1]
    print(max_x, max_y)
    dim = max(max_x, max_y)
    row = [[None] * dim]
    matrix = dim * row
    visited = set([])
    twice = set([])
    for vec in data:
        if vec[0][0] == vec[1][0]:
            if vec[0][1] > vec[1][1]:
                for num in range(vec[0][1], vec[1][1]-1, -1):
                    tup = (vec[1][0], num)
                    print(tup, vec)
                    if tup in visited:
                        twice.add(tup)
                    visited.add(tup)
            else:
                for num in range(vec[0][1], vec[1][1]+1):
                    tup = (vec[1][0], num)
                    print(tup, vec)
                    if tup in visited:
                        twice.add(tup)
                    visited.add(tup)
        elif vec[0][1] == vec[1][1]:
            if vec[0][0] > vec[1][0]:
                for num in range(vec[0][0], vec[1][0]-1, -1):
                    tup = (num, vec[0][1])
                    print(tup, vec)
                    if tup in visited:
                        twice.add(tup)
                    visited.add(tup)
            else:
                for num in range(vec[0][0], vec[1][0]+1):
                    tup = (num, vec[0][1])
                    print(tup, vec)
                    if tup in visited:
                        twice.add(tup)
                    visited.add(tup)
        else:
            num = vec[0][0]
            num2 = vec[0][1]
            if vec[0][0] > vec[1][0] and vec[0][1] > vec[1][1]:
                while num >= vec[1][0] and num2 >= vec[1][1]:
                    tup = (num, num2)
                    if tup in visited:
                        twice.add(tup)
                    visited.add(tup)
                    num -= 1
                    num2 -= 1
            elif vec[0][0] > vec[1][0] and vec[0][1] < vec[1][1]:
                while num >= vec[1][0] and num2 <= vec[1][1]:
                    tup = (num, num2)
                    if tup in visited:
                        twice.add(tup)
                    visited.add(tup)
                    num -= 1
                    num2 += 1
            elif vec[0][0] < vec[1][0] and vec[0][1] > vec[1][1]:
                while num <= vec[1][0] and num2 >= vec[1][1]:
                    tup = (num, num2)
                    if tup in visited:
                        twice.add(tup)
                    visited.add(tup)
                    num += 1
                    num2 -= 1
            else:
                while num <= vec[1][0] and num2 <= vec[1][1]:
                    tup = (num, num2)
                    if tup in visited:
                        twice.add(tup)
                    visited.add(tup)
                    num += 1
                    num2 += 1
    return len(twice)


print(solution(genericparse("problem5.txt", [])))
# print(solution(genericparse("problem5-2.txt", [])))