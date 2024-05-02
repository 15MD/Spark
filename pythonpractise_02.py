A= [23,5,9]

def myfunc(listA):
    # print(listA)
    listA.sort()
    # print(listA)
    # print(len(listA))
    # print(listA[2])
    return listA[len(listA)-1]
myfunc(A)    

A= [23,5,9]
def sumfunn(listA):
    sum = 0;
    for i in listA:
        sum = sum + i
    return sum    
sumfunn(A)


#reverse the string


st = "mohit"    
def reverse(s):
    str = ""
    for i in s:
        # print(i)
        str =  i + str
        # print(str)
    return str

reverse(st)

# factorial

def factorial(A):
    total = 1
    if A== 0:
        return 1
    while A > 0:
       total = total * A
       A = A- 1

    return total

factorial(8)    

# check prime number
def checkPrime(A):
 for i in range(2,A-1):
     if A % i== 0:
         return 'Not Prime'
     elif A%1 == 0 & A%A == 0:
         return 'Prime number'     
 
checkPrime(12) 


#Fibonaci

def fibseries(n):
    a= 0
    b= 1
    listA= []
    listA.append(a)
    listA.append(b)
    for i in range(2,n):
        c= a+b
        listA.append(c)
        if c > n:
         break
        a=b
        b=c
    return listA

fibseries(15)    

# maximum frequency character in string

def max_frequency(A):
  countFrequncey = {}
  for i in A:
     if i in countFrequncey:        
        countFrequncey.update({i:countFrequncey.get(i)+1})
        # countFrequncey[i]+=1
     else:
         #countFrequncey[i]=1
         countFrequncey.update({i:1})  

  # finding the character with maximum frequency
  max_char = max(countFrequncey, key=countFrequncey.get)

# printing result
  print("The maximum of all characters in GeeksforGeeks is : " + str(max_char))

max_frequency("GeeksforGeeks")


