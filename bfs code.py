graph ={
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : [],
    '8' : []
}

visited = [] #List for visited nodes.
queue =[] #Initialize a queue.
 
def bfs(visited,graph,node):
    visited.append(node)   #5
    queue.append(node)     #5
 
    while queue:
        m = queue.pop(0)
        # print(m,end=" ") # [5,3]
 
        for i in graph[m]:
            if i not in visited:
                print("I:", i)
                visited.append(i)
                queue.append(i)  
 
#Driver Code
print("following is the Breadth-First Search")
bfs(visited,graph,'5')

    