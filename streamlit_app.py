#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import wikipediaapi
import wikipedia
import json
import re
import scrapy
import spacy
from spacy import displacy
#python -m spacy download en
import string
import unidecode
import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer


# In[3]:


wiki_wiki = wikipediaapi.Wikipedia('en')

page_py = wiki_wiki.page('Artificial intelligence')


# In[4]:


print("Page exists :" ,page_py.exists())


# In[5]:


page_py.title


# In[6]:


page_py.fullurl


# In[7]:


page_py.summary


# In[8]:


data = page_py.text


# In[9]:


#text preprocessing
data = data.replace('\n','')
data = data.replace('\\','')
data = re.sub(r'(?<=[.])(?=[^\s])',' ',data)
data = re.sub(r'[^\w\s\.]','', data)
data = unidecode.unidecode(data)


# In[10]:


data


# In[11]:


NER = spacy.load("en_core_web_sm")

#tokenizing the text
text_tokens = word_tokenize(data)

#removing stopping words from the original data
all_stopwords = NER.Defaults.stop_words
tokens_without_sw= [word for word in text_tokens if not word in all_stopwords]
data = ' '.join([str(item) for item in tokens_without_sw])
print(data)


# In[12]:


# stemming does bring the word to root but it causes overstemming and understemming so i prefered lemmatization

#lemmatization 
data1 = []
lemmatizer=WordNetLemmatizer()
text_tokens_1 = word_tokenize(data)
for word in text_tokens_1:
    data1.append(lemmatizer.lemmatize(word))
data = ' '.join([str(item) for item in data1])
data


# In[13]:


#Named Entity recognition
data1= NER(data)
for word in data1.ents:
    print(word.text,word.label_)


# In[14]:


displacy.render(data1,style="ent",jupyter=True)


# In[ ]:




