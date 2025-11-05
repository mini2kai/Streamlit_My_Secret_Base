import streamlit as st
import login.login_service as lsogin_service


st.write(f"欢迎回来，{st.session_state.get('username', '用户')}！")
st.write("这是主页面内容。")

# 可以在这里添加主页面的具体功能
st.write("\n您可以使用左侧导航栏访问其他页面。")
