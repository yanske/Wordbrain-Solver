import itertools

class Grid(object):

    def __init__(self):
        self.grid = []
        self.dim = 0

    def promptDim(self):
        self.dim = int(raw_input("How large is your square?: "))

    def promptRow(self):
        row = []
        for i in range(0, self.dim):
            error = True
            while error:
                print "Entry " + str(i + 1)
                entry = raw_input("")
                if self.isChar(entry):
                    row.append(entry.upper())
                    error = False
                else:
                    print "Error, try again."
        return row

    def isChar(self, input):
        if input.isalpha() and len(input) == 1:
            return True
        return False

    def fillGrid(self):
        for i in range(0, self.dim):
            print "Row " + str(i + 1)
            self.grid.append(self.promptRow())

    def drawRow(self):
        string = ""
        for i in range(0, self.dim):
            string += " ---"
        print string

    def drawCol(self, row):
        string = ""
        for i in range(0, self.dim):
            string += "| "
            string += self.grid[row][i]
            string += " "
        string += "|"
        print string

    def drawGrid(self):
        self.drawRow()
        for i in range(0, self.dim):
            self.drawCol(i)
            self.drawRow()

    def linearList(self):
        lList = []
        for i in range(0, self.dim):
            for j in range(0, self.dim):
                lList.append(self.grid[i][j])
        return lList

    def returnPerms(self, length):
        permList = []
        letters = self.linearList()
        for tuple in itertools.permutations(letters, length):
            permList.append("".join(tuple))
        return permList

    def isBeside(self, origin, letter):
        for i in range(0, self.dim):
            for j in range(0, self.dim):
                if self.grid[i][j] == origin:
                    if not i - 1 < 0:
                        if not j - 1 < 0 and self.grid[i-1][j-1] == letter:
                            return True
                        if self.grid[i-1][j] == letter:
                            return True
                        if not j + 1 >= self.dim and self.grid[i-1][j+1] == letter:
                            return True
                    if not i + 1 >= self.dim:
                        if not j - 1 < 0 and self.grid[i+1][j-1] == letter:
                            return True
                        if self.grid[i+1][j] == letter:
                            return True
                        if not j + 1 >= self.dim and self.grid[i+1][j+1] == letter:
                            return True
                    if not j - 1 < 0 and self.grid[i][j-1] == letter:
                        return True
                    if not j + 1 >= self.dim and self.grid[i][j+1] == letter:
                        return True
        return False

    def wordPossible(self, word):
        for i in range(0, len(word)-1):
            if not self.isBeside(word[i], word[i+1]):
                return False
        return True





