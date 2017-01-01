"""
WordBrain Solver
January 1st, 2017
Yan Ke
"""

from grid import Grid

#initalization
newGrid = Grid()
newGrid.promptDim()
newGrid.fillGrid()
newGrid.drawGrid()

#stores potential words as a list
with open('dictionary.txt', 'r') as wordList:
    words = list(wordList)

wordSizes = []
wordSizes.append(int(raw_input("What is the first word size: ")))

letterPerms = newGrid.returnPerms(wordSizes[0])
wordsPerm = []
for perm in letterPerms:
    if perm+"\n" in words:
        wordsPerm.append(perm)

potentialWords = []

#filter out inaccessible words
for word in wordsPerm:
    if newGrid.wordPossible(word):
        potentialWords.append(word)

print potentialWords







