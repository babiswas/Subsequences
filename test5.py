def partition(arr):
    wall=-1
    pivot=arr[len(arr)-1]
    for i in range(len(arr)-1):
        if arr[i]<pivot:
            wall+=1
            arr[wall],arr[i]=arr[i],arr[wall]
    wall+=1
    arr[wall],arr[len(arr)-1]=arr[len(arr)-1],arr[wall]
    return wall

if __name__=="__main__":
    arr=[12,11,2,21,10,6,9,14,23,26,16]
    partition(arr)
    print(arr)
    