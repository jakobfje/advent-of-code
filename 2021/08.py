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
    print("Task " + str(taskNr) + ", Test:   " + str(taskResult) + ", " + rightOrWrong)


def task1(data):
    data = [line.split(" | ")[1] for line in data]
    cntPerLen = [0 for i in range(8)]
    
    for line in data:
        for x in line.split(' '):
            cntPerLen[len(x)] += 1
    
    return cntPerLen[2] + cntPerLen[4] + cntPerLen[3] + cntPerLen[7]

    
def task2(data):
    data = [line.split(" | ") for line in data]

    for line in data:
        for x in line[1].split(' '):
            pass

    return "output2"


testData = ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
"edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
"fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
"fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
"aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
"fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
"dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
"bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
"egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
"gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]
testResult1 = 26
testResult2 = ""
data = getLines("08input.txt")

print()
testAndVerify(1, task1(testData), testResult1)
print("Task 1, Answer: " + str(task1(data)))
# testAndVerify(2, str(task2(testData)), testResult2)
# print("Task 2, Answer: " + str(task2(data)))
print()