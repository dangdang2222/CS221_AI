###### Write Your Library Here ###########
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

    openList=[]
    closedList = []


    heapq.heappush(openList, (manhatten_dist(start_point, end_point),[start_point]))

    while openList:
        path = heapq.heappop(openList)[1]
        currentpoint = path[-1]
        #print(currentpoint)
        if currentpoint in closedList:
            continue
        closedList.append(currentpoint)
        #print(closedList)
        if currentpoint == end_point:
            return path
        neighbors = maze.neighborPoints(currentpoint[0], currentpoint[1])
        for neighbor in neighbors:
            if neighbor in closedList:
                continue
            temp_g = len(path)
            temp_h = manhatten_dist(neighbor,end_point)
            temp_f = temp_g+temp_h
            
            temp = path.copy()
            temp.append(neighbor)
            heapq.heappush(openList,(temp_f,temp))
            #print(openList)
    return path
    ############################################################################


# -------------------- Stage 02: Four circles - A* Algorithm  ------------------------ #



def stage2_heuristic():
    pass


def astar_four_circles(maze):
    end_points=maze.circlePoints()
    end_points.sort()

    path=[]

    ####################### Write Your Code Here ################################

    
    """start_point=maze.startPoint()
    end_points=maze.circlePoints()

    def astar_four_length(start_point, end_point):
        openList=[]
        closedList = []
        heapq.heappush(openList, (manhatten_dist(start_point, end_point),[start_point]))

        while openList:
            path = heapq.heappop(openList)[1]
            #print(path)
            currentpoint = path[-1]
            #print(currentpoint)
            if currentpoint in closedList:
                continue
            closedList.append(currentpoint)
            #print(closedList)
            if currentpoint == end_point:
                #print(path)
                return len(path)
            neighbors = maze.neighborPoints(currentpoint[0], currentpoint[1])
            for neighbor in neighbors:
                if neighbor in closedList:
                    continue
                temp_g = len(path)
                temp_h = manhatten_dist(neighbor,end_point)
                temp_f = temp_g+temp_h
                
                temp = path.copy()
                temp.append(neighbor)
                heapq.heappush(openList,(temp_f,temp))
                #print(openList)
        return len(path)



    
                ##너무 오래걸려 그냥 다 치우고 f만 게산해서 그 최솟값 경로로 가는ㄴ걸 찾아봐
    def astar_four_path(start_point, end_point):
        openList=[]
        closedList = []
        heapq.heappush(openList, (manhatten_dist(start_point, end_point),[start_point]))

        while openList:
            path = heapq.heappop(openList)[1]
            currentpoint = path[-1]
            #print(currentpoint)
            if currentpoint in closedList:
                continue
            closedList.append(currentpoint)
            #print(closedList)
            if currentpoint == end_point:
                return path
            neighbors = maze.neighborPoints(currentpoint[0], currentpoint[1])
            for neighbor in neighbors:
                if neighbor in closedList:
                    continue
                temp_g = len(path)
                temp_h = manhatten_dist(neighbor,end_point)
                temp_f = temp_g+temp_h
                
                temp = path.copy()
                temp.append(neighbor)
                heapq.heappush(openList,(temp_f,temp))
                #print(openList)
        return path

    startedges=[] #startpoint->circle
    myedges=[] #circle->circle

    for item in end_points:
        startedges.append((astar_four_length(start_point,item),start_point,item))
    i=0
    j=0
    #print(startedges)
    while i< len(end_points):
        j=0
        while j<len(end_points):
            if i!=j:
                myedges.append((astar_four_length(end_points[i],end_points[j]),end_points[i],end_points[j]))
            else:
                myedges.append((0,end_points[i],end_points[j]))
            j=j+1
        i=i+1
    #print(myedges)
    
    #길이만 저장함 일단
        
    sub_path_length=[]
    j=0
    t=0
    y=0
    g=0
    h=0
    index = 0
    while t<len(end_points):
        y=0
        while y<len(end_points):
            g=0
            if(y!=t):
                while g<len(end_points):
                    h=0
                    if(g!=t and g!=y):
                        while(h<len(end_points)):
                            if(h!=t and h!=y and h!= g):
                               sub_path_length.append((startedges[t][0]+myedges[t*4+y][0]+myedges[y*4+g][0]+myedges[g*4+h][0],t,y,g,h))
                            h=h+1
                    g=g+1
            y=y+1
        t=t+1

    mini = min(sub_path_length)
    #print(mini)
    mini_index = sub_path_length.index(mini)
    length,tt,yy,gg,hh = sub_path_length[mini_index]

    #print(length, tt,yy,gg,hh)



    path = astar_four_path(start_point,end_points[tt])
    path.pop()
    path=path+astar_four_path(end_points[tt],end_points[yy])
    path.pop()
    path=path+astar_four_path(end_points[yy],end_points[gg])
    path.pop()
    path=path+astar_four_path(end_points[gg],end_points[hh])
    
    return path"""
    start_point=maze.startPoint()
    def astar_four_length(start_point, end_point):
        openList=[]
        closedList = []
        heapq.heappush(openList, (manhatten_dist(start_point, end_point),[start_point]))

        while openList:
            path = heapq.heappop(openList)[1]
            currentpoint = path[-1]
            if currentpoint in closedList:
                continue
            closedList.append(currentpoint)
            if currentpoint == end_point:
                return len(path)
            neighbors = maze.neighborPoints(currentpoint[0], currentpoint[1])
            for neighbor in neighbors:
                if neighbor in closedList:
                    continue
                temp_g = len(path)
                temp_h = manhatten_dist(neighbor,end_point)
                temp_f = temp_g+temp_h
                
                temp = path.copy()
                temp.append(neighbor)
                heapq.heappush(openList,(temp_f,temp))
        return len(path)



    
                ##너무 오래걸려 그냥 다 치우고 f만 게산해서 그 최솟값 경로로 가는ㄴ걸 찾아봐
    def astar_four_path(start_point, end_point):
        openList=[]
        closedList = []
        heapq.heappush(openList, (manhatten_dist(start_point, end_point),[start_point]))

        while openList:
            path = heapq.heappop(openList)[1]
            currentpoint = path[-1]
            #print(currentpoint)
            if currentpoint in closedList:
                continue
            closedList.append(currentpoint)
            #print(closedList)
            if currentpoint == end_point:
                return path
            neighbors = maze.neighborPoints(currentpoint[0], currentpoint[1])
            for neighbor in neighbors:
                if neighbor in closedList:
                    continue
                temp_g = len(path)
                temp_h = manhatten_dist(neighbor,end_point)
                temp_f = temp_g+temp_h
                
                temp = path.copy()
                temp.append(neighbor)
                heapq.heappush(openList,(temp_f,temp))
                #print(openList)
        return path

    startedges=[] 
    for item in end_points:
        startedges.append((astar_four_length(start_point,item),start_point,item))
    i=0
    j=0


    startedges.sort(reverse=True)
    def astar_four_get_neighbors(start_point, end_point,end_points,path):
        if len(path)==4:
            return (end_point)
        else:
            temp = []
            temp = end_points.copy()
            if(start_point in end_points):
                temp.remove(start_point)
            temp.remove(end_point)
            

            for item in temp:
                if item in path:
                    temp.remove(item)


            return temp

    def astar_four_big_length(start_point, end_point,end_points):
        openList=[]
        closedList = []

        first = 0
        second = manhatten_dist(start_point, end_point)
        heapq.heappush(openList, (first+second,first,second,[start_point]))


        while openList:
            info = heapq.heappop(openList)
            prev_f = info[0]
            prev_h = info[1]
            prev_g = info[2]
            path =info[3]
            currentpoint = path[-1]
            if currentpoint in closedList:
                continue

            if len(path) == 5:
                return prev_f,path
            
            neighbors = astar_four_get_neighbors(currentpoint, end_point,end_points,path)

            for neighbor in neighbors:
                if isinstance(neighbor, int)==True:
                    neighbor = neighbors
                temp_g = prev_h+astar_four_length(currentpoint,neighbor)-1
                temp_h = manhatten_dist(neighbor,end_point)
                temp_f = temp_g+temp_h

 
                temp = path.copy()
                temp.append(neighbor)

                heapq.heappush(openList,(temp_f,temp_g,temp_h,temp))
        return len(path)

    total_length=[]
    for item in startedges:
        total_length.append(astar_four_big_length(start_point, item[2],end_points))
    
    mini = min(total_length)

    path = astar_four_path(start_point,mini[1][1])
    path.pop()
    path = path+astar_four_path(mini[1][1],mini[1][2])
    path.pop()
    path = path+astar_four_path(mini[1][2],mini[1][3])
    path.pop()
    path = path+astar_four_path(mini[1][3],mini[1][4])

    return path
        
    
    ############################################################################




