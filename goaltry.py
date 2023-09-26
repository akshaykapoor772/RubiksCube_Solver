import random
import sys

MOVES = {
    "U": [2, 0, 3, 1, 20, 21, 6, 7, 4, 5, 10, 11, 12, 13, 14, 15, 8, 9, 18, 19, 16, 17, 22, 23],
    "U'": [1, 3, 0, 2, 8, 9, 6, 7, 16, 17, 10, 11, 12, 13, 14, 15, 20, 21, 18, 19, 4, 5, 22, 23],
    "R": [0, 9, 2, 11, 6, 4, 7, 5, 8, 13, 10, 15, 12, 22, 14, 20, 16, 17, 18, 19, 3, 21, 1, 23],
    "R'": [0, 22, 2, 20, 5, 7, 4, 6, 8, 1, 10, 3, 12, 9, 14, 11, 16, 17, 18, 19, 15, 21, 13, 23],
    "F": [0, 1, 19, 17, 2, 5, 3, 7, 10, 8, 11, 9, 6, 4, 14, 15, 16, 12, 18, 13, 20, 21, 22, 23],
    "F'": [0, 1, 4, 6, 13, 5, 12, 7, 9, 11, 8, 10, 17, 19, 14, 15, 16, 3, 18, 2, 20, 21, 22, 23],
    "D": [0, 1, 2, 3, 4, 5, 10, 11, 8, 9, 18, 19, 14, 12, 15, 13, 16, 17, 22, 23, 20, 21, 6, 7],
    "D'": [0, 1, 2, 3, 4, 5, 22, 23, 8, 9, 6, 7, 13, 15, 12, 14, 16, 17, 10, 11, 20, 21, 18, 19],
    "L": [23, 1, 21, 3, 4, 5, 6, 7, 0, 9, 2, 11, 8, 13, 10, 15, 18, 16, 19, 17, 20, 14, 22, 12],
    "L'": [8, 1, 10, 3, 4, 5, 6, 7, 12, 9, 14, 11, 23, 13, 21, 15, 17, 19, 16, 18, 20, 2, 22, 0],
    "B": [5, 7, 2, 3, 4, 15, 6, 14, 8, 9, 10, 11, 12, 13, 16, 18, 1, 17, 0, 19, 22, 20, 23, 21],
    "B'": [18, 16, 2, 3, 4, 0, 6, 1, 8, 9, 10, 11, 12, 13, 7, 5, 14, 17, 15, 19, 21, 23, 20, 22],
}

allowedColors = {'W', 'Y', 'R', 'G', 'B', 'O'}
inversecolor = {
    "W": "Y",
    "Y": "W",
    "R": "O",
    "O": "R",
    "B": "G",
    "G": "B",
}
inversemove = {
    "F":"F'",
    "U":"U'",
    "R":"R'",
    "D":"D'",
    "L":"L'",
    "B":"B'",
    "F'":"F",
    "U'":"U",
    "R'":"R",
    "D'":"D",
    "L'":"L",
    "B'":"B",
}
complementarymove = {
    "U":"D'",
    "D'":"U",
    "U'":"D",
    "D":"U'",
    "L'":"R",
    "R":"L'",
    "L":"R'",
    "R'":"L",
    "F":"B'",
    "B'":"F",
    "F'":"B",
    "B":"F'",
}
'''
sticker indices:

      0  1
      2  3
16 17  8  9   4  5  20 21
18 19  10 11  6  7  22 23
      12 13
      14 15

face colors:

    0
  4 2 1 5
    3

moves:
[ U , U', R , R', F , F', D , D', L , L', B , B']
'''


