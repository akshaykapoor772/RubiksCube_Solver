import queue
import random
import sys
import time
import goaltry
from goaltry import cube
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
    "B'":"B"
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
    "B":"F'"
}

sides = [(3,9,4),(6,11,13),(1,5,20),(15,7,22),(2,8,17),(19,10,12),(0,16,21),(18,14,23)]
sidesprint = [(0,0,1),(0,1,1),(1,0,1),(1,1,1),(0,0,0),(0,1,0),(1,0,0),(1,1,0)]
sidecolored = [{'W','G','R'},{'R','G','Y'},{'W','R','B'},{'Y','R','B'},{'W','G','O'},{'O','G','Y'},{'W','O','B'},{'O','Y','B'}]

class cubesolver:
    c = cube
    Solvedstate = ["W", "W", "W", "W", "R", "R", "R", "R", "G", "G", "G", "G", "Y", "Y", "Y", "Y", "O", "O", "O",
                   "O", "B", "B", "B", "B"]

    def bfsgoalstate (self, initialstate, goal):
        goalCube = initialstate.clone()
        for moves in goal:
            goalCube.applyMove(moves)



    def bfs (self, moves, b= "WWWW RRRR GGGG YYYY OOOO BBBB"):

        start = time.time()
        a = cubesolver()
        d = goaltry
        c = cube(b)
        initialstate = c.applyMovesStrrand(moves)
        initialstate.print()
        initialstate.normalize()
        node = initialstate
        visited = set()
        unvisited = [node.default]
        movesapplied = [[]]
        isGoal = False
        while isGoal is False:
            workingcube = cube()
            workingcube.default = unvisited.pop(0)
            workingcubeMoves = movesapplied.pop(0)
            moveslist = list(goaltry.MOVES.keys())
            moveslist2 = random.choices(moveslist, weights=None, k=5)
            allowedmoves = self.allowedmoves(" ".join(moveslist2))
            for moves in allowedmoves:
                anotherCube = workingcube.clone()
                anotherCube.applyMoverand(moves)
                anotherCube.normalize()
                if anotherCube.isgoal():
                    end = time.time()
                    isGoal = True
                    goal = workingcubeMoves+ [moves]
                    print(" ".join(goal))
                    initialstate.print()
                    self.bfsgoalstate(initialstate, goal)
                    print(len(visited))
                    print(end-start)
                    break
                elif not anotherCube in visited:
                    unvisited.append(anotherCube.default)
                    movesapplied.append(workingcubeMoves+[moves])
            workingcube.normalize()
            visited.add(workingcube)

    def ids (self, moves, b= "WWWW RRRR GGGG YYYY OOOO BBBB"):
        start = time.time()
        a = cubesolver()
        d = goaltry
        c = cube(b)
        initialstate = c.applyMovesStrrand(moves)
        initialstate.print()
        initialstate.normalize()
        node = initialstate
        node.normalize()
        sumofvisited = 0
        depth = 0
        depthdict = {}
        isGoal = False
        while not isGoal:
            unvisited = [node.default]
            nodesVisitedDepth = 0
            visited = set()
            movesApplied = [[]]
            unvisitedDepth = [0]
            while len(unvisited)>0:
                workingCube = cube()
                workingCube.default = unvisited.pop()
                workingCubeMoves = movesApplied.pop()
                workingCubeDepth = unvisitedDepth.pop()
                if workingCubeDepth is depth:
                    nodesVisitedDepth+=1
                    moveslist = list(goaltry.MOVES.keys())
                    moveslist2 = random.choices(moveslist, weights=None, k=6)
                    allowedmoves = self.allowedmoves(" ".join(moveslist2))
                for moves in allowedmoves:
                    workingCube2 = workingCube.clone()
                    workingCube2.applyMoverand(moves)
                    workingCube2Moves = workingCubeMoves+ [moves]
                    workingCube2Depth = workingCubeDepth+1
                    if workingCube2.isgoal():
                        sumofvisited =len(visited)+sumofvisited
                        depthdict[depth]= len(visited)
                        clues = list(depthdict.keys())
                        clues.sort()
                        for clue in clues:
                            a = clue
                            print("Depth", clue,"d:", depthdict[clue])
                        end = time.time()
                        print("IDS found a solution at depth", a)
                        print(" ".join(workingCube2Moves))
                        initialstate.print()
                        self.bfsgoalstate(node, workingCube2Moves)
                        print(sumofvisited)
                        print(end-start)
                        break
                    elif not workingCube2 in visited:
                        workingCube2.normalize()
                        if workingCube2Depth<=depth:
                            unvisited.append(workingCube2.default)
                            movesApplied.append(workingCube2Moves)
                            unvisitedDepth.append(workingCube2Depth)
                if workingCube2.isgoal():
                    isGoal = True
                    break
            workingCube.normalize()
            visited.add(workingCube)
            depthdict[depth]=nodesVisitedDepth
            sumofvisited+=nodesVisitedDepth
            depth+=1

    def astar(self, moves, b= "WWWW RRRR GGGG YYYY OOOO BBBB"):
        start = time.time()
        a = cubesolver()
        d = goaltry
        c = cube(b)
        initialstate = c.applyMovesStrrand(moves)
        initialstate.print()
        initialstate.normalize()
        isgoal = False
        unvisited = queue.PriorityQueue()
        unvisited.put((self.goalheuristic(initialstate), initialstate.default, []))
        movesApplied = [[]]
        visited = set()
        while isgoal is False:
            queue2 = unvisited.get()
            moveslist = list(goaltry.MOVES.keys())
            moveslist2 = random.choices(moveslist, weights=None, k=6)
            workingCube = cube()
            temp = 1
            workingCube.default = queue2[temp]
            workingCubeMoves = queue2[temp+1]
            allowedmoves = self.allowedmoves(" ".join(moveslist2))
            for item in allowedmoves:
                workingCube2 = workingCube.clone()
                workingCube2.applyMoverand(item)
                workingCube2Moves = workingCubeMoves+[item]
                workingCube2.normalize()
                if workingCube2.isgoal():
                    isgoal = True
                    end= time.time()
                    print(" ".join(workingCube2Moves))
                    initialstate.print()
                    self.bfsgoalstate(initialstate, workingCube2Moves)
                    print(len(visited))
                    print(end - start)
                    break
                elif not workingCube2 in visited:
                    unvisited.put((len(workingCube2Moves)+self.goalheuristic(workingCube2), workingCube2.default, workingCube2Moves))
            workingCube.normalize()
            visited.add(workingCube)


    def manhattanDistance(self, a, b):
        return sum(abs(val1-val2) for val1,val2 in zip(a,b))

    def goalheuristic(self, state):
        workCube = cube()
        workCube.normalize()
        state.normalize()
        result = 0
        finalresult = result/4
        for i in range(len(sides)):
            side = sides[i]
            sidecolor = {state.default[side[0]],state.default[side[1]], state.default[side[2]]}
            position = sidecolored.index(sidecolor)
            result = result+self.manhattanDistance(sidesprint[i],sidesprint[position])
        return finalresult


    def allowedmoves (self, previousmove):
        listofmoves = previousmove.split(" ")
        allowedmoves = []
        for item in listofmoves:
            allowedmoves.append(item)
            if len(allowedmoves)>1 and allowedmoves[-2] is inversemove[item]:
                allowedmoves.remove(inversemove[allowedmoves[-1]])
            elif len(allowedmoves)>1 and allowedmoves[-2] is complementarymove[item]:
                allowedmoves.remove(complementarymove[allowedmoves[-1]])
            elif len(allowedmoves)>=3 and allowedmoves[-1] is allowedmoves[-2]:
                allowedmoves.remove(item)
            else:
                allowedmoves.append(item)
                allowedmoves.remove(item)
        return allowedmoves


'''''
def main():
    c = cubesolver()
    c.ids("L D' R' F R D'")
    #c.allowedmoves2("L D' R' F R D'")

'''''
def main():
    goal = cubesolver()
    c = cube()
    narg=len(sys.argv)
    if narg == 3:
        if sys.argv[1] == "bfs":
            goal.bfs(sys.argv[2])
        elif sys.argv[1] == "ids":
            goal.ids(sys.argv[2])
        elif sys.argv[1] == "astar":
            goal.astar(sys.argv[2])
        else:
            print("Please enter a valid command")



if __name__ == '__main__':
    main()



