#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


url='https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population'


# In[3]:


Headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}


# In[4]:


webpage=requests.get(url,headers=Headers)


# In[5]:


webpage


# In[6]:


soup=BeautifulSoup(webpage.text,'html')


# In[7]:


print(soup)


# In[8]:


soup.find_all('table')


# In[9]:


soup.find('table',class_='sortable wikitable sticky-header static-row-numbers col1left col4left')


# In[10]:


table=soup.find_all('table')[1]
print(table)


# In[11]:


soup.find_all('th')


# In[12]:


world_titles=table.find_all('th')


# In[13]:


world_titles


# In[14]:


len(world_titles)


# In[15]:


world_table_titles=[title.text.strip() for title in world_titles]
print(world_table_titles)


# In[16]:


df=pd.DataFrame(columns=world_table_titles)
df


# In[17]:


column_data=table.find_all('tr')


# In[18]:


for row in column_data[2:]:
    print(row.find_all('td'))


# In[19]:


for row in column_data[2:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    print(individual_row_data)


# In[23]:


for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    #print(individual_row_data)
    length=len(df)
    df.loc[length]=individual_row_data


# In[24]:


df


# In[26]:


df.to_csv(r'D:\Data Analyst\Project\City_Wise_Population\City_wise_population.csv',index=False)


# In[ ]:




