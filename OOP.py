#!/usr/bin/env python
# coding: utf-8

# In[11]:


class prntCls:
    def __init__(self):
        self.val1 = self.val2 = 1
    def sum(self):
        return self.val1 + self.val2


# In[12]:


obj = prntCls()
print(obj.sum())


# In[13]:


class chldCls(prntCls):
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2


# In[17]:


obj2 = chldCls(2,3)
print(obj2.sum())


# In[ ]:




