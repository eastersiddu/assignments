#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Write a program to accept two numbers from the user and calculate multiplication,division
x=int(input("num1 : "))
y=int(input("num2 : "))
def multi(x,y):
    print("Multiplication : {}".format(x*y))
    print("Division : {}".format(x/y))
muldi(x,y)


# In[3]:


#2. Write a python program to print the characters from a string that are present at an even index
name=input()
n=""
for letters in range(0,len(name)):
    if letters%2==0:
        n+=name[letters]
print(n)


# In[4]:


#3. Write a python program to print the characters from a string that are present at an odd index
name=input()
n=""
for letters in range(0,len(name)):
    if letters%2!=0:
        n+=name[letters]
print(n)


# In[9]:


#4. Write a python program which will print the sum of the two numbers if the two numbers are even or it will print 
#the difference of two  numbers
num1=int(input("Number 1 : "))
num2=int(input("Number 2 : "))
if num1 and num2%2==0:
    print("Sum of {} and {} is {}".format(num1,num2,num1+num2))
else:
    print("Difference of {} and {} is {}".format(num1,num2,num1-num2))


# In[10]:


#5. Write a python program to convert all even indexed alphabets to upper and odd indexed char to lower
name=input("Type here : ")
new=""
for i in range(0,len(name)):
    if i%2==0:
        new+=name[i].upper()
    else:
        new+=name[i].lower()
print(new)


# In[2]:


#6. Write a python program which will print True if the input number is divisible by 5 or else False
num=int(input("Enter any number : "))
if num%5==0:
    print(True)
else:
    print(False)


# In[7]:


#7. Given two integer numbers return their product only if the product is greater than 1000, else return their sum
num1=int(input("Number 1 : "))
num2=int(input("Number 2 : "))
def pro(num1,num2):
    if num1*num2 >1000:
        return "The product of {} and {} is {}".format(num1,num2,num1*num2)
    else:
        return "The sum of {} and {} is {}".format(num1,num2,num1+num2)
pro(num1,num2)


# In[10]:


#8.Given two strings x, y writes a program to return a new string made of x and y’s first, middle, and last characters
#Example: Input X=” pytho” Y=” javas” Output ” pjtvos”
x=input()
y=input()
def slicing(x,y):
    ma=int(len(x)/2)
    mb=int(len(y)/2)
    print("\n")
    print(x[0]+y[0]+x[ma]+y[mb]+x[-1]+y[-1])
slicing(x,y)


# In[13]:


#9. Write a python program to take three names as input from a user in the single input () function call
name=input("enter your names here : ")
d=name.split()
for names in d:
    print(" {}".format(names))


# In[16]:


#10. Write a Python program to get a string from a given string where all occurrences of its first char have been
#changed to '@', except the first char itself
name=input("enter your names here : ")
a=name[0]
b=name[1:]
c=b.replace(a,"@")
print(a+c)


# In[19]:


#11. Write a Python program to add 'ing' at the end of a given string (string length should be equal to or more than 3)
#. If the given string already ends with 'ing' thenadd 'ly' instead. If the string length of the given string is less than 3, leave it
name=input("enter the string here : ")
if len(name)<3:
    print(name)
elif len(name)>=3:
    if name[-3:]=="ing":
        print(name.replace("ing","ly"))
    else:
        print(name+"ing")


# In[22]:


#12.Write a python program that accepts two inputs num1 and num2 print Trueif one of them is 10 or if their sum is 10 
#otherwise print False
num1=int(input("num1 : "))
num2=int(input("num2 : "))
if num1==10 or num2==10 or num1+num2==10:
      print(True)
else:
      print(False)


# In[23]:


#13. Write a python program that accepts three inputs x, y and z print True if x*y>z otherwise False
x=int(input())
y=int(input())
z=int(input())
if x*y>z:
    print(True)
else:
    print(False)


# In[25]:


#14. Write a python program that accepts two strings inputs return True depending on whether the total number of 
#characters in the first string is equal to the total number of characters in the second string
name1=input()
name2=input()
if len(string1)==len(string2):
    print(True)
else:
    print(False)


# In[27]:


#15. Write a python program that takes a string input, we'll say that the front is the firstthree characters of the
#string. If the string length is less than three characters, thefront is whatever is there. Return a new string, 
#which is three copies of the front
string=input()
if len(string)<3:
    print(string)
else:
    f=string[0:3]
print(f,f,f)


# In[30]:


#16write a python program that in world and determines wheathr or not it is plural.A plural word is one tht ends in"s"
word=input()
if word[-1]=="s" or word[-1]=="S":
    print("The given word {} is plural ".format(word)) 
else:
    print("The given word {} is not a plural ".format(word))


# In[34]:


#17. A bartender is writing a simple program to determine whether he should serve drinks to someone. He only serves 
#drinks to people 18 and older and when he's not on break (True means break and False means not a break time). 
##Given the person's age, and whether break time is in session, create a python program which prints whether he 
#should serve drinks or not.
name=input("Enter your :")
age=int(input("please provide your age : ")) 
print("provide bar tender is in break or not?")
b=input("type y or n:")
if b=="n" or b=="N":
    print("Bartender is not taking Break!")
    if age >=18:
        print("The bartender serves drink to {}".format(name)) 
    else:
        print("The bartender will not serves drink to {}".format(name)) 
    if b=="Y" or b=="y":
        print("The bartender serves drink to {}".format(name))


# 18.manoj kumar ha family and friends. help him remaid them who is who.given a string with a name,return the relation 
# of that person to manoj kumar.
# persion relation
# shiva father
# letha mother
# tarun brother

# In[40]:


person=input("Please enter your name : ")
data={"shiva":"Father","letha":"Mother","vasavi":"Sister","tarun":"Brother"} 
if person in data:
    print("{} is {} to Manoj Kumar.".format(person,data[person]))
else:
    relation=input("Please provide your relation with Manoj Kumar : ") 
    if relation!="friend" or relation!="Friend":
        data.update({person:relation})
        print("{} is {} to Manoj Kumar.".format(person,data[person])) 
    else:
        print("{} is friend to Manoj Kumar.".format(person))


# 19. Write a python program that takes a string, breaks it up and returns it with vowels first, consonants second. For any character that's not a vowel (like special characters or spaces), treat them like consonants

# In[42]:


string=input()
v=""
c=""
for letters in string:
    if letters in ["a","e","i","o","u","A","E","I","O","U"]: 
        v+=letters
    else: 
        c+=letters
print(v+c)


# In[ ]:




