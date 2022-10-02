#Find subset of two numbers
def subset_2(l):
    subsets=list()
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            subsets.append((l[i],l[j]))
    return subsets

def find_all_subset(l):
    subsets=list()
    index=0
    temp=list()
    def all_subset(index,temp):
        if index==len(l):
           subsets.append(temp.copy())
           return 
        temp.append(l[index])
        all_subset(index+1,temp)
        temp.pop()
        all_subset(index+1,temp)
    all_subset(index,temp)     
    return subsets
        

if __name__=="__main__":
    print(subset_2([2,4,5,7,8]))
    print(find_all_subset([2,4,5,7,8]))
            