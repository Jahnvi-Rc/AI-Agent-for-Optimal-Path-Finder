#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 17:25:02 2019

@author: jahnvirc
"""

def convert_to_list(string): 
    li = list(string.split(" ")) 
    return li 
import queue
def convert(list): 
    return tuple(list)
def convert_string(s): 
    str1 = "" 
    return(str1.join(s)) 

fp = open(r"input_UCS_3.txt","r")
algo = fp.readline().rstrip()
rc_count = convert_to_list(fp.readline().rstrip())
C = int(rc_count[0])
R = int(rc_count[1])
land_site = convert_to_list(fp.readline().rstrip())
sr = int(land_site[1])
sc = int(land_site[0])
max_h = int(fp.readline().rstrip())
no_target = int(fp.readline().rstrip())
end_r = []
end_c = []
end_sites,grid_str = [],[]
grid = []
for i in range(0,no_target):
    end_sites = convert_to_list(fp.readline().rstrip())
    end_c.append(int(end_sites[0]))
    end_r.append(int(end_sites[1]))
for i in range(0,R):
    grid_str = convert_to_list(fp.readline().rstrip())
    grid.append([int(i) for i in grid_str]) 
fp.close()

def solve_bfs(R,C,sr,sc,max_h,er,ec,maze):
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0
    move_count = 0
    reached_end = False
    rq = queue.Queue()
    rq.queue.clear()
    cq = queue.Queue()
    cq.queue.clear()
    parent = {}
    parent.clear()
    output_nodes = []
    output_nodes.clear()
    visited = []
    minimumCost = []
    for i in range(0,R):
        visited.append([])
        minimumCost.append([])
        for j in range(0,C):
            visited[i].append(0)
            minimumCost[i].append(0)
    dr = [-1,+1,0,0,-1,+1,+1,-1]
    dc = [0,0,+1,-1,-1,+1,-1,+1]
    rq.put(sr)
    cq.put(sc)
    if sr==er and sc==ec:
        output_nodes = [[ec,er]]
        
    minimumCost[sr][sc]=0
    visited[sr][sc]=True
    while rq.qsize()>0:
        r = rq.get()
        c = cq.get()
        old_val = maze[r][c]
        if r==er and c==ec:
            reached_end = True
            break
        explore_neighbours_bfs(parent,minimumCost,r,c,R,C,rq,cq,dr,dc,nodes_in_next_layer,visited,old_val,maze,max_h)
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            minimumCost[r][c] += 1
            move_count += 1 
    end = [er,ec]
    start = (sr,sc)
    if reached_end:
        x = end
        y = convert(x)
        on=[]
        str_count = 0
        while(y!=start):
            y = convert(x)
            x = parent.get(y,None)
            output_nodes.append(y[::-1])
        output_nodes.reverse()
        for i in range (0,len(output_nodes)):
            for j in range (0,len(output_nodes[0])):
                on.append(str(output_nodes[i][j]))
                str_count += 1
                if str_count%2==0:
                    on.append(" ")
                else:
                    on.append(',')
        str_on = convert_string(on)
    else:
        str_on = 'FAIL'
    return str_on
def explore_neighbours_bfs(parent,minimumCost,r,c,R,C,rq,cq,dr,dc,nodes_in_next_layer,visited,old_val,maze,max_h):
    for i in range(0,8):
        rr = r+dr[i]
        cc = c+dc[i]
        cost = 1
        if rr<0 or cc<0:
            continue
        if rr>=R or cc>=C:
            continue    
        if visited[rr][cc]:
            minimumCost[rr][cc] = min(minimumCost[rr][cc],minimumCost[r][c]+cost)
            continue
        new_val = maze[rr][cc]
        if abs(old_val-new_val)>max_h:
            continue 
        minimumCost[rr][cc]=minimumCost[r][c]+cost
        rq.put(rr)
        cq.put(cc)
        parent[rr,cc] = [r,c]
        visited[rr][cc]=True
        nodes_in_next_layer= nodes_in_next_layer+1
class Node_ucs():
    def __init__(self, depth = None, parent=None, x_pos=None, y_pos=None):
        self.depth = depth
        self.parent = parent
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.position = [x_pos,y_pos]
        self.cost = 0

def neighbour_list_ucs(node,R,C,dr,dc,max_h,maze):
        neighbour = []
        for i in range(0,8):
            new_x = node.x_pos+dr[i]
            new_y = node.y_pos+dc[i]
            if new_x<0 or new_y<0:
                continue
            if new_x>=R or new_y>=C:
                continue
            new_val = maze[new_x][new_y]
            if abs(node.depth-new_val)>max_h:
                continue 
            neighbour.append(Node_ucs(maze[new_x][new_y],node,new_x,new_y))
        return neighbour
def solve_ucs(R,C,start_row,start_col,max_h,end_row,end_col,maze):
    dr = [-1,+1,0,0,-1,+1,+1,-1]
    dc = [0,0,+1,-1,-1,+1,-1,+1]
    reached_end = False
    startNode = Node_ucs(maze[start_row][start_col],None,start_row,start_col)
    startNode.cost = 0
    endNode = Node_ucs(maze[end_row][end_col],None,end_row,end_col) 
    open_list = []
    closed_list = []
    cost = 0
        
    open_list.append(startNode)
    while(len(open_list)>0):
        currentNode = open_list[0]
        for i in range(1,len(open_list)):
            if open_list[i].cost<currentNode.cost:
                currentNode = open_list[i]
        open_list.remove(currentNode)
        closed_list.append(currentNode)
        
        neighbours = []
        neighbours = neighbour_list_ucs(currentNode,R,C,dr,dc,max_h,maze)
        for i in neighbours:
            flag = 0
            r = i.x_pos
            c = i.y_pos
            rr = currentNode.x_pos
            cc = currentNode.y_pos
            if abs(rr-r)==1 and abs(cc-c)==0 or abs(rr-r)==0 and abs(cc-c)==1:
                cost = 10
            else:
                cost = 14
            for closed_neighbour in closed_list:
                if i == closed_neighbour:
                    flag = 1
                    break
            for open_node in open_list:
                if i == open_node and i.cost > open_node.cost:
                    flag = 2
                    break
            if flag !=0:
                continue
            if(i==endNode):
                reached_end = True
            i.cost = currentNode.cost + cost
            open_list.append(i)    
            
        if currentNode == endNode or reached_end == True:
            path = []
            path.append([endNode.x_pos,endNode.y_pos])
            current = currentNode
            while current is not None:
                path.append([current.x_pos,current.y_pos])
                current = current.parent
            path.reverse()
            outputs = list_to_string(path)
            return outputs
#    if reached_end == False:
#        return 'FAIL'




def list_to_string(lists):
    on = []
    str_count = 0 
    for i in range (0,len(lists)):
        for j in range (0,len(lists[0])):
            on.append(str(lists[i][j]))
            str_count += 1
            if str_count%2==0:
                on.append(" ")
            else:
                on.append(',')
    str_on = convert_string(on)
    return str_on




import math
class Node():
    def __init__(self, depth = None, parent=None, y_pos=None, x_pos=None):
        self.depth = depth
        self.parent = parent
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.position = [x_pos,y_pos]
        self.gCost = 0
        self.hCost = 0
        self.fCost = self.gCost+self.hCost
        
def neighbour_list(node,R,C,dr,dc,max_h,maze):
        neighbour = []
        for i in range(0,8):
            new_x = node.x_pos+dr[i]
            new_y = node.y_pos+dc[i]
            new_val = maze[new_x][new_y]
            if new_x<0 or new_y<0:
                continue
            if new_x>=R or new_y>=C:
                continue
            if abs(node.depth-new_val)>max_h:
                continue 
            neighbour.append(Node(maze[new_x][new_y],node,new_x,new_y))
        return neighbour
def solve_Astar(R,C,sr,sc,max_h,end_r,end_c,maze):
    dr = [-1,+1,0,0,-1,+1,+1,-1]
    dc = [0,0,+1,-1,-1,+1,-1,+1]
    reached_end = False
    startNode = Node(maze[sr][sc],None,sr,sc)
    startNode.gCost = startNode.hCost = startNode.fCost = 0
    endNode = Node(maze[end_r][end_c],None,end_r,end_c) 
    open_list = []
    closed_list = []
    cost = 0
        
    open_list.append(startNode)
    while(len(open_list)>0):
        currentNode = open_list[0]
        for i in range(1,len(open_list)):
            if open_list[i].fCost<currentNode.fCost:
                currentNode = open_list[i]
        open_list.remove(currentNode)
        closed_list.append(currentNode)
        
        neighbours = []
        neighbours = neighbour_list(currentNode,R,C,dr,dc,max_h,maze)
        depth_diff = 0
        for i in neighbours:
            flag = 0
            r = i.x_pos
            c = i.y_pos
            rr = currentNode.x_pos
            cc = currentNode.y_pos
            if abs(rr-r)==1 and abs(cc-c)==0 or abs(rr-r)==0 and abs(cc-c)==1:
                cost = 10
            else:
                cost = 14
            for closed_neighbour in closed_list:
                if i == closed_neighbour:
                    flag = 1
                    break
            for open_node in open_list:
                if i == open_node and i.fCost > open_node.fCost:
                    flag = 2
                    break
            if flag !=0:
                continue
            if(i==endNode):
                reached_end = True
            depth_diff = abs(currentNode.depth - i.depth)
            i.gCost = currentNode.gCost + cost + depth_diff
            i.hCost = math.sqrt((currentNode.x_pos - endNode.x_pos)**2+(currentNode.y_pos - endNode.y_pos)**2)
            open_list.append(i)    
            
            if reached_end == True:
                path = []
                path.append([endNode.x_pos,endNode.y_pos])
                current = currentNode
            while current is not None:
                path.append([current.x_pos,current.y_pos])
                current = current.parent
            path.reverse()
            outputs = list_to_string(path)
            return outputs
    if reached_end == False:
        return 'FAIL'
            
fw = open("output.txt","w")
out = []
if algo == 'BFS':
    for i in range(0,no_target):
        out.append(solve_bfs(R,C,sr,sc,max_h,end_r[i],end_c[i],grid))    
    for i in out:
        fw.write(i)
        fw.write('\n')
elif algo =='UCS':
    for i in range(0,no_target):
       # print(solve_ucs(R,C,sr,sc,max_h,end_r[i],end_c[i],grid))
        out.append(solve_ucs(R,C,sr,sc,max_h,end_r[i],end_c[i],grid))
    for i in out:
        fw.write(i)
        fw.write('\n') 
elif algo =='A*':
    for i in range(0,no_target):
        out.append(solve_bfs(R,C,sr,sc,max_h,end_r[i],end_c[i],grid))
    for i in out:
        fw.write(i)
        fw.write('\n')
fw.close()