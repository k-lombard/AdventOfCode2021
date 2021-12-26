
def genericparse(file, data):
    file = open(file, 'r')
    
    for line in file:
        line.rstrip()
        line.lstrip()
        line = line.replace("\n", "")
        data.append(line)
    
    return data



def solution1(data):
    idx = 0
    while idx < len(data[0]):
        freq = {}
        for item in data:
            if item[idx] not in freq:
                freq[item[idx]] = 1
            else:
                freq[item[idx]] += 1
        greater = max(freq, key=freq.get)
        temp = list(freq.values())
        if temp[0] == temp[1]:
            greater = '1'
        
        i = 0
        while i < len(data):
            if data[i][idx] == greater:
                i += 1
                continue
            else:
                del data[i]
                continue
        if len(data) == 1:
            return data[0]
        idx += 1
    return data[0]

def solution2(data):
    idx = 0
    while idx < len(data[0]):
        freq = {}
        for item in data:
            if item[idx] not in freq:
                freq[item[idx]] = 1
            else:
                freq[item[idx]] += 1
        lower = min(freq, key = freq.get)
        temp = list(freq.values())
        if temp[0] == temp[1]:
            lower = '0'
        i = 0
        while i < len(data):
            if data[i][idx] == lower:
                i += 1
                continue
            else:
                del data[i]
                continue
        if len(data) == 1:
            return data[0]
        idx += 1
    return data[0]

print(int(solution1(genericparse("problem3.txt", [])),2) * int(solution2(genericparse("problem3.txt", [])),2))