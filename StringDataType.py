#---1-----Write a Program to Reverse a String without using Reverse function----------------------------------------------------------------------- 
#           Ex: Enter a String : INDIA  
#               Reverse String is : AIDNA  

#------------------------------------BELLOW--CODE--IN---[python-Language]--------------------------------------------------------

string = input("Enter any String : " )

reverse=""
length_str=len(string)

for i in range(1,length_str+1):
    reverse = reverse + string[-i]

print(reverse)

#---2-----Write a program in C# Sharp to find the length of a string without using library function----------------------------------------------------
#           Ex: Input : Jalatechnologies
#               Output : 16

#------------------------------------BELLOW--CODE--IN---[python-Language]--------------------------------------------------------

string = input("Enter any String : " )

length_str=len(string)

print(length_str)

#---3-----Write a Program to calculate the length of the string using count function------------------------------------------------------------------- 
#           Ex: Given String: INDIA  
#               The Length of the First String is : 5  

#------------------------------------BELLOW--CODE--IN---[python-Language]--------------------------------------------------------

str = input("Enter a string: ")

counter = 0
for s in str:
      counter = counter+1
print("Length of the input string is:", counter)

#---4-----Write a Program to Replace String in String using Replace function-------------------------------------------------------------------------
#           Ex: Sentence Before Replacing : Sun Rises in the West  
#               Sentence After Replacing : Sun Rises in the East 

#------------------------------------BELLOW--CODE--IN---[python-Language]--------------------------------------------------------

sen = "Sun Rises in the West"

replace_sen = sen.replace("West","East")

print(replace_sen)
 

#---5-----Write a Program to Convert Upper case to Lower Case using LowerCase method--------------------------------------------------------------------  
#           Ex: Enter the String in Uppercase : JALA  
#               String in Lowercase :jala  

#------------------------------------BELLOW--CODE--IN---[python-Language]--------------------------------------------------------

str = input("Enter any string : ")

result = str.lower() 

print(result)

#---6-----Write a program in C# Sharp to find maximum occurring character in a string--------------------------------------------------------------------
#           Ex: Input string : Welcome to india
#               Output : The highest frequency of the character 'a' appear as 1 time

#------------------------------------BELLOW--CODE--IN---[python-Language]--------------------------------------------------------

test_str = "jalatechnologies"
  
print ("The original string is : " + test_str)
  
tuple = {}
for i in test_str:
    if i in tuple:
        tuple[i] += 1
    else:
        tuple[i] = 1
res = max(tuple, key = tuple.get) 
  
print ("The maximum of all characters in jalatechnologies is : " + str(res))


#---7-----Write a program in C# Sharp to sort a string array in ascending order.--------------------------------------------------------------------
#           Ex: Input string : this is a string
#               Output : After sorting the string appears like : a g h i i i n r s s s t t

#------------------------------------BELLOW--CODE--IN---[python-Language]--------------------------------------------------------

str = input("Enter any string : ")

result = ''.join(sorted(str))

print("String after sorting : " + result)
