import streamlit as st



st.set_page_config(page_title="Gallery", page_icon=None, layout="centered", initial_sidebar_state="collapsed", menu_items=None)

st.title("Gallery:")

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.image("images/52b8442c-e474-40b7-b897-207a970596d1.jpg")
with col2:
    st.image("images/35175577-5251-4d18-bb3d-1ca15c5f1cbb.jpg")
with col3:
    st.image("images/dclassic 2024-11-23 190400.228.jpg")
with col4:
    st.image("images\dclassic 2024-11-23 190510.804 (1).jpg")
with col5:
    st.image("images/DSCF6313_Original.JPG")




