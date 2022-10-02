def find_subarray(arr,target):
    sum=0
    index1=0
    index2=0
    for i in range(len(arr)):
       index1=i
       sum+=arr[i]
       if sum==target:
          index2=i
          return index1,index2
       if i+1<len(arr):
         for j in range(i+1,len(arr)):
             sum+=arr[j]
             if sum==target:
                index2=j
                return index1,index2
         sum=0
    return -100,-100

def find_new_subarray(arr,target):
    sum=0
    left=0
    right=0
    while left<=right:
      if sum<target:
         sum+=arr[right]
         right=right+1
      elif sum>target:
         sum-=arr[left]
         left=left+1
      elif sum==target:
         return left,right
    return -100,-100
      
       


if __name__=="__main__":
   print(find_subarray([1,2,2,2,12],12))
   print(find_new_subarray([1,2,2,2,12],12))
  
   
       
       