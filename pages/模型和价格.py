import streamlit as st

st.title("模型和价格")
st.title("")
st.markdown("""##### 现支持gpt-3.5-turbo, gpt-4, 价格如下:""")
st.write("")
st.markdown("""
| Model             | Input                  | Output                 |
|-------------------|------------------------|------------------------|
| gpt-4             | 0.024 rmb / 1k tokens  | 0.048 rmb / 1k tokens  |
| gpt-4-32K         | 0.048 rmb / 1k tokens  | 0.096 rmb / 1k tokens  |
| gpt-3.5-turbo     | 0.0012 rmb / 1k tokens | 0.0016 rmb / 1k tokens |
| gpt-3.5-turbo-16K | 0.0024 rmb / 1k tokens | 0.0032 rmb / 1k tokens |
""")
st.write("")
st.markdown("""##### 1k tokens ≈ 552个汉字, 费率与官方一致，8毛一刀，相当于官方价格的1折 ！(快涨价了, 先到先得!)""")
