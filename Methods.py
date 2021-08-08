#---1-----Write a program using WriteLine(Boolean) method in c#-------------------------------------------------------------------------------------

#---2-----Write a program on static and instance methods in c# -------------------------------------------------------------------------------------

#---3-----Write a method of Calculator and print sum and product in c#------------------------------------------------------------------------------
#            Ex:
#            Input : 
#               enter a and b values
#            Output : 
#               sum = 12 and product = 36

#------------------------------------BELLOW--CODE--IN---[python-Language]--------------------------------------------------------

a = int(input("Enter value 1 : "))
b = int(input("Enter value 2 : "))
sum = a + b
product = a * b
print("Sum of given 2 values : " + str(sum))
print("Product of given 2 values : " + str(product))

#---4-----Write a program using parameter arrays and print output in console in c#-------------------------------------------------------------------

list_a = ['1','2','3'] 
list_b = ['red','green','blue']

result = list_a.append(list_b)

for i in result:
    print(i)

#---5-----Write a program to print entered number of even numbers in c#----------------------------------------------------------------------------
#            Ex:
#            Input :
#               Enter number : 5
#            Output :
#               2 4 6 10 12

numList = []

print("Enter 10 Numbers: ")

for i in range(10):
  numList.insert(i, int(input()))

print("\nEven Numbers:")

for i in range(10):
  if numList[i]%2==0:
    print(numList[i])