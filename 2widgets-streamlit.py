#!/usr/bin/env python
# coding: utf-8

# In[4]:


#install matplotlib


# In[7]:


import pandas as pd
#import ipywidgets as widgets
#import seaborn as sns
#import matplotlib.pyplot as plt
#from IPython.display import display
import streamlit as st
import plotly as plt


# In[37]:


st.set_page_config(layout = "wide", page_title="Bundesliga Data Dashboard")


# In[38]:


df=pd.read_excel("blPlayersAll23.xlsm", sheet_name="blplayers2023")

ALL = 'TODOS'
def unique_sorted_values_plus_ALL(array):
    unique = array.unique().tolist()
    unique.sort()
    unique.insert(0, ALL)
    return unique


# In[41]:

def common_filtering(club):
    df1=df[df.Club == club]
    selbox2 = st.sidebar.selectbox(label="Seleccione el Jugador: ", options =    unique_sorted_values_plus_ALL(df1.Jugador)

dropdown_club = st.sidebar.selectbox(label="Seleccione el club: ", options =    unique_sorted_values_plus_ALL(df.Club), on_change=common_filter)
#dropdown_club

dropdown_player = st.sidebar.selectbox(label="Seleccione el Jugador: ", options =    unique_sorted_values_plus_ALL(df.Jugador))

    

# In[18]:


def dropdown_club_eventhandler(change):
    common_filtering(change.new, dropdown_player.value)
def dropdown_player_eventhandler(change):
    common_filtering(dropdown_club.value, change.new)


# In[46]:


#dropdown_club.observe(
#dropdown_club_eventhandler, names='value')
#dropdown_player.observe(
#dropdown_player_eventhandler, names='value')

#l=widgets.link((dropdown_club, 'value'), (dropdown_player, 'value'))



# In[47]:


#display(dropdown_club)
#display(dropdown_player)


# In[21]:


#display(output)


# In[22]:


#input_widgets=widgets.HBox([dropdown_club, dropdown_player])
#display(input_widgets)


# In[23]:


#tab=widgets.Tab([output])
#tab.set_title(0, 'Datos Bundesliga')
#display(tab)


# In[24]:


#dashboard=widgets.VBox([input_widgets, tab])
#display(dashboard)


# In[ ]:




