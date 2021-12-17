#!/usr/bin/env python
# coding: utf-8

# In[46]:


from collections import Counter

import matplotlib.pyplot as plt
import numpy as np


# In[ ]:





# In[2]:


# read the file
text = open("/Users/Krish/PycharmProjects/lithum/venv/job.txt", "r")

data = text.read()
data = data.lower()
text.close()


# In[3]:


print(data)


# In[11]:


tokenized = data.split()

clean_tokenized = tokenized

chaps = []
curr_chap = 1

for i in range(len(clean_tokenized)):
    old_str = clean_tokenized[i]
    new_str = ''
    
    first = old_str.split(":")[0]
    # print(first)
    if first.isnumeric() and int(first) == curr_chap:
        chaps.append(i)
        curr_chap+=1
    
    for j in range(len(old_str)):
        curr = old_str[j]
        
        if curr.isalpha() or curr == '\'':
            new_str += old_str[j]
    clean_tokenized[i] = new_str
    
chaps.append(len(clean_tokenized))
# print("chaps: ", chaps, "length: ", len(chaps))
# print("clean_tokenized: ", clean_tokenized)


# In[12]:


map = Counter(clean_tokenized)
# print(map)


# In[ ]:





# In[24]:


def temporal_occurrences(chaps, word):
    occur = []
    
    for i in range(len(clean_tokenized)):
        if clean_tokenized[i] == word:
            occur.append(i)
    
    for i in range(len(occur)):
        chap_found = -1
        for j in range(len(chaps)):
            if occur[i] < chaps[j]:
                chap_found = j-1
                break
        
        offset = occur[i] - chaps[chap_found]
        total = chaps[chap_found+1] - chaps[chap_found]
        occur[i] = chap_found + (offset/total)
 
    return occur


# In[42]:


def graph(chaps, word):
    oc = temporal_occurrences(chaps, word)
    print(oc)
    
    length = len(oc)
    x = list(range(length))
    # print(x)
    
    plt.title("Temporal analysis of \'{}\' in The Book of Job".format(word))
    plt.ylim([1, len(chaps)])
    plt.xlabel("Occurrence #")
    plt.ylabel("Chapter Temporal Occurrence")
    plt.scatter(x, oc)


# In[60]:


def line_graph(chaps, word):
    oc = temporal_occurrences(chaps, word)
    # print(oc)
    
    length = len(oc)
    x = list(range(length))
    # print(x)
    
    plt.title("Temporal analysis of \'{}\' in The Book of Job".format(word))
    # plt.ylim([1, len(chaps)])
    plt.xlabel("Chapter Temporal Occurrence")
    plt.ylabel("# of Occurrences")
    plt.scatter(oc, np.ones(len(oc)))
    plt.show()


# In[62]:


line_graph(chaps, "mouth")


# In[ ]:




