from pprint import pprint
import re
import queue

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


def matching(char, last_char):
    if ((last_char == '(' and char == ')') or
        (last_char == '[' and char == ']') or 
        (last_char == '{' and char == '}') or
        (last_char == '<' and char == '>')):
        return True
    else:
        return False


def task1(data):
    faulty_chars = []
    lifo = queue.LifoQueue()
    for line in data:
        for char in line:
            if char in '({[<':
                lifo.put(char)
            elif char in ')}]>':
                last_char = lifo.get()
                if not matching(char, last_char):
                    faulty_chars.append(char)
                    break
    
    score = sum(3 for x in faulty_chars if x == ')')
    score += sum(57 for x in faulty_chars if x == ']')
    score += sum(1197 for x in faulty_chars if x == '}')
    score += sum(25137 for x in faulty_chars if x == '>')
    return score


def task2(data):
    scores = []
    for line in data:
        corrupt = False
        lifo = queue.LifoQueue()
        for char in line:
            if char in '({[<':
                lifo.put(char)
            elif char in ')}]>':
                last_char = lifo.get()
                if not matching(char, last_char):
                    corrupt = True
                    break
        
        if not corrupt:
            score = 0
            while not lifo.empty():
                char = lifo.get()
                score *= 5
                if char == '(':
                    score += 1
                elif char == '[':
                    score += 2
                elif char == '{':
                    score += 3
                elif char == '<':
                    score += 4
            scores.append(score)

    scores.sort()
    return scores[int(len(scores)/2)]


testData = ["[({(<(())[]>[[{[]{<()<>>",
"[(()[<>])]({[<{<<[]>>(",
"{([(<{}[<>[]}>{[]{[(<()>",
"(((({<>}<{<{<>}{[]{[]{}",
"[[<[([]))<([[{}[[()]]]",
"[{[{({}]{}}([{[{{{}}([]",
"{<[[]]>}<{[{[{[]{()[[[]",
"[<(<(<(<{}))><([]([]()",
"<{([([[(<>()){}]>(<<{{",
"<{([{{}}[<[[[<>{}]]]>[]]"]
testResult1 = 26397
testResult2 = 288957
data = getLines("10input.txt")

print()
testAndVerify(1, task1(testData), testResult1)
print("Task 1, Answer: " + str(task1(data)))
testAndVerify(2, task2(testData), testResult2)
print("Task 2, Answer: " + str(task2(data)))
print()