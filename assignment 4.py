#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1. Define a function which will return Max of three numbers

def max(a,b,c):
    m=0
    for y in (a,b,c):
        if y>m:
            m=y
    return m


# In[6]:


max(20,30,40)


# In[19]:


def max(a,b,c):
    m=0
    for g in (a,b,c):
        if g>m:
            m=g
    return m
        


# In[20]:


max(100,200,300)


# In[25]:


#2. Define a Python Function to reverse a string.

def reverse(s):
    l=list(s)
    l.reverse()
    s1=" ".join(l)
    return s1


# In[26]:


reverse("Innomatics")


# In[4]:


#3. Write a Python program to define a function that accepts 2 values and return its sum, subtraction and multiplication.

def val(a,b):
    return a+b,a-b,a*b


# In[5]:


val(2,3)


# In[13]:


#4.Define a function that accepts roll number and returns whether the student is present or 
#absent.
students_info={1:"easter",2:"keerthi",3:"Ameem",4:"rajesh",5:"Manoj",6:"Bhagya"} 
def attendance(*rollnum):
    keys=students_info.keys() 
    for num in keys:
        if num in rollnum:
            print("{} is present".format(students_info[num]))
        else:
            print("{} is abscent".format(students_info[num]))


# In[15]:


attendance(1,2,3,5)


# In[17]:


#5. Define a function in python that accepts n values and returns the maximum of n numbers
def maxi(*num):
    return "Max num : {}".format(max(num))


# In[18]:


maxi(1,2,3,4,5,6,8,77,65,45,78.1,99.2)


# In[23]:


#6. Define a function which counts vowels and consonant in a word.
def syllable(s): 
    vowels=["A","E","I","O","U","a","e","i","o","u"] 
    v=0
    c=0
    for letters in s:
        if letters in vowels:
            v+=1 
        else:
            c+=1
    print("Total vowels in given string = {}".format(v))
    print("Total consonants in given string = {}".format(c))


# In[24]:


syllable("udtfzjagutrweujvfdahjfuaiukshduwtuafgvbs")


# In[27]:


#7. Define a function that returns Factorial of a number
def factorial(num): 
    f=1
    for num in range(1,num+1): 
        f*=num
    return f


# In[31]:


factorial(6)


# In[34]:


#8. Define a function that accepts radius and returns the area of a circle.
def area(rad):
    pi=22/7
    return pi*(rad**2)


# In[37]:


area(8)


# In[40]:


#9. Define a function that takes a number as a parameter and check the number is prime or not.
def checkPrime(num):
    if num==2 or num==3:
        return "{} is a prime number".format(num) 
    for i in range(2,num-1):
        if num%i!=0:
            return "{} is a prime number".format(num)
        else:
            return "The give number {} is not a prime number".format(num)


# In[48]:


checkPrime(987)


# In[51]:


checkPrime(70)


# In[68]:


#10. Mary wants to run a 25-mile marathon. When she attempts to sign up for the marathon, she notices the sign-up 
#sheet doesn't directly state the marathon's length. Instead, the marathon's length is listed in small, different 
#portions. Help Mary find out how long the marathon actually is.
def marathon_distance(l):
    positive=[]
    if l==[]: 
        return False
    for num in l: 
        if num<0:
            num=num*(-1)
            positive.append(num) 
        else:
            positive.append(num) 
    if sum(positive)==25:
        return True 
    else:
        return False
        


# In[69]:


marathon_distance([1, 2, 3, 4])


# In[70]:


marathon_distance([1, 9, 5, 8, 2])


# In[73]:


marathon_distance([-6, 15, 4])


# In[76]:


#11. Create a function that takes a number and returns True if the number is automorphic, False if it isn't.
def automorphic_check(n):
    a=n**2
    b=str(a)
    if int(b[-1])==n:
        return True 
    else:
        return False


# In[77]:


automorphic_check(2)


# In[78]:


automorphic_check(6)


# In[85]:


#12) Create a function, that will take given a, b, c, and do the following:
#Add a to itself b times and Check if the result is divisible by c. and return true if it is divisible by c or false
def check(a,b,c):
    new=[]
    for num in range(b): 
        new.append(a)
    if sum(new)%c==0:
        return True 
    else:
        return False


# In[86]:


check(1,2,3)


# In[87]:


check(1,2,2)


# In[92]:


#13) Create a function that changes specific words into emoticons. Given a sentence as a string, replace the 
#words smile, grin, sad and mad with their corresponding emoticons
def emotions(s): 
    sep=s.split()
    dic={"smile":":D","grin":":)","sad":":(","mad":":P"} 
    keys=dic.keys()
    for items in sep:
        if items in keys: 
            change=s.replace(items,dic[items]) 
            print(change)


# In[94]:


emotions("i am sad")


# In[95]:


emotions("I am mad at you")


# In[96]:


emotions("She had a big grin on her face")


# In[97]:


emotions("I smile when I was with you")


# In[100]:


#14) Write a Python program to square and cube every number in a given list of integers using Lambda
li=[4,2]
x=list(map(lambda x:x**2,li)) 
y=list(map(lambda y:y**3,li)) 
print("Squares : {}".format(x))
print("Cubes : {}".format(y))


# In[102]:


#15) Write a Python program to check whether a given string is number or not using Lambda
check=lambda s:s.isdigit() 
check("333")


# In[ ]:




