#Find triplets in an array.
def find_triplets(arr,target):
    sum=0
    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1,len(arr)):
                sum=arr[i]+arr[j]+arr[k]
                if sum==target:
                    return i,j,k
            sum=0
    return -1,-1,-1

#Find triplets in an array
def find_triplets_sort(arr,target):
    arr.sort()
    for i in range(len(arr)):
        temp=target-arr[i]
        index1=i+1
        index2=len(arr)-1
        while index1<index2:
            temp1=temp-arr[index1]
            if temp1<arr[index2]:
                index2=index2-1
            elif temp1>arr[index2]:
                index1=index1+1
            else:
                return i,index1,index2
    return -1,-1,-1


#Binary search algorithm
def binary_search(arr,low,high,key):
    while low<=high:
        mid=(low + high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        elif arr[mid]>key:
            high=mid-1
    return -1

#Find peak element
def peak_element(arr):
    if len(arr)==1:
        return -1
    elif len(arr)==2:
        if arr[0]<arr[1]:
            return 1
        elif arr[0]>arr[1]:
            return 0
        else:
            return 0
    for i in range(len(arr)):
        if i-1>=0 and i+1<len(arr):
            if arr[i-1]<=arr[i] and arr[i+1]<=arr[i]:
                return i
        elif i==0:
            if arr[0]>arr[i+1]:
                return 0
        elif i==len(arr)-1:
            if arr[i]>arr[i-1]:
                return i
    return -1

#Find peak element binary search
def peak_element_search(arr,low,high):
    while low<=high:
        mid=(low+high)//2
        if mid!=0 and mid!=high-1:
            if arr[mid]>=arr[mid+1] and arr[mid]<=arr[mid-1]:
                return mid
            else:
                if arr[mid]<=arr[mid+1]:
                   low=mid+1
                elif arr[mid]<=arr[mid-1]:
                    high=mid-1
        elif mid==0:
            if arr[mid]>=arr[mid+1]:
                return mid
            else:
                low=mid+1
        elif mid==high-1:
            if arr[mid]>=arr[mid-1]:
                return mid
            else:
                high=mid-1
            
if __name__=="__main__":
    arr=[12, 3, 4, 1, 6, 9]
    i,j,k=find_triplets(arr,24)
    print(arr[i],arr[j],arr[k])
    arr=[1, 2, 3, 4, 5]
    i,j,k=find_triplets_sort(arr,9)
    print(arr[i],arr[j],arr[k])
    arr=[12, 3, 4, 1, 6, 9]
    i,j,k=find_triplets_sort(arr,24)
    print(arr[i],arr[j],arr[k])
    print("The binary search of the tree is:")
    arr=[5,9,15,19,20,23,32,50,64,72]
    for i in arr:
        print(binary_search(arr,0,10,i))
    print(binary_search(arr,0,10,-10))
    print("The peak element of the array is:")
    arr=[1,2,3]
    print(peak_element(arr))
    print("The peak element in the array is:")
    print(peak_element_search([1,2,3],0,3))
    
    
    
    
    