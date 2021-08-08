#---1-----Write a C# Sharp program to check whether a given number is positive or negative---------------------------------------------------------------
#            Ex:
#                Input  :14
#                Output :14 is a positive number

#------------------------------------BELLOW--CODE--IN---[python-Language]--------------------------------------------------------

num= int(input("Enter any Integer : "))

if (num > 0):
    print("Given Number is Positive : ")
else :
    print("Given Number is Negative : ")

#---2-----Write a C# Sharp program to find whether a given year is a leap year or not---------------------------------------------------------------
#            Ex:
#               Input :  2016
#               Output : 2016 is leap year

year = int(input("Enter any Year : "))

if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print(str(year) + " Year is a Leap Year") 
else:
    print(str(year) + " Year is Not Leap Year")

#---3-----Write a C# Sharp program to check whether an alphabet is a vowel or consonant-------------------------------------------------------------
#            Ex:
#               Input : enter any alphabet : k
#               Output : The alphabet is a consonant.

alpha = input("Enter any Alphabet : ")

if (alpha == "a" or alpha == "A" or alpha == "e" or alpha == "E" or alpha == "i" or alpha == "I" or alpha == "o" or alpha == "O" or alpha == "u" or alpha == "U"):
    print("Given Alphabet is a Vowel.")
else : 
    print("Given Alphabet is a Consonant.")