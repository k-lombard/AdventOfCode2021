def genericparse(file, data):
    file = open(file, 'r')
    
    for line in file:
        line.rstrip()
        line.lstrip()
        line = line.replace("\n", "")
        data.append(line)
    
    return data

class Submarine:
    def __init__(self):
        self.depth = 0
        self.horizontal = 0
        self.aim = 0

    def moveHor(self, amt):
        self.horizontal += amt
    def moveVert(self, amt):
        self.depth += amt

    
    def parseCmd(self, data):
        print(data)
        for item in data:
            if "down" in item:
                # self.moveVert(int(item[-1]))
                self.aim += int(item[-1])
            elif "up" in item:
                # self.moveVert(-int(item[-1]))
                self.aim -= int(item[-1])
            elif "forward" in item:
                self.moveHor(int(item[-1]))
                self.depth += (self.aim * int(item[-1]))
        return self.depth*self.horizontal

sub = Submarine()
print(sub.parseCmd(genericparse("problem2.txt", [])))