###### Write Your Library Here ###########

from collections import deque
import heapq


#########################################


def search(maze, func):
    return {
        "bfs": bfs,
        "astar": astar,
        "astar_four_circles": astar_four_circles,
        "astar_many_circles": astar_many_circles
    }.get(func)(maze)


# -------------------- Stage 01: One circle - BFS Algorithm ------------------------ #

def bfs(maze):
    """
    [문제 01] 제시된 stage1의 맵 세가지를 BFS Algorithm을 통해 최단 경로를 return하시오.(20점)
    """
    start_point=maze.startPoint()

    path=[]

    ####################### Write Your Code Here ################################

    visited = set()
    path.append([start_point])
    #visited.add((start_point[0], start_point[1]))


    while path:
        current = path.pop(0)
        if(current[-1][0],current[-1][1]) in visited:
            continue
        else :
            visited.add((current[-1][0], current[-1][1]))

        if maze.isObjective(current[-1][0], current[-1][1]):
            print(current)
            return current
        for item in maze.neighborPoints(current[-1][0],current[-1][1]):
            if item not in visited:
                path.append(current + [item])
    

    return current

    ############################################################################



class Node:
    def __init__(self,parent,location):
        self.parent=parent
        self.location=location #현재 노드

        self.obj=[]

        # F = G+H
        self.f=0
        self.g=0
        self.h=0

    def __eq__(self, other):
        return self.location==other.location and str(self.obj)==str(other.obj)

    def __le__(self, other):
        return self.g+self.h<=other.g+other.h

    def __lt__(self, other):
        return self.g+self.h<other.g+other.h

    def __gt__(self, other):
        return self.g+self.h>other.g+other.h

    def __ge__(self, other):
        return self.g+self.h>=other.g+other.h


# -------------------- Stage 01: One circle - A* Algorithm ------------------------ #

def manhatten_dist(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def astar(maze):

    """
    [문제 02] 제시된 stage1의 맵 세가지를 A* Algorithm을 통해 최단경로를 return하시오.(20점)
    (Heuristic Function은 위에서 정의한 manhatten_dist function을 사용할 것.)
    """

    start_point=maze.startPoint()

    end_point=maze.circlePoints()[0]

    path=[]

    ####################### Write Your Code Here ################################


    #내가 다시 써야함 코드 걸린다->list를 heap으로 바꿔보던지 하자

    Nstart = Node(None, start_point)
    Nend = Node(None, end_point)

    openList = []
    closedList = []

    openList.append(Nstart)

    while openList:
        currentNode = openList[0]
        currenidx = 0

        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentidx = index
        

        openList.pop(currentidx)
        closedList.append(currentNode)

        if currentNode == Nend:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        for neighbor in maze.neighbors(currentNode.row, currentNode.col):
            if neighbor in closedList:
                continue

            neighbor.g = currentNode.g +1
            neighbor.h = manhatten_dist(neighbor, Nend)
            neighbor.f = neighbor.g + neighbor.h

            for openNode in openList :
                if neighbor == openNode and neighbor.g > openNode.g:
                    continue

            openList.append(neighbor)
                


















    return path

    ############################################################################


# -------------------- Stage 02: Four circles - A* Algorithm  ------------------------ #



def stage2_heuristic():
    pass


def astar_four_circles(maze):
    """
    [문제 03] 제시된 stage2의 맵 세가지를 A* Algorithm을 통해 최단 경로를 return하시오.(30점)
    (단 Heurstic Function은 위의 stage2_heuristic function을 직접 정의하여 사용해야 한다.)
    """

    end_points=maze.circlePoints()
    end_points.sort()

    path=[]

    ####################### Write Your Code Here ################################


















    return path

    ############################################################################



# -------------------- Stage 03: Many circles - A* Algorithm -------------------- #

def mst(objectives, edges):

    cost_sum=0
    ####################### Write Your Code Here ################################













    return cost_sum

    ############################################################################


def stage3_heuristic():
    pass


def astar_many_circles(maze):
    """
    [문제 04] 제시된 stage3의 맵 세가지를 A* Algorithm을 통해 최단 경로를 return하시오.(30점)
    (단 Heurstic Function은 위의 stage3_heuristic function을 직접 정의하여 사용해야 하고, minimum spanning tree
    알고리즘을 활용한 heuristic function이어야 한다.)
    """

    end_points= maze.circlePoints()
    end_points.sort()

    path=[]

    ####################### Write Your Code Here ################################





















    return path

    ############################################################################
