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


st.set_page_config(layout = "wide", page_title="Bundesliga Data Dashboard")

df=pd.read_excel("blPlayersAll23.xlsm", sheet_name="blplayers2023")

ALL = 'TODOS'
def unique_sorted_values_plus_ALL(array):
    unique = array.unique().tolist()
    unique.sort()
    unique.insert(0, ALL)
    return unique


def common_filtering():
        if (dropdown_club == ALL) & (dropdown_player == ALL):
            dropdown_player.options = unique_sorted_values_plus_ALL(df.Jugador)
            #dropdown_player = widgets.Dropdown(options = unique_sorted_values_plus_ALL(df.Jugador))
            common_filter = df
        elif (dropdown_club == ALL):
            dropdown_player.options = unique_sorted_values_plus_ALL(df.Jugador)
            #dropdown_player = widgets.Dropdown(options = unique_sorted_values_plus_ALL(df.Jugador))
            common_filter = df[df.Jugador == player]
        elif (dropdown_player == ALL):
            if(dropdown_club ==ALL):
                dropdown_player.options = unique_sorted_values_plus_ALL(df.Jugador)
            else:
                df1=df[df.Club == club]
                dropdown_player.options = unique_sorted_values_plus_ALL(df1.Jugador)
            #dropdown_player = widgets.Dropdown(options = unique_sorted_values_plus_ALL(df.Jugador))
            common_filter = df[df.Club == club]
        else:
            if(dropdown_club != ALL):
                df1=df[df.Club == club]
                dropdown_player.options = unique_sorted_values_plus_ALL(df1.Jugador)
                #dropdown_player = widgets.Dropdown(options = unique_sorted_values_plus_ALL(df1.Jugador))
                common_filter = df[df.Jugador == player]
        return common_filter


#dropdown_club
dropdown_club = st.sidebar.selectbox(label="Seleccione el club: ", options =    unique_sorted_values_plus_ALL(df.Club), key="club")
#dropdown_player = st.sidebar.selectbox(label="Seleccione el Jugador: ", options =    unique_sorted_values_plus_ALL(df.Jugador), key="player")

optionsfull=unique_sorted_values_plus_ALL(df.Club)
optionsclub=unique_sorted_values_plus_ALL(df.Jugador)

if st.session_state['club']==ALL:
    dropdown_player = st.sidebar.selectbox(label="Seleccione el Jugador: ", options =    unique_sorted_values_plus_ALL(df.Jugador))
else:
    df1=df[df.Club==st.session_state['club']]
    dropdown_player = st.sidebar.selectbox(label="Seleccione el Jugador: ", options =    unique_sorted_values_plus_ALL(df1.Jugador), key='player')


with st.container():
    
    if dropdown_club == ALL:
        if dropdown_player==ALL:
            st.write(df)
        else:
            st.write(df[df['Jugador']==dropdown_player])
    else:
        if dropdown_player==ALL:
            st.write(df[df['Club']==dropdown_club])
        else:
            
            st.write(df[(df['Club']==dropdown_club) & (df['Jugador']==dropdown_player)])
