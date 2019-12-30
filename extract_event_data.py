#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json


# In[ ]:


def extract_event_data (event_data):
    keys =[]
    for i in event_data:
        loaded_json=json.loads(i)
        for j in list(loaded_json.keys()):
            if j not in keys:
                keys.append(j)
    json_df=pd.DataFrame(index=range(1,event_data.shape[0]+1),columns=keys)
    p=1
    for i in event_data:
        lj=json.loads(i)
        for j in list(lj.keys()):
            check_add(j,json_df,lj[j],p)
    p=p+1
    return json_df


# In[ ]:


def check_add(k,df,val,ind):
    for i in df.columns:
        if k == i:
            df[i][ind]=val
    return df

