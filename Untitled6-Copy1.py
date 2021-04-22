#!/usr/bin/env python
# coding: utf-8

# In[1]:


age = input('Are you a cigarette addict older than 75 years old? ')

chronic = input('Do you have a severe chronic disease? ')

immune = input('Is your immune system too weak? ')

if age.title() == "No" and chronic.title() == 'No' or immune.title() == 'No':

    print('You are not in risky group')

else:

    print('You are in risky group')

