import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import datetime
import login.login_service as lsogin_service

if "login_service" not in st.session_state:
    st.session_state.login_service = None

login_service = lsogin_service.LoginService()
st.session_state.login_service = login_service
# 加载配置，使用支持邮箱登录的认证器
authenticator = login_service.get_authenticator()   

try:
    authenticator.login()
    if st.session_state.get('authentication_status'):

        pages = [
            st.Page("page/main.py", title="主页面"),
            st.Page("page/setting.py", title="设置"),
        ]

        #渲染导航菜单（默认就在侧边栏）
        current_page = st.navigation(pages)
        current_page.run()  # 运行选中页面的脚本 
    else:
        st.info(f'If you do not have a personal account, you can log in to experience it using the following account and password. Username: zeke | Password: zeke#0419', icon="ℹ️")
    

except Exception as e:
    st.error(e)



