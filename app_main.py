import streamlit as st
import pathlib

#load css file
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

#load the external css
css_path = pathlib.Path("style.css")
load_css(css_path)

st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="collapsed", menu_items=None)
st.title("AI stat maker:")
col1, col2  = st.columns(2)

with col1:
    pass
with col2 :
    center_button = st.button('CLICK ME', key="red")

if center_button:
    st.audio("song   3s/SEE YOU AGAIN featuring Kali Uchis [TGgcC5xg9YI].mp3",start_time=27, autoplay=True)
