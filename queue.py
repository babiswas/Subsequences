#implement stack using queue

class Stack_Queue:

    def __init__(self):
        self.q1=list()
        self.q2=list()

    def insert_num(self,num):
       #push operation in stack.
       self.q2.clear()
       self.q2.append(num)
       while self.q1:
          n=self.q1.pop(0)
          self.q2.append(n)
       while self.q2:
           m=self.q2.pop(0)
           self.q1.append(m)

    def get_top(self):
        #top of the stack.
        if self.q1:
            return self.q1[0]
    
    def pop_num(self):
        #pop operation in stack.
        if self.q1:
            return self.q1.pop(0)

if __name__=="__main__":
   #implemented a stack using a queue.
   myqueue= Stack_Queue()
   myqueue.insert_num(3)
   myqueue.insert_num(12)
   myqueue.insert_num(10)
   myqueue.insert_num(14)
   print(myqueue.get_top())
   print(myqueue.pop_num())
   print(myqueue.get_top())
   
  
     
