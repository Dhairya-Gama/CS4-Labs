import sys
import math

lines = sys.stdin.readlines()

line = lines[0]


lineList=[i for i in line]


answer = ""

vowels = ["a", "e", "i", "o", "u"]

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def isEven(x):
    return x % 2 == 0


for i in range(len(lineList)):

    if isPrime(i):
        if lineList[i] in consonants:
            temp = consonants.index(lineList[i])

            if temp == 20:
                temp = 0
            else:
                temp += 1
            lineList[i] = consonants[temp]





    if isEven(i):
        if lineList[i] in vowels:
            temp2 = lineList[i].swapcase()
            lineList[i] = temp2


    if not(isEven(i)):
        if lineList[i] in consonants:
            if lineList[i] == line[i]:
                lineList[i] = "*"



for a in range(len(lineList)):
    answer += lineList[a]

answer = answer.replace(" ", "")

print(answer)
    