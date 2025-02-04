import streamlit as st
import pathlib


st.set_page_config(page_title="home", page_icon=None, layout="centered", initial_sidebar_state="collapsed", menu_items=None)



#load css file
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

#load the external css
css_path = pathlib.Path("style.css")
load_css(css_path)

st.title("Will you be my valentine? <3")

col1,col2,col3 = st.columns(3)

with col1:
    yes_button =st.button("YES")

with col2:
    ofcourse_button = st.button("Of course yes!!!")

with col3:
    no_button=st.button("NO - you suck")

if yes_button:
    st.audio("songs/SEE YOU AGAIN featuring Kali Uchis [TGgcC5xg9YI].mp3",start_time=27,autoplay=True)
    st.video("gifs\Excited Season 4 GIF by Friends.gif")


if ofcourse_button:
    st.audio("songs/Lady Gaga, Bruno Mars - Die With A Smile (Official Music Video) [kPa7bsKwL-c].mp3",start_time=30,autoplay=True)

if no_button:
    st.audio("songs/Lift Yourself [8fbyfDbi-MI].mp3",start_time=112,autoplay=True)