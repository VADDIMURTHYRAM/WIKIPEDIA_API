#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
nltk.download('wordnet')


# In[2]:


wiki_wiki = wikipediaapi.Wikipedia('en')

page_py = wiki_wiki.page('Machine learning')


# In[3]:


print("Page exists :" ,page_py.exists())


# In[4]:


page_py.title


# In[5]:


page_py.fullurl


# In[6]:


page_py.summary


# In[7]:


data = page_py.text


# In[8]:


print('==' in data)
print('\n' in data) 


# In[9]:


data = data.replace('\n','')
data = data.replace('\\','')
data = re.sub(r'(?<=[.])(?=[^\s])',' ',data)
data = re.sub(r'[^\w\s\.]','', data)
#data = re.sub(r'(?=\d\d\d\d)',' ',data)
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
print(tokens_without_sw)


# In[12]:


data = ' '.join([str(item) for item in tokens_without_sw])
print(data)


# In[13]:


#stemming
'''from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
text_tokens_1 = nltk.word_tokenize(data)
for word in text_tokens_1:
    print(stemmer.stem(word))''' 
# stemming does bring the word to root but it causes overstemming and understemming so i prefered lemmatization


# In[14]:


#lemmatization 
data1 = []
lemmatizer=WordNetLemmatizer()
text_tokens_1 = word_tokenize(data)
for word in text_tokens_1:
    data1.append(lemmatizer.lemmatize(word))
data = ' '.join([str(item2) for item2 in data1])
data


# In[15]:


data1= NER(data)


# In[16]:


for word in data1.ents:
    print(word.text,word.label_)


# In[17]:


displacy.render(data1,style="ent",jupyter=True)


# In[ ]:




