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


dropdown_club = st.sidebar.selectbox(label="Seleccione el club: ", options =    unique_sorted_values_plus_ALL(df.Club))
#dropdown_club

dropdown_player = st.sidebar.selectbox(label="Seleccione el Jugador: ", options =    unique_sorted_values_plus_ALL(df.Jugador))

def common_filtering(club, player):
    output.clear_output()
    
    if (club == ALL) & (player == ALL):
        dropdown_player.options = unique_sorted_values_plus_ALL(df.Jugador)
        #dropdown_player = widgets.Dropdown(options = unique_sorted_values_plus_ALL(df.Jugador))
        common_filter = df
    elif (club == ALL):
        dropdown_player.options = unique_sorted_values_plus_ALL(df.Jugador)
        #dropdown_player = widgets.Dropdown(options = unique_sorted_values_plus_ALL(df.Jugador))
        common_filter = df[df.Jugador == player]
    elif (player == ALL):
        if(club ==ALL):
            dropdown_player.options = unique_sorted_values_plus_ALL(df.Jugador)
        else:
            df1=df[df.Club == club]
            dropdown_player.options = unique_sorted_values_plus_ALL(df1.Jugador)
        #dropdown_player = widgets.Dropdown(options = unique_sorted_values_plus_ALL(df.Jugador))
        common_filter = df[df.Club == club]
    else:
        if(club != ALL):
            df1=df[df.Club == club]
            dropdown_player.options = unique_sorted_values_plus_ALL(df1.Jugador)
            #dropdown_player = widgets.Dropdown(options = unique_sorted_values_plus_ALL(df1.Jugador))
            common_filter = df[df.Jugador == player]
    
    with output:
        return (common_filter)


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




