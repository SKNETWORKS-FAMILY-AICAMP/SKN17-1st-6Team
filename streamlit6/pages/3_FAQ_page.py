import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import altair as alt
import csv


# head
st.subheader("❓ 브랜드 FAQ")

kia_tab, hd_tab = st.tabs(["기아자동차", "현대자동차"])


# 기아자동차 탭
with kia_tab:
    st.subheader("KIA 자주 묻는 질문💬")

    faq_data = []
    with open("C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/faq/faq_kia.csv", 'r', encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split('|')
            if len(parts) >= 2:
                question, answer = parts[0].strip(), parts[1].strip()
                faq_data.append((question, answer))

    # Expander로 FAQ 출력
    for question, answer in faq_data:
        with st.expander(question):
            st.write(answer)
    # with open("faq_kia.csv", 'r', encoding="utf-8") as f:
    #     faq = f.readlines()

    # for i in faq:
    #     ques, ans = i.split(',')

    # with st.expander(faq[1]):
    #     st.write(faq[0][1])


    with st.expander("기아차의 유지비는 어떤가요?"):
        st.write("연비 기준으로는 준수하며, 보증과 A/S망도 우수하다는 평이 많습니다.")

    with st.expander("기아차의 유지비는 어떤가요?"):
        st.write("연비 기준으로는 준수하며, 보증과 A/S망도 우수하다는 평이 많습니다.")

    url = 'https://www.kia.com/kr/customer-service/center/faq#none'
    st.warning(f"🔽 더 궁금하신 점이 있다면 아래 링크를 확인해주세요❗  \n{url}")









# 현대자동차 탭
with hd_tab:
    faq_data = []
    with open("C:/Users/mjs/Documents/GitHub/SKN17-1st-6Team/faq/faq_hyundai.csv", 'r', encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split('|')
            if len(parts) >= 2:
                question, answer = parts[0].strip(), parts[1].strip()
                faq_data.append((question, answer))

    # Expander로 FAQ 출력
    for question, answer in faq_data:
        with st.expander(question):
            st.write(answer)






    url = 'https://www.hyundai.com/kr/ko/e/customer/center/faq'
    st.warning(f"🔽 더 궁금하신 점이 있다면 아래 링크를 확인해주세요❗  \n{url}")









col1, _, _, _, col5 = st.columns(5)

with col1:
    # 이전 페이지 이동 버튼
    if st.button("◀️ 이전 페이지"):
        st.switch_page("pages/2_rank_page.py")

with col5:
    # 첫 페이지 이동 버튼
    if st.button("⏪ 첫 페이지"):
        st.switch_page("main_page.py")