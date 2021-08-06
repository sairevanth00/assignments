#---1-----Create any value called EmpName and print that value in the output-----------------------------------------

EmpName = "JALA Technologies" #string type

print(EmpName)

#---2-----Declare a variable name of any datatype and read the name in the output-------------------------------------

name = True  #Boolean type

print(name)

#---3-----Declare a 2 strings as input and contacenate with another string with the both Strings and get Output-------------------------------
#       Ex: Input : enter firstname , enter lastname , "Hello" + firstname + lastname
#           Output: Hello firstname lastname

firstName = input()
lastName  = input()

result = "Hello! " +firstName+" "+lastName #string concatination

print(result)



#---4-----Write a program by taking two integer values and return the value by adding in the Output-----------------------------
#       Ex: Input : 5,4
#           Output : 9

Given_two_num = input()

split_two_num = Given_two_num.split(",")

result= int(split_two_num[0]) + int(split_two_num[1]) #adding 2 integers

print(result)

#---5-----Write a program to enter password by converting it to char array into string print the Output------------------------
#       Ex: Input : enter password
#           Output : Password : 123

a=input("Enter Password : ")

print("Password : "+ str(a))  #string concatination