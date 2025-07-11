import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import altair as alt
import mysql.connector


# head
st.subheader("📉한눈에 알아보는 국내 자동차 시장 점유율") 

# data
# df = pd.read_csv('C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/prog_languages_data.csv')


# pie chart 1 - 2020

#- 데이터베이스 연결
def get_data():
    conn = mysql.connector.connect(
        host='localhost',
        user='sixsense',
        password='sixsense',
        database='cardb'
    )
    query = """
        SELECT (CASE WHEN C.BRAND_NAME LIKE '기아%' THEN '기아자동차'
                    WHEN C.BRAND_NAME LIKE '현대%' THEN '현대자동차'
                    ELSE '기타' END) BRAND_GROUP,
                SUM(R.REGISTED_COUNT) AS TOTAL_COUNT
        FROM CAR_INFO C
        LEFT JOIN REGISTED_INFO R USING (BRAND_CODE)
        WHERE R.YEAR = '2020' 
            AND R.REGISTED_COUNT IS NOT NULL
        GROUP BY BRAND_GROUP;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


#- 데이터 불러오기
dfs = get_data()

#- 사용자 정의 hover 텍스트 생성
dfs["hover_text"] = dfs["BRAND_GROUP"] + "<br>등록 대수: " + dfs["TOTAL_COUNT"].apply(lambda x: f"{x:,}") + "대"

#- 원형 차트 시각화
fig = px.pie(
    dfs,
    names="BRAND_GROUP",
    values="TOTAL_COUNT",
    title="2020년도 자동차 등록 현황",
    hover_data=["hover_text"],
)

fig.update_traces(
    hovertemplate="%{customdata[0]}<extra></extra>",
    customdata=dfs[["hover_text"]]
)

st.plotly_chart(fig)


st.header("")


# 뉴스 헤드라인 이미지 삽입
img_url1 = "C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/img/news_img.png"
news_link1 = "https://zdnet.co.kr/view/?no=20250103171650"

img_url2 = "C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/img/news_img2.png"
news_link2 = "https://news.einfomax.co.kr/news/articleView.html?idxno=4362946"

col1, col2 = st.columns(2)

with col1:
    st.image(img_url1, width=300)
    st.link_button("해당 뉴스 보러가기", url=news_link1)

with col2:
    st.image(img_url2, width=400)
    st.link_button("해당 뉴스 보러가기", url=news_link2)

st.header("")

# pie chart 2 - 최신 

#- 데이터베이스 연결
def get_data():
    conn = mysql.connector.connect(
        host='localhost',
        user='sixsense',
        password='sixsense',
        database='cardb'
    )

    query = """
        SELECT (CASE WHEN C.BRAND_NAME LIKE '기아%' THEN '기아자동차'
                    WHEN C.BRAND_NAME LIKE '현대%' THEN '현대자동차'
                    END) BRAND_GROUP,
                SUM(R.REGISTED_COUNT) AS TOTAL_COUNT
        FROM CAR_INFO C
        LEFT JOIN REGISTED_INFO R USING (BRAND_CODE)
        WHERE R.YEAR = '최신' AND R.REGISTED_COUNT IS NOT NULL
        GROUP BY BRAND_GROUP;
    """

    df = pd.read_sql(query, conn)
    conn.close()
    return df


#- 데이터 불러오기
dfs = get_data()

#- 사용자 정의 hover 텍스트 생성
dfs["hover_text"] = dfs["BRAND_GROUP"] + "<br>판매 대수: " + dfs["TOTAL_COUNT"].apply(lambda x: f"{x:,}") + "대"

#- 원형 차트 시각화
fig = px.pie(
    dfs,
    names="BRAND_GROUP",
    values="TOTAL_COUNT",
    title="최근 2개년도 기아 vs 현대 판매량",
    hover_data=["hover_text"],    
)

fig.update_traces(
    hovertemplate="%{customdata[0]}<extra></extra>",
    customdata=dfs[["hover_text"]]
)

st.plotly_chart(fig)




col1, _, col3 = st.columns(3)
with col1:
    # 이전 페이지 이동 버튼
    if st.button("이전 페이지"):
        st.switch_page("main_page.py")

with col3:
    # 비교 페이지 바로가기 버튼
    if st.button("순위 페이지 바로 가기"):
        st.switch_page("pages/2_rank_page.py")