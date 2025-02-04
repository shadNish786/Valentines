import streamlit as st
import plotly.express as px
import pandas as pd


st.title("Statistics:")

df= pd.DataFrame(dict(
    x = [1, 2, 3, 4],
    y = [1, 2, 3, 4]
))

fig = px.line(df, x="x", y="y", title="How much I love you <3")

fig.show()


