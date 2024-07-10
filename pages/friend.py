import streamlit as st
import backgroud.backgroud as bg
st.title("男友性格选择页面")
if "xingge" not in st.session_state:
    st.session_state.xingge = ""
bt = st.button("狼系男友")
if bt:
    st.session_state.xingge="强势自信"
    st.switch_page("pages/aibot.py")
bt1 = st.button("犬系男友")
if bt1:
    st.session_state.xingge="阳光忠诚"
    st.switch_page("pages/aibot.py")
bt2 = st.button("狐系男友")
if bt2:
    st.session_state.xingge="机智幽默"
    st.switch_page("pages/aibot.py")
bg.main_bg('image/frend1.jpg')