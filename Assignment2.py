#question 1 (A)

len("python is a case sensitive language")

#question 1 (B)

s = 'Python is a case sensitive language' #initial string
reversed=''.join(reversed(s)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversed) #print the reversed string

#question 4

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
 
print("The largest number is",largest)

#question 5

s = "What is your name ?"
word = "Geeks"
 
if (isWordPresent(s, word)):
    print("Yes")
else:
    print("No")
