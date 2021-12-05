import pprint
import re


def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines


def testAndVerify(taskNr, taskResult, correctAnswer):
    rightOrWrong = ""
    if taskResult == correctAnswer:
        rightOrWrong = "Correct"
    else:
        rightOrWrong = "Wrong"
    print("Task " + str(taskNr) + ", Test:   " + taskResult + ", " + rightOrWrong)


def parseData(data):
    numbers = data[0].split(",")
    nrOfBoards = int((len(data) - 1) / 6)

    boards = []
    boardCheck = []
    for i in range(nrOfBoards):
        board = {}
        for rowIdx, line in enumerate(data[i*6 + 2 : i*6 + 2 + 5]):
            rowNbrs = [x for x in line.split(" ") if x != '']
            for colIdx, nbr in enumerate(rowNbrs):
                board[nbr] = { "row": rowIdx, "col": colIdx, "marked": False }

        boards.append(board)
        boardCheck.append({ "colCnt": [0, 0, 0, 0, 0], "rowCnt": [0, 0, 0, 0, 0], "finished": False})
    return numbers, boards, boardCheck


def task1(data):
    numbers, boards, boardCheck = parseData(data)
    
    winner = False
    winScore = 0
    for lottoNr in numbers:
        for boardIdx, board in enumerate(boards):
            if lottoNr in board.keys():
                board[lottoNr]["marked"] = True
                boardCheck[boardIdx]['colCnt'][board[lottoNr]["col"]] += 1
                boardCheck[boardIdx]['rowCnt'][board[lottoNr]["row"]] += 1
                if boardCheck[boardIdx]['colCnt'][board[lottoNr]["col"]] == 5 or boardCheck[boardIdx]['rowCnt'][board[lottoNr]["row"]] == 5:
                    for nbr in board.keys():
                        if board[nbr]['marked'] == False:
                            winScore += int(nbr)
                    winScore *= int(lottoNr)
                    winner = True
                    break
        if winner:
            break
    return winScore

    
def task2(data):
    numbers, boards, boardCheck = parseData(data)
    
    winner = False
    winScore = 0
    boardsFinished = 0
    for lottoNr in numbers:
        for boardIdx, board in enumerate(boards):
            if not boardCheck[boardIdx]['finished']:
                if lottoNr in board.keys():
                    board[lottoNr]["marked"] = True
                    boardCheck[boardIdx]['colCnt'][board[lottoNr]["col"]] += 1
                    boardCheck[boardIdx]['rowCnt'][board[lottoNr]["row"]] += 1
                    if boardCheck[boardIdx]['colCnt'][board[lottoNr]["col"]] == 5 or boardCheck[boardIdx]['rowCnt'][board[lottoNr]["row"]] == 5:
                        boardCheck[boardIdx]['finished'] = True
                        boardsFinished += 1
                        if boardsFinished == len(boards):
                            for nbr in board.keys():
                                if board[nbr]['marked'] == False:
                                    winScore += int(nbr)
                            winScore *= int(lottoNr)
                            winner = True
                            break
        if winner:
            break
    return winScore


testData = ["7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
"",
"22 13 17 11  0",
" 8  2 23  4 24",
"21  9 14 16  7",
" 6 10  3 18  5",
" 1 12 20 15 19",
"",
" 3 15  0  2 22",
" 9 18 13 17  5",
"19  8  7 25 23",
"20 11 10 24  4",
"14 21 16 12  6",
"",
"14 21 17 24  4",
"10 16 15  9 19",
"18  8 23 26 20",
"22 11 13  6  5",
" 2  0 12  3  7"]
testResult1 = "4512"
testResult2 = "1924"
data = getLines("04input.txt")

print()
testAndVerify(1, str(task1(testData)), testResult1)
print("Task 1, Answer: " + str(task1(data)))
testAndVerify(2, str(task2(testData)), testResult2)
print("Task 2, Answer: " + str(task2(data)))
print()