# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# 앱 제목
st.title("📦 배달 위치 시각화")

# CSV 파일 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("이정원 - Delivery.csv")
    return df

df = load_data()

# 지도 시각화
fig = px.scatter_mapbox(
    df,
    lat="Latitude",
    lon="Longitude",
    hover_name="Num",
    zoom=10,
    height=600,
    color_discrete_sequence=["blue"]
)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig)
