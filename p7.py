import sys
def find(str1,target,m,n):
   if n==0:
      return 1
   elif m==0:
      return sys.maxsize-1
   else:
      ch=-1
      for i in range(n-1,-1,-1):
        if target[i]==str1[m-1]:
           ch=i
           break
      if ch==-1:
         return 1
      else:
         return min(find(str1,target,m-1,ch)+1,find(str1,target,m-1,n))

if __name__=="__main__":
   print(find("babab","babba",len("babab"),len("babba")))
   
    