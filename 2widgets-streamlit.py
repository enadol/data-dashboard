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

df.style.set_table_styles([cell_hover, headers]).set_properties(**properties).hide(axis="index")

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

st.sidebar.write("Datos, edades y fechas al término del torneo 2022/23 de la Bundesliga en Alemania (mayo de 2023)")

with st.container():


    st.title("NAVEGADOR DE DATOS BUNDESLIGA TORNEO 2022/2023")
    if dropdown_club == ALL:
        if dropdown_player==ALL:
            st.write(f'Indicadores Club: {dropdown_club} - Jugador: {dropdown_player}')
            df_styled=df.style.format(precision=0).set_table_styles([cell_hover, index_names, headers]).set_properties(**properties)
            st.table(df_styled)
        else:
            st.write(f'Indicadores Club: {dropdown_club} - Jugador: {dropdown_player}')
            df_filt=df[df['Jugador']==dropdown_player]
            df_styled=df_filt.style.format(precision=0).set_table_styles([cell_hover, index_names, headers]).set_properties(**properties)
            st.table(df_styled)
    else:
        if dropdown_player==ALL:
            st.write(f'Indicadores Club: {dropdown_club} - Jugador: {dropdown_player}')
            df_filt=df[df['Club']==dropdown_club]
            df_styled=df_filt.style.format(precision=0).set_table_styles([cell_hover, index_names, headers]).set_properties(**properties)
            st.table(df_styled)
        else:
            st.write(f'Indicadores Club: {dropdown_club} - Jugador: {dropdown_player}')
            df_filt=df[(df['Club']==dropdown_club) & (df['Jugador']==dropdown_player)]
            df_styled=df_filt.style.format(precision=0).set_table_styles([cell_hover, index_names, headers]).set_properties(**properties)
            with st.container():
                c1, c2, c3=st.columns([0.3, 0.3, 0.3], gap="small")
                c1.write(df_filt['Jugador'])
                c2.write(df_filt['Nacimiento'])
                c3.write(df_filt['Nación'])
            with st.container():
                c4, c5, c6=st.columns([0.3, 0.3, 0.3], gap="small")
                c4.write(df_filt['PJ'])
                c5.write(df_filt['Goles'])
                c6.write(df_filt['Asistencias'])                

            #st.table(df_styled)
