#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data = pd.read_csv("tracks.csv")


# In[3]:


data.head(5)


# In[4]:


data.shape


# In[5]:


pd.isnull(data).sum()


# In[6]:


data.info()


# In[7]:


least_popular_song = data.sort_values('popularity') #by default it's in ascending order so don't need to mention it
least_popular_song.head(10)


# In[8]:


data.describe().transpose()


# In[9]:


most_popular_song=data.query('popularity>90', inplace=False).sort_values('popularity',ascending=False)
most_popular_song.head(10)


# In[10]:


data.set_index('release_date', inplace=True)
data.index = pd.to_datetime(data.index)
data.head()


# In[11]:


data[['artists']].iloc[18] #to check any specific position of specific column


# In[12]:


#To convert duration_ms into second
data['duration']=data['duration_ms'].apply(lambda x: round(x/1000))
data.drop('duration_ms', inplace= True, axis=1)
data.head()


# In[13]:


#To check correlation & avoid some unnecesary columns

corr_data=data.drop(['key','mode','explicit'], axis=1).corr(method='pearson')
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_data,fmt='.1g',annot=True,vmin=1,vmax=1,center=0,linecolor='black',linewidths=1,cmap='crest')
heatmap.set_title('Correlation heatmap among variables')
heatmap.set_xticklabels(heatmap.get_xticklabels(),rotation=90)


# In[14]:


sample_data = data.sample(int(0.004*len(data)))
print(len(sample_data))


# In[15]:


plt.figure(figsize=(10,6))
sns.regplot(data=sample_data,y='loudness',x='energy',).set_title('Loudness vs Energy relation')


# In[16]:


plt.figure(figsize=(10,6))
sns.regplot(data=sample_data,y='danceability',x='valence',color='b').set_title('danceability vs valence correlation')


# In[17]:


data['dates']=data.index.get_level_values('release_date')
data.dates=pd.to_datetime(data.dates)
years=data.dates.dt.year


# In[18]:


sns.displot(data=years,kind='hist').set(title='Number of songs per year')


# In[19]:


total_duration=data.duration
fig, ax=plt.subplots(figsize=(18,7))
fig=sns.barplot(x=years,y=total_duration).set(title='Songs duration over past years')
plt.xticks(rotation=90)
plt.tight_layout()


# In[ ]:


total_duration=data.duration
fig, ax=plt.subplots(figsize=(18,7))
fig=sns.lineplot(x=years,y=total_duration).set(title='Songs duration over past years')
plt.xticks(rotation=90)
plt.tight_layout()


# In[21]:


data_g= pd.read_csv('genre.csv')
data_g.head()


# In[28]:


sns.barplot(data=data_g,x='duration_ms',y='genre', errcolor=".2", edgecolor=".2").set(title='Songs duration with different genre')
plt.xlabel('duration in mili second')
plt.ylabel('Genre')
sns.color_palette('colorblind',as_cmap=True)
plt.tight_layout()


# In[31]:


plt.figure(figsize=(10,4))
popular=data_g.sort_values(by='popularity',ascending=False).head(10)
sns.barplot(data=popular,x='popularity',y='genre').set(title='Top 5 genres by popularity')


# In[ ]:




