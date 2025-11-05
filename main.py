import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import datetime
import login.login_service as lsogin_service

login_service = lsogin_service.LoginService()
# 加载配置，使用支持邮箱登录的认证器
authenticator = login_service.get_authenticator()   

try:
    authenticator.login()
    if st.session_state.get('authentication_status'):
        st.success("登录成功")
        authenticator.logout()

    st.write(st.session_state)

except Exception as e:
    st.error(e)

