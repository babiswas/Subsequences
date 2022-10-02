#Count all the distinct subsequence.
def count_distinct(str1):
      myset=set()
      temp=list()
      index=0
      def count_util(index,temp):
            if index==len(str1):
               myset.add(''.join(temp.copy()))
               return
            temp.append(str1[index])
            count_util(index+1,temp)
            temp.pop()
            count_util(index+1,temp)
      count_util(index,temp)
      return len(myset)
   
#dynamic programming
def count_unique(str1):
   dp=[0]*(len(str1)+1)
   dp[0]=1
   test=[-1]*27
   for i in range(0,len(str1)):
      print(dp)
      print(test)
      dp[i+1]=2*dp[i]
      if test[ord(str1[i])-ord('a')]!=-1:
         dp[i+1]=dp[i+1]-dp[test[ord(str1[i])-ord('a')]-1]
      test[ord(str1[i])-ord('a')]=i+1
   print(test)
   print(dp)
   return dp[-1]
if __name__=="__main__":
   print(count_distinct("gfg"))
   print(count_unique("gfg"))
   
      
         
    


         