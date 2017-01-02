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
    #if a word and if word possible by game rules
    if perm+"\n" in words and newGrid.wordPossible(perm):
        wordsPerm.append(perm)

print wordsPerm







