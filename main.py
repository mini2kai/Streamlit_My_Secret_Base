import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import datetime
import login.login_service as lsogin_service

# 加载配置
authenticator = lsogin_service.LoginService().get_authenticator()   

try:
    authenticator.login()

    if st.session_state.get('authentication_status'):
        st.success("登录成功")
        st.write(st.session_state)
        authenticator.logout()

    else:
        st.write(st.session_state)

except Exception as e:
    st.error(e)

