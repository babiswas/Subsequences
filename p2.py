#Find if the string str1 is present in the subsequence str2
def find(str1,str2):
    index1=0
    index2=0
    while index1<len(str1) and index2<len(str2):
        if str1[index1]==str2[index2]:
            index1+=1
            index2+=1
        elif str1[index1]!=str2[index2]:
            index2+=1
    if index1==len(str1):
        return True
    else:
        return False

def find1(str1,str2,m,n):
    if m==0:
        return True
    elif n==0:
        return False
    else:
        if str1[m-1]==str2[n-1]:
            return find1(str1,str2,m-1,n-1)
        else:
            return find1(str1,str2,m,n-1)
        
    
if __name__=="__main__":
    print(find("AXY","ADXCPY"))
    print(find("AXY","YADXCP"))
    print(find("gksrek","geeksforgeeks"))
    print(find1("gksrek","geeksforgeeks",len("gksrek"),len("geeksforgeeks")))