class cube:
    Solvedstate = ["W", "W", "W", "W", "R", "R", "R", "R", "G", "G", "G", "G", "Y", "Y", "Y", "Y", "O", "O", "O",
                   "O", "B", "B", "B", "B"]

    def __init__(self, String="WWWW RRRR GGGG YYYY OOOO BBBB"):
        self.default = []
        for ele in String:
            if ele.strip():
                self.default.append(ele)


    def normalize(self):
        newCube = {}
        newCube[self.default[10]] = 'G'
        newCube[self.default[12]] = 'Y'
        newCube[self.default[19]] = 'O'
        newCube[inversecolor[self.default[10]]] = inversecolor['G']
        newCube[inversecolor[self.default[12]]] = inversecolor['Y']
        newCube[inversecolor[self.default[19]]] = inversecolor['O']
        for i in range(len(self.default)):
            self.default[i] = newCube[self.default[i]]

    def equals(self, cube):

        return

    def clone(self):
        c = cube()
        c.default = self.default
        return c

    def print(self):
            print("\n")
            print("     " + self.default[0] + " " + self.default[1])
            print("     " + self.default[2] + " " + self.default[3])
            print(self.default[16] + " " + self.default[17] + "  " + self.default[8] + " " + self.default[9] + "  " + self.default[4] + " " + self.default[5] + "  " + self.default[20] + " " + self.default[21])
            print(self.default[18] + " " + self.default[19] + "  " + self.default[10] + " " + self.default[11] + "  " + self.default[6] + " " + self.default[7] + "  " + self.default[22] + " " + self.default[23])
            print("     " + self.default[12] + " " + self.default[13])
            print("     " + self.default[14] + " " + self.default[15])

    def applyMove(self, move):
        if MOVES[move] == None:
            print("Please input a valid move")
            sys.exit(0)
        newCube = []
        moveCube = MOVES[move]
        for i in range(len(moveCube)):
            newCube.append(self.default[moveCube[i]])
        self.default = newCube
        print()
        self.print()
        #print()

    def applyMoverand(self, move):
        if MOVES[move] == None:
            print("Please input a valid move")
            sys.exit(0)
        newCube = []
        moveCube = MOVES[move]
        for i in range(len(moveCube)):
            newCube.append(self.default[moveCube[i]])
        self.default = newCube

    def applyMovesStrrand(self, strmoves):
        runtimecube = self.clone()
        movecommands = strmoves.split(" ")
        for i in movecommands:
            runtimecube.applyMoverand(i)
        return runtimecube

    def applyMovesStr(self, strmoves):
        runtimecube = self.clone()
        movecommands = strmoves.split(" ")
        for i in movecommands:
            runtimecube.applyMove(i)
        return runtimecube

    def isgoal(self):
        for i in range(0, 16, 4):
            if not (self.default[i] == self.default[i + 1] == self.default[i + 2] == self.default[i + 3]):
                return False
        return True

    ''''
    def print(self):

        print(sep="\t", end="\t\t  ")
        print(*self.default[0:2], sep="  ")
        print(sep="\t", end="\t\t  ")
        print(*self.default[2:4], sep="  ")
        print(*self.default[16:18], sep=" ", end='\t\t  ')
        print(*self.default[8:10], sep=" ", end='\t ')
        print(*self.default[4:6], sep=" ", end='\t ')
        print(*self.default[20:22], sep=" ")
        print(*self.default[18:20], sep=" ", end='\t\t  ')
        print(*self.default[10:12], sep=" ", end='\t ')
        print(*self.default[6:8], sep=" ", end='\t ')
        print(*self.default[22:24], sep=" ")
        print(sep="\t", end="\t\t  ")
        print(*self.default[12:14], sep="  ")
        print(sep="\t", end="\t\t  ")
        print(*self.default[14:16], sep="  ")
    '''''

    def identify(self, Inputlist="WWWW RRRR GGGG YYYY OOOO BBBB"):
        self.default = []
        for ele in Inputlist:
            if ele.strip():
                self.default.append(ele)
        Solvedstate = ["W", "W", "W", "W", "R", "R", "R", "R", "G", "G", "G", "G", "Y", "Y", "Y", "Y", "O", "O", "O",
                       "O", "B", "B", "B", "B"]

        for x, y in zip(self.default, Solvedstate):
            a = 0
            b = 0
            if x != y:
                a = a + 1
            else:
                b = b + 1
        if a > 0:
            print("False")
        else:
            print("True")

    def statecomp(self, Inputlist1, Inputlist2):
        self.default1 = []
        self.default2 = []
        for ele in Inputlist1:
            if ele.strip():
                self.default1.append(ele)
        print(*self.default1, sep=" ")

        for ele in Inputlist2:
            if ele.strip():
                self.default2.append(ele)
        print(*self.default2, sep=" ")

        for x, y in zip(self.default1, self.default2):
            a = 0
            b = 0
            if x != y:
                a = a + 1
            else:
                b = b + 1
        if a > 0:
            print("False")
        else:
            print("True")

    def shuffle(self, n):
        listofmoves = []
        moves = ["U", "U'", "R", "R'", "F", "F'", "D", "D'", "L", "L'", "B", "B'"]
        for i in range(n):
            randmove = random.choice(moves)
            listofmoves.append(randmove)
            # self.normalize()
        print(*listofmoves, sep=" ")
        applyMovesshuf2(" ".join(listofmoves), self)


