#---1-----Declare a value as int datatype and print in the output--------------------------------------------------------

number = int(input("Enter any Integer Value : ")) #integer type

print(number)

#---2-----Write a program in boolean type and print in console---------------------------------------------------------

boolean = bool("Enter any Boolean Value : ") #boolean type

print(boolean)

#---3-----Write a program on converting Float to Decimal type and print in console--------------------------------------



#---4-----Write a C# Sharp program that takes two numbers as input and perform an operation (+,-,*,x,/) on them and displays the result of that operation.
#           Ex: Input : first number: 20, second number: 12
#               Output : 20-12 = 8

#------------------------------------BELLOW--CODE--IN---[python-Language]--------------------------------------------------------
 
firstNum = int(input("Enter First Num : "))
secondNum = int(input("Enter Second Num : "))

result_1 = firstNum + secondNum 
result_2 = firstNum - secondNum
result_3 = firstNum * secondNum 
result_4 = firstNum / secondNum




print("Addition of Given Two Num : " + str(result_1))
print("Subtraction of Given Two Num : " + str(result_2))
print("Multiplication of Given Two Num : " + str(result_3))
print("Division of Given Two Num : " + str(result_4))

#---5-----Write a C# Sharp program that takes three letters as input and display them in Reverse Order.
#           Ex: Input: Enter letter: b Enter letter: a Enter letter: t
#               Output : t a b

#------------------------------------BELLOW--CODE--IN---[python-Language]--------------------------------------------------------

a = input("Enter Letter 1 : ")
b = input("Enter Letter 2 : ")
c = input("Enter Letter 3 : ")

print(c,b,a)


#---6-----Write a C# Sharp program that takes a character as input and check the input (lowercase) is a vowel, a digit, or any other symbol.
#           Ex: Input : symbol : a
#               Output : It is a lowercase vowel

#------------------------------------BELLOW--CODE--IN---[python-Language]--------------------------------------------------------

character = input("Enter Any Charecter : ") 

if (character.isdigit()):
    print("It is a Digit")
elif (character.islower()) and (character == "a" or character == "e" or character == "i" or character == "o" or character == "u"):
    print("It is a lowercase vowel") 
else:
    print("It is a symbol")
