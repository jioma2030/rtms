# main.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="배달 위치 시각화", layout="wide")

# 제목
st.title("📦 배달 위치 시각화 앱")

# CSV 데이터 로드
@st.cache_data
def load_data():
    df = pd.read_csv("이정원 - Delivery.csv")
    return df

df = load_data()

# 데이터 개수 및 미리보기
st.subheader("데이터 미리보기")
st.write(f"총 데이터 수: {len(df)}개")
st.dataframe(df)

# Plotly 지도 생성
st.subheader("지도 시각화 (Plotly Mapbox)")

fig = px.scatter_mapbox(
    df,
    lat="Latitude",
    lon="Longitude",
    hover_name="Num",
    zoom=10,
    height=600,
    color_discrete_sequence=["royalblue"]
)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig, use_container_width=True)
