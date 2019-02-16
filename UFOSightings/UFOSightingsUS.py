
# coding: utf-8

# In[29]:


import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode()


# In[7]:


complete_data = pd.read_csv("complete.csv", usecols=[0, 1, 2, 9, 10], low_memory=False)
scrubbed_data = pd.read_csv("scrubbed.csv", usecols=[0, 1, 2, 9, 10], low_memory=False)


# In[8]:


complete_data.describe()


# In[9]:


complete_data


# In[10]:


complete_data['datetime'] = pd.to_datetime(complete_data['datetime'], errors='coerce')


# In[12]:


complete_data['datetime']


# In[13]:


complete_data.insert(1, 'year', complete_data['datetime'].dt.year)


# In[14]:


complete_data


# In[16]:


complete_data['year'] = complete_data['year'].fillna(0).astype(int)


# In[17]:


complete_data['city'] = complete_data['city'].str.title()


# In[18]:


complete_data


# In[19]:


complete_data['state'] = complete_data['state'].str.upper()


# In[20]:


complete_data['latitude'] = pd.to_numeric(complete_data['latitude'], errors='coerce')


# In[21]:


complete_data = complete_data.rename(columns={'longitude ':'longitude'})


# In[22]:


complete_data


# In[27]:


us_states = np.asarray(['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
                        'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
                        'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
                        'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
                        'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'])


# In[28]:


us_states


# In[31]:


complete_data = complete_data[complete_data['state'].isin(us_states)].sort_values('year')


# complete_data

# In[32]:


complete_data


# In[33]:


complete_data = complete_data[(complete_data.latitude > 15) & (complete_data.longitude < -65)]
complete_data = complete_data[(complete_data.latitude > 50) & (complete_data.longitude > -125) == False]
complete_data = complete_data[complete_data['city'].str.contains('\(Canada\)|\(Mexico\)') == False]


# In[34]:


complete_data


# In[36]:


complete_data['text'] = complete_data[complete_data.year > 0]['datetime'].dt.strftime('%B %-d, %Y')


# In[37]:


complete_data


# In[38]:


data = [dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = complete_data[complete_data.year > 0]['longitude'],
        lat = complete_data[complete_data.year > 0]['latitude'],
        text = complete_data[complete_data.year > 0]['text'],
        mode = 'markers',
        marker = dict(
            size = 5.5,
            opacity = 0.75,
            color = 'rgb(0, 163, 81)',
            line = dict(color = 'rgb(255, 255, 255)', width = 1))
        )]


# In[39]:


data


# In[41]:


layout = dict(
         title = 'UFO Reports by Latitude/Longitude in United States (1910-2014)',
         geo = dict(
             scope = 'usa',
             projection = dict(type = 'albers usa'),
             showland = True,
             landcolor = 'rgb(250, 250, 250)',
             subunitwidth = 1,
             subunitcolor = 'rgb(217, 217, 217)',
             countrywidth = 1,
             countrycolor = 'rgb(217, 217, 217)',
             showlakes = True,
             lakecolor = 'rgb(255, 255, 255)')
        )


# In[43]:


figure = dict(data = data, layout = layout)
iplot(figure)

