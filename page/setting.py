import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import datetime



login_service = st.session_state.login_service

authenticator = login_service.authenticator

authenticator.logout()


st.write("欢迎来到设置页面！")



