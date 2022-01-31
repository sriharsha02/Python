#!/usr/bin/env python
# coding: utf-8

# # Write a program to accept a string from the user and display characters that are present at an even index number

# In[3]:


word = input("Enter the string: ")
print('Old String is : ', word)
x = list(word)
for i in x[0::2]:
    print(i)


# # Write a program to remove characters from a string starting from zero up to n and return a new string.

# In[5]:


def char_rem(word, n):
    print('Original String: ', word)
    x = word[n:]
    return x


# In[7]:


print(char_rem('harsha',2))
print(char_rem('sriharshaakshintala',4))


# In[ ]:




