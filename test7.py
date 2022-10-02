import sys
def minm_steps(arr):
    minm_steps=0
    index=0
    def minm_steps_util(index,minm_steps):
        if index==len(arr)-1:
           return minm_steps
        elif arr[index]==0:
           return sys.maxsize-2
        elif index+arr[index]>=len(arr)-1:
             return minm_steps+1
        else:
            return min([minm_steps_util(i,minm_steps)+1 for i in range(index+1,index+arr[index]+1)])
    minm_steps=minm_steps_util(index,minm_steps)
    return minm_steps

def minm_jumps(arr):
    minm_steps=0
    index=0
    def find_steps(index,minm_steps):
        temp=sys.maxsize
        if index==len(arr)-1:
           return minm_steps
        elif arr[index]==0:
           return sys.maxsize
        elif index+arr[index]>=len(arr)-1:
           return minm_steps+1
        else:
            for i in range(index+1,index+arr[index]+1):
                test=find_steps(i,minm_steps)
                if test<temp:
                    temp=test
            return temp+1
    return find_steps(index,minm_steps)
                
           

if __name__=="__main__":
    print(minm_steps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
    print(minm_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
    
                
           
           
        
    