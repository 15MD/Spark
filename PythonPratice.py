class Animal:
    
    def __init__(self) -> None:
         pass

    def getName(self):
        print("I am a class.")

    def fibas(self,a,b,wheretostop):
        
        listA = []
        listA.append(a)
        listA.append(b)        
               
        for i in range(wheretostop -1 ):
            print("a is =>",a)
            print("b is =>",b)
            summ = a+b   
            print("sum is =>",summ)
            listA.append(summ)
            a = b
            b= summ        
        return listA  

    q= 0
    def recursiveFibonnaci(self,a,b):
     global q 
     print("a is =>",a)
     print("b is =>",b)
     print("q is =>",q)
     listA = []
     listA.append(a)
     listA.append(b)     
     if q <= 14:
        print("a is =>",a)
        print("b is =>",b)         
        summ = a+b
        print("sum is =>",summ)
        listA.append(summ)
        a = b
        b= summ
        q += 1
        self.recursiveFibonnaci(a,b)
        return listA  
     else:
        return 
     

            
            

dog = Animal()

#dog.getName()
#dog.fibas(1,1,6)
dog.recursiveFibonnaci(1,1)


print(0)
print(1)


print(0)
print(1)
count = 0

def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)

 


def fibOne(n):
    listB = []
    total = 0
    for i in range(n):
        #print(i)
        total = total + i
        listB.append(total)
    return listB
    
fibOne(10)

def fib2(n):
    listB = []
    total = 0
    a = 0
    b =1
    i = 0
    while(i< n):
        total = a +b
        listB.append(total)
        a= b
        b = total
        i = i +1
    
    return listB
    
fib2(10)



#version 1      
def facto(n):
   i = 1
   listA = []
   total = 1
   listA.append(n)
   for i in range(n):
      if(i >0):
       listA.append(i)
      #print(listA)  
   for j in listA:
      #print("total =>",total)
      total = total * j

   return total      

facto(6)     

#version 2
      
def facto(n):
   total =1
   for i in range(n+1):
      if(i >0):
       total = total * i 
                
   return total      

facto(7) 