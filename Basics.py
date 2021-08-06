#--1-----Declare a variable of data type int with name empID--------------------------------------------------------------

empID = int(input())    

#--2-----Declare a variable of data type string with name empName---------------------------------------------------------

empName = input()          

#--3-----Assign a value 5 for the empId variable and print the value of empId on console----------------------------------

empID = 5 
print(empID)

#--4-----Assign a value "Puja" for the empName variable and print the value of empId on console---------------------------

empName = "Puja"
print(empName)

#--5-----write a program to check whether it is odd or even----------------------------------------------------------
#          Ex: Input-2  
#              OutPut-even  

number = int(input())

if(number % 2 ==0):
    print("Even")
else:
    print("Odd")

#--6-----Write a program to swap 2 numbers----------------------------------------------------------------------------
#          Ex: Input- 22,65 
#              Output- 65,22   

number=input() 
result = number.split(",")
print(result[1]+","+result[0])