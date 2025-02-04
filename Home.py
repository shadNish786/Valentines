import streamlit as st
import streamlit.components.v1 as com

import pathlib


st.set_page_config(page_title="home", page_icon=None, layout="centered", initial_sidebar_state="collapsed", menu_items=None)



#load css file
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

#load the external css
css_path = pathlib.Path("style.css")
load_css(css_path)

if "confirmed_yes" not in st.session_state:
    st.session_state.confirmed_yes = False


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
    com.iframe("https://lottie.host/embed/ce788ef7-0bba-4d86-8f37-f8fd78bb6ccd/zp2bjsqxUb.lottie")

if no_button:
    st.audio("songs/Lift Yourself [8fbyfDbi-MI].mp3",start_time=112,autoplay=True)
    com.iframe("https://lottie.host/embed/8dbac72e-5b96-4998-82b7-1f70a3df1ecf/LsH8Aovq3y.lottie")
    
    col4,col5,col6 = st.columns(3)
    with col4:
        pass

    with col5:
        check_button =st.button("are you sure you dont mean yes?")

    with col6:
        pass

    if check_button:
        st.session_state.confirmed_yes = True
        st.experimental_rerun()
        




        



if ofcourse_button or st.session_state.confirmed_yes:
    st.audio("songs/Lady Gaga, Bruno Mars - Die With A Smile (Official Music Video) [kPa7bsKwL-c].mp3",start_time=30,autoplay=True)
    com.iframe("https://lottie.host/embed/a30e1791-98e2-45d2-927c-a259120e1460/MFS2TgkkWM.lottie")

