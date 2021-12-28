#!/usr/bin/env python
# coding: utf-8

# In[1]:


# What is Python Programming?
    # Python is a high level prog lang.
    # Python is an interpreted prog lang.
    # case sensitive
        # NAME and name --> Different
    # python is an object oriented language.
    


# In[2]:


# Why Python?
    # Simple to learn.
    # Easy and short syntax.
    # Lots of libraries.(Set of code)
    # Platform Independent(Code can be run in any type of OS)
        # This is one of the main functionaity of Python.
    # Great community Support.


# In[3]:


print("My name is Sri Harsha")


# In[4]:


print(2+2)


# In[5]:


print(2+2*6)


# # Variables

# In[6]:


# Variable is a sort of container used to store data values.


# In[7]:


name = "Sri Harsha"
print(name)


# In[11]:


# Static Allocation
num1 = 5
num2 = 10
sum = num1 + num2
print(sum)


# In[12]:


num1,num2,num3,num4 = 10,20,30,40
print(num1,num2,num3,num4)


# In[13]:


# Dynamic Allocation of values
num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
sum = num1 + num2
print(sum)


# In[14]:


# Dynamic Allocation of values
num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
sum = num1 + num2
print(sum)


# # Data Types in Python
# 

# In[15]:


# We can store different forms of data 
    # int
    # float (decimal)
    # string
    # boolean(True/False)
    # complex(combination of real +imaginary number--> a+ib)


# In[16]:


a = 15
print(type(a))


# In[17]:


name = "Harsha"
print(type(name))


# In[18]:


num1 = 10.02
print(type(num1))


# In[20]:


a = 4
b = 10
print(a>b)
print(a<b)


# In[21]:


number = 60 + 70j
print(type(number))

