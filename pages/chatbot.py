import streamlit as st
import backgroud.backgroud as bg
st.title('选择想要的ai模块🤞')

# 创建两列，第一列放置图片，第二列放置按钮
col1, col2 = st.columns([2, 1])

# 在第一列放置图片
with col1:
    st.image("https://th.bing.com/th?id=OIF.xmcsW8V4UfjPMP%2fgbZ4c%2fw&w=266&h=187&c=7&r=0&o=5&dpr=1.5&pid=1.7", use_column_width=True)

# 在第二列放置按钮
with col2:
    if st.button("基础ai助手"):
        st.switch_page("pages/xiaobaibot.py")
        # 在此处加载基础ai助手页面的内容

    if st.button("地理的一切"):
        st.switch_page("pages/dfswbot.py")
        # 在此处加载地理的一切页面的内容

    if st.button("男友类型选择"):
        st.switch_page("pages/friend.py")
        # 在此处加载自主cp选择页面的内容
bg.main_bg('image/chat.jpg')