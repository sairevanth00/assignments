#---1-----Write a program to Implicit Type Conversion------------------------------------------------------------------------------------------
#           Ex: 
#              Input : Enter Int value
#                      Enter Long value
#              Output :Int value - 53
#                      Long value - 53

a = 7
print(type(a))
b = 3.0
print(type(b))
c = a + b
print(c)
print(type(c))
d = a * b
print(d)
print(type(d))

#---2-----Write an example of explicit type conversion---------------------------------------------------------------------------------------------
#            Ex:
#                Input :Enter Value of I
#                Output :Value of I is 34 

c = input("Enter any Char : ")
print("The ASCII value of '" + c + "' is", ord(c))

#---3-----Write a program of built in type conversion methods-------------------------------------------------------------------------------------
#           Ex:
#               Input :Enter string name
#                      Enter Integer value
#               Output :string to float - 34.6
#                       int to double - 337


string= "3.141"
  
print(string)
print(type(string))
  
Float = float(string)  
  
print(Float)
print(type(Float))

#---4-----Write a program that converts various value types to string type--------------------------------------------------------------------------
#            Ex:
#                Input :Enter Integer value
#                       Enter Float Value
#                Output :int.ToString() - 75
#                        float.ToString()- 43.09