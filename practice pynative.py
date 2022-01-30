#!/usr/bin/env python
# coding: utf-8

# # Given two integer numbers return their product only if the product is greater than 1000, else return their sum

# In[4]:


def product_sum(num1,num2):
    product = num1 * num2
    if product > 1000:
        return product
    else:
        return num1 + num2


# In[5]:


result = product_sum(50,20)
print(result)


# In[6]:


result = product_sum(10,20)
print(result)


# In[7]:


result = product_sum(80,20)
print(result)


# # Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number

# In[19]:


x = range(10)
for i in x:
    print(f'Current number is {i} Previous number is {i-1} Next Number is {i + 1}')
    i = i + 1
    


# In[ ]:




