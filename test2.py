def find_pair(arr,target):
    if len(arr)==0:
        return -1,-1
    elif len(arr)==1:
        return -1,-1
    else:
        for i in range(0,len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]==target:
                    return i,j
        return -1,-1
    
def find_pair_sorting(arr,target):
    if len(arr)==0:
        return -1,-1
    elif len(arr)==1:
        return -1,-1
    else:
        arr.sort()
        index1=0
        index2=len(arr)-1
        while index1<index2:
            temp=target-arr[index1]
            if temp>arr[index2]:
                index1+=1
            elif temp<arr[index2]:
                index2-=1
            else:
                return index1,index2
        return -1,-1

def find_pair_hash(arr,target):
    m=dict()
    for index,value in enumerate(arr):
        m.update({value:index})
    for index,value in enumerate(arr):
        temp=target-value
        test=m.get(temp,-1)
        if test!=-1 and test!=index:
            return index,test
    return -1,-1

def find_pair_remandr(arr,target):
    rem=[0 for i in range(target+1)]
    for i in arr:
        if i<=target:
            rem[i%target]=rem[i%target]+1
    for i in range(target//2):
        if rem[i]!=0:
            if rem[target-i]!=0:
                return i,target-i
    return -1,-1

if __name__=="__main__":
    arr=[1, 5, 7, -1]
    index1,index2=find_pair(arr,6)
    print(arr[index1],arr[index2])
    arr=[1, 5, 7, -1]
    index1,index2=find_pair_sorting(arr,6)
    print(arr[index1],arr[index2])
    arr=[1, 5, 7, -1]
    index1,index2=find_pair_hash(arr,6)
    print(arr[index1],arr[index2])
    arr=[1, 5, 7, -1]
    num1,num2=find_pair_remandr(arr,6)
    print(num1,num2)
                
            
    