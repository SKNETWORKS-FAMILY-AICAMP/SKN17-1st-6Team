import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import altair as alt
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from pages.sdb import recent_excel as r

# head
st.subheader("🚀 대표 브랜드별 인기 차량 비교")
st.caption("")

    
# --기아자동차 영역
col1, col2, col3, _ = st.columns([1, 1, 1.5, 0.5])

with col1:
    img = Image.open('C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/img/kia_logo.png')
    st.image(img, width=150)
        
with col2:
    st.subheader("인기 순위")

with col3:
    st.caption("")
    st.caption("판매 대수는 2024년 기준입니다.")
    
# --기아자동차 인기 순위
kia_top5 = r.kia_recent()       # recent 엑셀 불러오기

top1, top2, top3 = st.columns(3)

with top1:
    st.subheader("1위")
    st.subheader(kia_top5[0][0][:3])

    img = Image.open("C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/img/k_sor.jpg")
    st.image(img)

    st.warning(f"▪️총 판매 대수: {kia_top5[0][1]}대  \n▪️차종명 : 중형 SUV  \n▪️가격 : 3,550만원 ~")

with top2:
    st.subheader("2위")
    st.subheader(kia_top5[1][0][:3])

    img = Image.open("C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/img/k_ca.jpg")
    st.image(img)

    st.warning(f"▪️총 판매 대수: {kia_top5[1][1]}대  \n▪️차종명 : 대형 MPV  \n▪️가격 : 3,551만원 ~")

with top3:
    st.subheader("3위")
    st.subheader(kia_top5[2][0][:4])

    img = Image.open("C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/img/k_스포티지.jpg")
    st.image(img)

    st.warning(f"▪️총 판매 대수: {kia_top5[2][1]}대  \n▪️차종명 : 중형 SUV  \n▪️가격 : 2,793만원 ~")

top4, top5, top6 = st.columns(3)

with top4:
    st.subheader("4위")
    st.subheader(kia_top5[3][0][:3])

    img = Image.open("C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/img/k_셀.jpg")
    st.image(img)

    st.warning(f"▪️총 판매 대수: {kia_top5[3][1]}대  \n▪️차종명 : 소형 SUV  \n▪️가격 : 2,169만원 ~")

with top5:
    st.subheader("5위")
    st.subheader(kia_top5[4][0][:2])

    img = Image.open("C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/img/k_Ra.jpg")
    st.image(img)
    st.warning(f"▪️총 판매 대수: {kia_top5[4][1]}대  \n▪️차종명 : 경차  \n▪️가격 : 1,340만원 ~")

with top6:
    pass

# --------------------------------------------------------------------------
st.header("")

# --현대자동차 영역
col11, col12, col13, _ = st.columns([1, 1, 1.5, 0.5])

with col11:
    img = Image.open('C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/img/hd_logo.png')
    st.image(img, width=150)
        
with col12:
    st.subheader("인기 순위")

with col13:
    st.caption("")
    st.caption("판매 대수는 2024년 기준입니다.")



# --현대자동차 인기 순위
hd_top5 = r.hyundai_recent()    # recent 엑셀 불러오기

top1, top2, top3 = st.columns(3)

with top1:
    st.subheader("1위")
    st.subheader(hd_top5[0][0][:3])
    img = Image.open("C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/img/h_g80.png")
    st.image(img)
    st.warning(f"▪️총 판매 대수: {hd_top5[0][1]}대  \n▪️차종명 : 중형 SUV  \n▪️가격 : 3,492만원 ~")

with top2:
    st.subheader("2위")
    st.subheader(hd_top5[1][0][:3])
    img = Image.open("C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/img/h_sant.png")
    st.image(img)
    st.warning(f"▪️총 판매 대수: {hd_top5[1][1]}대  \n▪️차종명 : 준대형  \n▪️가격 : 3,798만원 ~")

with top3:
    st.subheader("3위")
    st.subheader(hd_top5[2][0][:3])
    img = Image.open("C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/img/h_gra.png")
    st.image(img)
    st.warning(f"▪️총 판매 대수: {hd_top5[2][1]}대  \n▪️차종명 : 준중형  \n▪️가격 : 2,034만원 ~")

top4, top5, top6 = st.columns(3)

with top4:
    st.subheader("4위")
    st.subheader(hd_top5[3][0][:2])
    img = Image.open("C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/img/h_ava.png")
    st.image(img)
    st.warning(f"▪️총 판매 대수: {hd_top5[3][1]}대  \n▪️차종명 : 중형SUV  \n▪️가격 : 2,729만원 ~")

with top5:
    st.subheader("5위")
    st.subheader(hd_top5[4][0][:3])
    img = Image.open("C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/img/h_tu.png")
    st.image(img)
    st.warning(f"▪️총 판매 대수: {hd_top5[4][1]}대  \n▪️차종명 : 준대형  \n▪️가격 : 5,899만원 ~")
  
with top6:
    pass











# 선택 후 비교 시각화



col1, _, col3 = st.columns(3)

with col1:
    # 이전 페이지 이동 버튼
    if st.button("◀️ 이전 페이지"):
        st.switch_page("pages/1_chart_page.py")

with col3:
    # FAQ 페이지 바로가기 버튼
    if st.button("FAQ 페이지 바로가기  ▶️"):
        st.switch_page("pages/3_FAQ_page.py")


_, _, col13 = st.columns(3)

with col3:
    # 비교 페이지 바로가기 버튼
    url = "https://auto.danawa.com/compare/?Codeas="
    if st.button("차량비교를 원한다면❓"):
        st.write(f"🔽 비교 사이트 바로가기{url}")

