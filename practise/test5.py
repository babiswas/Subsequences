import string

def reverse(str1):
    temp=list(str1)
    index1=0
    index2=len(temp)-1
    while index1<index2:
          temp[index1],temp[index2]=temp[index2],temp[index1]
          index1+=1
          index2-=1
    return temp

if __name__=="__main__":
    print(''.join(reverse("bapan")))