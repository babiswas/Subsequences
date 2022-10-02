def jump_steps(arr):
    jumps=0
    max_range=0
    if arr[0]==0:
        return -1
    elif len(arr)==1:
        return 0
    steps=arr[0]
    for i in range(len(arr)):
        steps-=1
        max_range=max(max_range,i+arr[i])
        if steps==0:
           steps=max_range-i
           if steps==0:
               return -1
           jumps+=1
    return jumps


def jump_bfs(arr):
    queue=list()
    index=0
    jumps=0
    queue.append(arr[index])
    destination=len(arr)-1
    while queue:
        m=queue.pop(0)
        if m==destination:
            return jumps
        if arr[index]==0:
            return -1
        for i in range(index+1,index+arr[index]):
            queue.append(i)
        jumps+=1
    return jumps
            
    

if __name__=="__main__":
    print(jump_steps([3,2,1,0,4]))
    
        