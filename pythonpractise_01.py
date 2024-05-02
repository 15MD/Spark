print("Hello World!")


# python variables
x='mohit'
print(x)
print(type(x))

y=5
print(y)
print(type(y))

# Python Data Structure
 #list
aList = ['a','b','c','d','e','f']
print(type(aList))
for i in aList:
  print(i)

  #list methods
    #- sort(),reverse(),pop(),count(),append()

 #tuple
  atuple= ('a','b','c','d')
  for i in atuple:
   print(i)

   #tuple methods
    #- count() - Returns the number of times a specified value occurs in a tuple
    #index() - 	Searches the tuple for a specified value and returns the position of where it was found

 #range
aRange = range(6)
for i in aRange:
   print(i)

 #dict
aDict = {"1":"Mohit","2":"Rutuja","3":"Nancy"}
print(aDict.items())
print(aDict)
  #dict methods
    #- get(),items(),keys(),values()
# for i in aDict:
#    print(i)


 #set
aSet = {"apple", "banana", "cherry"}
for i in aSet:
   print(i)

    #set methods
    #- add(),pop(),discard(),values()
   # remove()- remove the specified element


# Python loops
#    Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
   
#1. if -Else
   a= 4
   b=1

   if a> b:
     print('Correct')
   elif(a==b):
    print('1st conditon') 
   else:
     print('In else condition')  

 #2. While loop

ab = 1
while ab < 6:
  print(ab)
  if ab == 3:
    break
  ab += 1    
print(ab)


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


#3. For loop
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# Functions:
  def my_fun(*a):
    # print("It's a function")
    print("value of argument is " , a[0],a[1])
    return a[0]+a[1]

  my_fun(5,4) 

  def list_fun(aList):
     for i in aList:
       print(i)

  aa= [1,2,3,4]
  list_fun(aa)     


  # class 

  class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printname(self):
     print(self.name, self.age)
    
#   P1= person("mohit",31) 

#   print(P1) 
 
 #inheritance
  
  class employee(person):  
    pass
x = employee("mohit", 31)   
print(x.printname()) 