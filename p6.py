import sys
def find(s,t,m,n):
    if m==0 and n!=0:
       return -1
    elif n==0:
       return 0
    else:
        if s[m-1]!=t[n-1]:
              return 1+min(find(s,t,m-1,n),find(s,t,m,n-1))
        else:
           return find(s,t,m-1,n-1)

if __name__=="__main__":
   print(find("babab","babba",len("babab"),len("babba")))