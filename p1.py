def find(str1,K):
      ch=''
      m=dict()
      for i in str1:
         count=m.get(i,0)
         m.update({i:count+1})
      for i in str1:
        count=m.get(i)
        if count>=K:
           ch+=i
      return ch

def find1(str1,K):
   counter=0
   ch=''
   for i in range(len(str1)):
      counter+=1
      if i+1<len(str1):
         for j in range(i+1,len(str1)):
           if str1[i]==str1[j]:
             counter+=1
      if str1[i] in ch:
         ch+=str1[i]
      elif counter>=K:
         ch+=str1[i]
      counter=0         
   return ch
      
         
            
     

if __name__=="__main__":
   print(find("geeksforgeeks",2))
   print(find("aabbaabacabb",5))
   print("The brute force approach:")
   print(find1("geeksforgeeks",2))
   print(find1("aabbaabacabb",5))

           