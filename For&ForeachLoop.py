#---1-----Write a program in C# Sharp to display n terms of natural number and their sum.------------------------------------------------------------
#            Ex:
#            Input :
#               Enter number of natural terms do you want
#            Output :
#               The first 7 natural number is :1 2 3 4 5 6 7
#               The Sum of Natural Number upto 7 terms : 28

num = int(input("Enter number of natural terms do you want : ")) 
result=0
for i in range(1,num+1):
    result = result + i
    print(i)
print("The Sum of n Natural Number : " + str(result))

#---2-----Write a program in C# Sharp to display the n terms of odd natural number and their sum.------------------------------------------------------
#            Ex:
#            Input :
#               Input number of terms : 10
#            Output :
#               The odd numbers are :1 3 5 7 9 11 13 15 17 19
#               The Sum of odd Natural Number upto 10 terms : 100

num = int(input("Enter number of natural terms do you want : ")) 
result=0
for i in range(1,num+1):
    if (i%2 == 1):
        print(i)
        result = result + i

print("The Sum of n Odd Natural Number : " + str(result))

#---3-----By using Array write the program using For and Foreach loop in c#---------------------------------------------------------------------------
#            Ex:
#            Input :
#               Enter Array printing using for loop
#               Enter Array printing using ForEach loop
#            Output :
#               JalaTechnologies
#               JalaTechnologies

a = input("Enter a any string : ")
result = ''
for i in a:
    result= result + i 

print(result)