import streamlit as st
import pyshorteners


st.title("Encurtador de Links")
#st.header("Qual é o seu nome")
title = st.text_input(
    'Digite abaixo o link',
    'default',)

url = title
link = pyshorteners.Shortener()
shorten_url = link.tinyurl.short(url)
st.write("Segue o seu link:", f'\n{shorten_url}')