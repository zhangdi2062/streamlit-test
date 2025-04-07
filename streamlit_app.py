import streamlit as st

st.header('st.button')

# 初始化session state中的计数器
if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button('Say hello'):
    # 更新计数并显示
    st.session_state.count += 1
    st.write(f'点击次数：{st.session_state.count}')
    st.write('Why hello there')
else:
     st.write('Goodbye')


import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# 样例 1

st.write('Hello, *World!* :sunglasses:')

# 样例 2

st.write(1234)

# 样例 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# 样例 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# 样例 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)