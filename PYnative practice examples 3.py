#!/usr/bin/env python
# coding: utf-8

# # Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# In[1]:


def first_last(lists):
    size = len(lists)
    if lists[0] == lists[size - 1]:
        return True
    else:
        return False


# In[2]:


first_last([1,2,3,4])


# In[3]:


first_last([1,2,3,4,5,1])


# # Iterate the given list of numbers and print only those numbers which are divisible by 5

# In[11]:


def div_5(lists):
    for i in lists:
        if i % 5 == 0:
            print(i)


# In[6]:


div_5([1,2,3,4,5])


# In[12]:


div_5([5,15,20,10,4])


# In[ ]:




