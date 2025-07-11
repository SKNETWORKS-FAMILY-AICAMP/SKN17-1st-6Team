import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import altair as alt


# head
st.subheader("📉한눈에 알아보는 국내 자동차 시장 점유율") 

# data
df = pd.read_csv('C:/skn_17/sixth_sense/prog_languages_data.csv')


# pie chart 1 - 2020
fig = px.pie(df, 'lang', 'Sum', title = "브랜드별 점유율_2020")
st.plotly_chart(fig)


st.caption("출처 : 국토교통부 자동차365 2020년 신차 등록대수 분석")
st.caption("")



# pie chart 2 - 2024
fig2 = px.pie(df, 'lang', 'Sum', title = "브랜드별 점유율_2024")
st.plotly_chart(fig2)


st.caption('''출처 : 국토교통부 2024년자동차 등록 현황''')
st.caption("")



col1, _, col3 = st.columns(3)
with col1:
    # 이전 페이지 이동 버튼
    if st.button("◀️ 이전 페이지"):
        st.switch_page("main_page.py")

with col3:
    # 비교 페이지 바로가기 버튼
    if st.button("순위 페이지 바로 가기  ▶️"):
        st.switch_page("pages/2_rank_page.py")


