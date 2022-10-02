def find_max_subarr(arr,k):
    sum=0
    i=0
    j=0
    maxm=0
    while j<len(arr):
        if sum<k:
            sum+=arr[j]
            if sum==k:
               maxm=max(maxm,j-i+1)
               sum-=arr[i]
               i=i+1
            j+=1
        elif sum>k:
            sum-=arr[i]
            if sum==k:
               maxm=max(maxm,j-i+1)
            i-=1
    return maxm

if __name__=="__main__":
    print(find_max_subarr([10, 5, 2, 7, 1, 9],15))
    
    