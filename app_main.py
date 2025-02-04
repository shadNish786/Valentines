import streamlit as st

st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="collapsed", menu_items=None)

col1, col2  = st.columns(2)

with col1:
    pass
with col2 :
    center_button = st.button('CLICK ME')

if center_button:
    st.write("hi")