# -------------------- Stage 03: Many circles - A* Algorithm -------------------- #

def mst(maze,start_point,objectives, vertices, edges,start_edges):
    

    cost_sum=0
    ####################### Write Your Code Here ################################
    
    
    start_point=maze.startPoint()
    end_points=maze.circlePoints()


    check = []
    for item in vertices:
        check.append(item)
        check.append(item)
    #print(check)
    visited = []
    mst=[]
    eedges = []
    edges.sort()

    while check:
        #print(edges)
        f, n1, n2  = edges[0]
        
        """if n1 in visited and n2 in visited:
            del edges[edges.index((f,n1,n2))]
            del edges[edges.index((f,n2,n1))]

            continue"""
        if n1 != n2:
            start = n1
            second = n1
            while 1:
                cccheck=0
                for item in eedges:
                    if item[1]==start and item[2]!=second:
                        cccheck=1
                        second = start
                        start=item[2]
                        break

                if cccheck==0:
                    break
            #print(cccheck, start,n1,n2)
            if n2 == start:
                #print("here")
                del edges[edges.index((f,n1,n2))]
                del edges[edges.index((f,n2,n1))]
                continue
        #print("where")
        if(n1!=n2):
            eedges.append((f,n1,n2))
            eedges.append((f,n2,n1))
        #print(eedges)
        #print(f,n1,n2)
        del edges[edges.index((f,n1,n2))]
        if(n1!=n2):
            del edges[edges.index((f,n2,n1))]
        #print(len(edges))

        if(n1!=n2):
            visited.append(n1)
            visited.append(n2)
        #print(visited)
        if(n1!=n2):
            check.remove(n1)
            check.remove(n2)
        #print(check)
 
    
        for aa in visited:
            cnt = visited.count(aa)
            if cnt==2:
                for edge in edges:
                    ff,nn1,nn2=edge
                    if nn1 == aa or nn2 == aa:
                        del edges[edges.index((ff,nn1,nn2))]
                        del edges[edges.index((ff,nn2,nn1))]
        

        if len(check)==2:
            if check[0]!=check[1]:
                break
        #print(len(edges))


    fff,nnn1,nnn2 = edges[0]

    for item in start_edges:
        if item[2] == nnn1:
            fff1=item[0]
        if item[2] == nnn2:
            fff2=item[0]

    if fff1<fff2:
        return nnn1,eedges
    else:
        return nnn2,eedges        

    return nnn1,nnn2,eedges

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
    start_point=maze.startPoint()
    

    def astar_many_length(start_point, end_point):
        openList=[]
        closedList = []
        heapq.heappush(openList, (manhatten_dist(start_point, end_point),[start_point]))

        while openList:
            path = heapq.heappop(openList)[1]
            #print(path)
            currentpoint = path[-1]
            #print(currentpoint)
            if currentpoint in closedList:
                continue
            closedList.append(currentpoint)
            #print(closedList)
            if currentpoint == end_point:
                #print(path)
                return len(path)
            neighbors = maze.neighborPoints(currentpoint[0], currentpoint[1])
            for neighbor in neighbors:
                if neighbor in closedList:
                    continue
                temp_g = len(path)
                temp_h = manhatten_dist(neighbor,end_point)
                temp_f = temp_g+temp_h
                
                temp = path.copy()
                temp.append(neighbor)
                heapq.heappush(openList,(temp_f,temp))
                #print(openList)
        return len(path)



    
                ##너무 오래걸려 그냥 다 치우고 f만 게산해서 그 최솟값 경로로 가는ㄴ걸 찾아봐
    def astar_many_path(start_point, end_point):
        openList=[]
        closedList = []
        heapq.heappush(openList, (manhatten_dist(start_point, end_point),[start_point]))

        while openList:
            path = heapq.heappop(openList)[1]
            currentpoint = path[-1]
            #print(currentpoint)
            if currentpoint in closedList:
                continue
            closedList.append(currentpoint)
            #print(closedList)
            if currentpoint == end_point:
                return path
            neighbors = maze.neighborPoints(currentpoint[0], currentpoint[1])
            for neighbor in neighbors:
                if neighbor in closedList:
                    continue
                temp_g = len(path)
                temp_h = manhatten_dist(neighbor,end_point)
                temp_f = temp_g+temp_h
                
                temp = path.copy()
                temp.append(neighbor)
                heapq.heappush(openList,(temp_f,temp))
                #print(openList)
        return path

    vertices = []
    start_edges = []
    myedges = []
    
    #vertices.append(start_point)
    for item in end_points:
        vertices.append(item)
        start_edges.append((astar_many_length(start_point,item),start_point,item))
    
    i=0
    j=0

    while i< len(end_points):
        j=0
        while j<len(end_points):
            if i!=j:
                myedges.append((astar_many_length(end_points[i],end_points[j]),end_points[i],end_points[j]))
            else:
                myedges.append((0,end_points[i],end_points[j]))
            j=j+1
        i=i+1

    
    #print(myedges)

    first_circle, eedges = mst(maze,start_point,end_points, vertices, myedges,start_edges)
    
    
    path = astar_many_path(start_point,first_circle)
    path.pop()
    
    #print(eedges)
    #print(first_circle)
    start = first_circle
    while(eedges):
        for item in eedges:
            #print(item)
            if item[1]==start:
                path=path+astar_many_path(item[1],item[2])
                path.pop()
                del eedges[eedges.index((item[0],item[1],item[2]))]
                del eedges[eedges.index((item[0],item[2],item[1]))]
                start=item[2]
                #print(path)

    path.append(start)

    #print(path)
    return path

    #########################   ###################################################