def defcube(state="WWWW RRRR GGGG YYYY OOOO BBBB"):
    c = cube(state)
    c.printnew()


def applyMove(moves, c="WWWW RRRR GGGG YYYY OOOO BBBB"):
    a = cube(c)
    newCube = a.applyMovesStrrand(moves)
    newCube.print()
    print()
    return newCube


def applyMovesshuf2(moves, c):
    newCube = c.applyMovesStrrand(moves)
    print()
    newCube.print()
    return newCube


def applyMovesshuf(moves, c):
    newCube = c.applyMovesStrrand(moves)
    newCube.print()
    return newCube


def applymoveforrandom(moves, c):
    newCube = c.applyMovesStrrand(moves)


def goal(String):
    c = cube(String)
    print(c.identify(String))


def randomwalk(moves, n):
    c = cube()
    newCube = applyMovesshuf(moves, c)
    newCube.shuffle(n)
    '''''
    goal = False
    if newCube.goal():
        return []
    movesnumber= 0
    #listofmoves = c.shuffle(n)
    #print(*listofmoves, sep=" ")
    #newmovelist= []
    while movesnumber<n:
        newCube.shuffle(1)
        #newmovelist = c.shuffle(listofmoves)
        #print(newmovelist)
        movesnumber+=1
        if newCube.goal():
            goal = True
            break
    '''''


def norm(state):
    a = cube(state)
    a.normalize()
    a.print()


''''
def main():
    c = cube()
    nargs = len(sys.argv)
    if sys.argv[1] == "print":
        if nargs == 3:
            defcube(sys.argv[2])
        else:
            defcube()
    elif sys.argv[1] == "goal":
        if nargs == 3:
            goal(sys.argv[2])
        else:
            printError("Missing an argument")
    elif sys.argv[1] == "applyMovesStr":
        if nargs == 4:
            applyMove(sys.argv[2], sys.argv[3])
        elif nargs == 3:
            applyMove(sys.argv[2])
        else:
            printError("Missing an argument")
    elif sys.argv[1] == "norm":
        if nargs == 3:
            norm(sys.argv[2])
        else:
            printError("Missing an argument")
    elif sys.argv[1] == "shuffle":
        if nargs == 3:
            c.shuffle(int(sys.argv[2]))
        else:
            printError("Missing an argument")
    elif sys.argv[1] == "random":
        if nargs == 3:
            randomwalk(sys.argv[2])
        else:
            printError("Missing an argument")
    else:
        printError("Invalid Command")
'''''


def printError(errStr):
    print(errStr)
    sys.exit(0)


if __name__ == "__main__":
    main()
