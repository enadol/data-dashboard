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


st.set_page_config(layout = "wide", page_title="Bundesliga Data Dashboard - Torneo 2022/2023")

df=pd.read_excel("blPlayersAll23.xlsm", sheet_name="blplayers2023")
    
cell_hover = {
    "selector": "td:hover",
    "props": [("background-color", "#FFFFE0")]
    }
index_names = {
    "selector": ".index_name",
    "props": "font-style: italic; color: darkgrey; font-weight:normal;"
    }
headers = {
    "selector": "th:not(.index_name)",
    "props": "background-color: #800000; color: white; text-align: center"
}

properties = {"border": "1px solid black", "width": "65px", "text-align": "center"}

df.style.set_table_styles([cell_hover, index_names, headers]).set_properties(**properties)

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
                df1.style.set_table_styles([cell_hover, index_names, headers])
                dropdown_player.options = unique_sorted_values_plus_ALL(df1.Jugador)
                #dropdown_player = widgets.Dropdown(options = unique_sorted_values_plus_ALL(df1.Jugador))
                common_filter = df[df.Jugador == player]
        common_filter.style.set_table_styles([cell_hover, index_names, headers])
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


    st.title("NAVEGADOR DE DATOS BUNDESLIGA TORNEO 2022/2023")
    if dropdown_club == ALL:
        if dropdown_player==ALL:
            st.write(f'Indicadores Club: {dropdown_club} - Jugador: {dropdown_player}')
            df_styled=df.style.set_table_styles([cell_hover, index_names, headers]).set_properties(**properties)
            st.table(df_styled)
        else:
            st.write(f'Indicadores Club: {dropdown_club} - Jugador: {dropdown_player}')
            df_filt=df[df['Jugador']==dropdown_player]
            df_styled=df_filt.style.set_table_styles([cell_hover, index_names, headers]).set_properties(**properties)
            st.table(df_styled[df_styled['Jugador']==dropdown_player])
    else:
        if dropdown_player==ALL:
            st.write(f'Indicadores Club: {dropdown_club} - Jugador: {dropdown_player}')
            st.write(df[df['Club']==dropdown_club])
        else:
            st.write(f'Indicadores Club: {dropdown_club} - Jugador: {dropdown_player}')
            st.write(df[(df['Club']==dropdown_club) & (df['Jugador']==dropdown_player)])
