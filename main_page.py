import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import altair as alt


# head
st.title("🚗New Car Talk💭")
st.caption("")
st.subheader("🚶처음 차를 고민하는 당신을 위한 첫 걸음")


# 로고 이미지
col1, col2 = st.columns([1, 1.5])
with col1:
    img = Image.open('New_Car_Talk_.png')
    st.image(img, width=260)

# 페이지 설명
with col2:
    st.caption("")

    st.warning("저희는 성공적인 **첫 차 구매 계획 레퍼런스**를 제공합니다.")
    st.warning("💁‍♀️ 이런 분들에게 추천드립니다!")    
    st.warning('''➿ 첫 차를 구매하려는 **사회초년생 또는 대학생**에게  \n➿ 자동차 소비자 **인사이트**가 필요하신 분들에게  \n➿ 브랜드별 **인기 차종 순위**를 확인하고 싶은 분들에게  ''')    
    st.caption("")

col1, _, col3 = st.columns(3)
with col3:
    # 차트 페이지 바로가기 버튼
    if st.button("브랜드 점유율 알아보기 ▶️"):
        st.switch_page("pages/1_chart_page.py")


