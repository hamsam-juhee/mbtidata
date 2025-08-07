import streamlit as st
import pandas as pd
import altair as alt

st.title("🌍 국가별 가장 흔한 MBTI 유형 보기")

# CSV 파일 업로드
uploaded_file = st.file_uploader("MBTI 비율 CSV 파일 업로드", type=["csv"])

if uploaded_file is not None:
    # 데이터 불러오기
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 원본 데이터 미리보기")
    st.dataframe(df.head())

    # 각 국가에서 가장 비율이 높은 MBTI 유형 찾기
    mbti_columns = df.columns[1:]
    df["Top_MBTI"] = df[mbti_columns].idxmax(axis=1)

    st.subheader("🏆 국가별 가장 흔한 MBTI 유형")
    st.dataframe(df[["Country", "Top_MBTI"]])

    # MBTI 유형별 개수 집계
    top_counts = df["Top_MBTI"].value_counts().reset_index()
    top_counts.columns = ["MBTI", "Count"]

    # Altair 바 차트
    st.subheader("📈 가장 흔한 MBTI 유형 (국가 기준)")
    chart = alt.Chart(top_counts).mark_bar().encode(
        x=alt.X("MBTI:N", sort="-y", title="MBTI 유형"),
        y=alt.Y("Count:Q", title="국가 수"),
        tooltip=["MBTI", "Count"]
    ).properties(
        width=600,
        height=400
    )

    st.altair_chart(chart)

else:
    st.info("왼쪽에서 CSV 파일을 업로드해주세요. 예: countriesMBTI_16types.csv")
