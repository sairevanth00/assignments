#---1-----Write the program to demonstrate the working of Binary Arithmetic Operators ?------------------------------------------------------------------
#            Ex:
#            Input :Enter a and b values and result to perform operations on (+,-,*,/,%)
#            Output :
#               Addition Operator: 15
#               Subtraction Operator: 5
#               Multiplication Operator: 50
#               Division Operator: 2
#               Modulo Operator: 0

firstNum = int(input("Enter First Num : "))
secondNum = int(input("Enter Second Num : "))

result_1 = firstNum + secondNum 
result_2 = firstNum - secondNum
result_3 = firstNum * secondNum 
result_4 = firstNum / secondNum
result_5 = firstNum % secondNum

print("Addition of Given Two Num : " + str(result_1))
print("Subtraction of Given Two Num : " + str(result_2))
print("Multiplication of Given Two Num : " + str(result_3))
print("Division of Given Two Num : " + str(result_4))
print("Modulo of Given Two Num : "+ str(result_5))

#---2-----Write the program to demonstrate the working of Unary Arithmetic Operators ?-------------------------------------------------------------------------
#            Ex:
#            Input :Enter a value and res to perform operations on (a++,a--,++a,--a)
#            Output :
#               a is 11 and res is 10
#               a is 10 and res is 11
#               a is 11 and res is 11
#               a is 10 and res is 10



#---3-----Write the program to demonstrate the working of Relational Operators ?
#            Ex:
#           Input :Enter a and b values and result to perform operations on (==,>,<,>=,<=,!=)
#           Output :
#               Equal to Operator: False
#               Greater than Operator: False
#               Less than Operator: True
#               Greater than or Equal to: False
#               Lesser than or Equal to: True
#               Not Equal to Operator: True
print("Enter any two values")

num_1 = int(input("Enter any first value : "))

num_2 = int(input("Enter any second value : ")) 

if (num_1 != num_2):
    print("True")

elif(num_1 == num_2):
    print("False")

elif(num_1 > num_2):
    print("False")

elif(num_1 < num_2):
    print("True")

elif(num_1 >= num_2):
    print("False")

elif(num_1 <= num_2):
    print("False")