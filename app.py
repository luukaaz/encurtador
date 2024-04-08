import streamlit as st
import pyshorteners

default_value = 0
title = default_value

st.title("Encurtador de Links")
#st.header("Qual é o seu nome")
title = st.text_input(
    'Digite abaixo o seu link',
    'link',)

url = title
link = pyshorteners.Shortener()
shorten_url = link.tinyurl.short(url)

if title:
    st.write("Segue o seu link:", f'\n{shorten_url}')

title = default_value
