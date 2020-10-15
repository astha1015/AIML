#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt


# In[12]:


df = pd.read_csv('./full_data.csv')
new=df.loc[df['location'] == 'United States Virgin Islands'].dropna()
new = pd.DataFrame(new,columns=['date','total_cases','total_deaths'])
new


# In[13]:


fig, ax = plt.subplots()

new.plot(kind='line',x='date',y='total_cases',ax=ax)
new.plot(kind='line',x='date',y='total_deaths', color='red', ax=ax)

ax.xaxis_date()     # interpret the x-axis values as dates
fig.autofmt_xdate() # make space for and rotate the x-axis tick labels
plt.title('Total Corona Cases and Deaths until Oct 14, 2020 in United States')
plt.show()


# In[6]:


get_ipython().system('pip install plotly')
get_ipython().system('pip install pycountry-convert')


# In[14]:


df = pd.read_csv('./full_data.csv').dropna()
new=df.loc[df['date'] == '2020-10-14']
df = pd.DataFrame(new,columns=['location','total_cases','total_deaths'])

#function to convert to alpah2 country codes and continents
from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha3
def get_continent(col):
    try:
        cn_a2_code =  country_name_to_country_alpha3(col)
    except:
        cn_a2_code = 'Unknown' 
    return (cn_a2_code)
country_code = []
for country in df['location']:
  country_code.append(get_continent(country))
print(country_code)


# In[10]:


import plotly.graph_objs as go #importing graphical objects

df['country_code'] = country_code

df = pd.DataFrame(df,columns=['location','total_cases','total_deaths', 'country_code'])


data = dict(type = 'choropleth', locations = df['country_code'], z = df['total_cases'], text = df ['location'], colorbar = {'title' : 'Corona cases Worldwide'})
layout = dict(title = 'Total number of Corona cases around the world', geo = dict(showframe = False, projection = {'type':'natural earth'}))

worldmap = go.Figure(data = [data],layout = layout)
worldmap.show()


# In[ ]:




