import sys
def find_2nd_largest(arr):
    maxm1=-sys.maxsize+1
    maxm2=-sys.maxsize+1
    index=0
    while index<len(arr):
        if arr[index]>maxm1:
            maxm2=maxm1
            maxm1=arr[index]
        else:
            if maxm2<arr[index]:
                maxm2=arr[index]
        index=index+1
    return maxm2

if __name__=="__main__":
    print("Displaying the second largest number in an array:")
    large2=find_2nd_largest([10,3,2,45,16,28,23,29,-1,4])
    print(large2)
    
        