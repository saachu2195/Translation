#!/usr/bin/env python
# coding: utf-8

# In[91]:


## Installing the required libraries using pip.
get_ipython().system('pip install googletrans')

## Importing the required libraries.
from googletrans import Translator
import pandas as pd
import csv
     


# In[ ]:


## Defining function for translation the word from one language to another.

def translate():
    word = input("Please Enter your word : ")
    dest_lang = input("Please Enter your required language : ")
    output = translator.translate(word, dest=dest_lang) 
    return output.text 


# In[35]:


## Running the function

translate()


# ### Using Excel Doc 

# In[93]:


## Getting the file from Desktop.

file = pd.read_excel('C:/Users/square/Desktop/Words.xlsx')
file


# In[94]:


## Writing the function to translate the each elements in a columns

translator = Translator()
translation = {}
re_lang = input("Please Enter your required language : ")

## Checking for the unique elements in file.
for columns in file:
    unique_element = file[columns].unique()
    print(unique_element)
    
    ## Translation of word
    for unique_data in unique_element:
        translation[unique_data] = translator.translate(unique_data, dest = re_lang).text    
        
## Viewing         
translation    


# In[97]:


## Convertin the dictationary into dataframe.

df = pd.DataFrame(translation, index= [0])
df.transpose()


# In[ ]:




