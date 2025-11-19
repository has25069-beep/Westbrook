import streamlit as st
import pandas as pd
import plotly.express as px

st.title('국가별 MBTI 유형 분포 분석')

# 데이터 불러오기
df = pd.read_csv('countriesMBTI_16types.csv', encoding='utf-8')

# 국가 선택 (selectbox)
country = st.selectbox('국가를 선택하세요', df['Country'].unique())

# 해당 국가 데이터 추출
row = df[df['Country'] == country].iloc[0]
mbti_types = [c for c in df.columns if c != 'Country']
values = [row[t] for t in mbti_types]

# 정렬하여 1등 색상, 나머지 그라데이션
sorted_idx = sorted(range(len(values)), key=lambda i: values[i], reverse=True)
color_set = ['#FF3333'] + px.colors.sample_colorscale('blues', [i/(len(values)-1) for i in range(1, len(values))])
colors = [None]*len(values)
for rank, idx in enumerate(sorted_idx):
    colors[idx] = color_set[rank]

fig = px.bar(x=mbti_types, y=values, color=mbti_types,
             color_discrete_sequence=colors,
             labels={'x':'MBTI 유형', 'y':'비율'},
             title=f'{country}의 MBTI 유형 분포',
             hover_name=mbti_types)

st.plotly_chart(fig)
