def genericparse(file, data):
    file = open(file, 'r')
    
    for line in file:
        line.rstrip()
        line.lstrip()
        line = line.replace("\n", "")
        data.append(line)
    
    return data

def boardparse(file, data):
    file = open(file, 'r')
    board = []
    output = []
    for line in file:
        line.rstrip()
        line.lstrip()
        line = line.replace("\n", "")
        line = line.split()
        if len(line) > 0:
            board = board + [line]
        else:
            output = output + [board]
            board = []
    return output

def dfsRight(row, col, currSet, board, output, visited, boards):
    if board[row][col] in currSet:
        visited.add((row,col))
        if col == 4 and len(visited) == 5:
            if board not in output:
                output.append(board)
            return
        if col == 4:
            return
        dfsRight(row, col + 1, currSet, board, output, visited, boards)
    else:
        return


def dfsDown(row, col, currSet, board, output, visited, boards):
    if board[row][col] in currSet:
        visited.add((row,col))
        if row == 4 and len(visited) == 5:
            if board not in output:
                output.append(board)
            return
        dfsDown(row+1, col, currSet, board, output, visited, boards)
    else:
        return

def solution(nums, boards):
    length = len(boards)
    nums = nums[0].split(',')
    currSet = set(nums[0:5])
    currIdx = 4
    notFound = True
    foundBoard = []
    output = []
    while notFound:
        for board in boards:
            if board not in output:
                row = 0
                column = 0
                while row < 5:
                    newset = set([])
                    dfsRight(row, 0, currSet, board, output, newset, boards)
                    if len(output) == length:
                        notFound = False
                    row += 1
                row = 0
                column = 0
                while column < 5:
                    newset2 = set([])
                    dfsDown(0, column, currSet, board, output, newset2, boards)
                    if len(output) == length:
                        notFound = False
                        break
                    column += 1
        if currIdx < len(nums)-1 and notFound == True:
            currIdx += 1
            currSet.add(nums[currIdx])
        else:
            break
    foundBoard = output[-1]
    currSum = 0
    for row in foundBoard:
        for num in row:
            if num not in currSet:
                currSum += int(num)
    return currSum * int(nums[currIdx])



print(solution(genericparse("problem4-1.txt", []), boardparse("problem4-2.txt", [])))
# print(solution(genericparse("problem4test1.txt", []), boardparse("problem4test2.txt", [])))

