def find_duplicates(arr):
    for i in range(len(arr)):
       for j in range(len(arr)):
           if i!=j and arr[i]==arr[j]:
               print(f"{arr[i]} is the duplicate")
               
def find_duplicates_hash(arr):
    m=dict()
    for index,value in enumerate(arr):
        count=m.get(value,0)
        m.update({value:count+1})
    for key,value in m.items():
        if value>1:
            print(key)
            
def find_duplicates_arr(arr):
    for i in range(len(arr)):
        index=arr[i]%len(arr)
        arr[index]=arr[index]+len(arr)
    for index,value in enumerate(arr):
        num=value//len(arr)
        if num>=2:
           print(index)
        
                      
if __name__=="__main__":
    find_duplicates([1, 2, 3, 4 ,3])
    print("The duplicate in the array is:")
    find_duplicates_hash([1, 2, 3, 4 ,3])
    print("The duplicate in the array is:")
    find_duplicates_arr([1, 2, 3, 4 ,3])
    
               