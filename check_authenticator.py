import streamlit as st
import login.login_service as lsogin_service
import inspect
import json

# 获取认证器实例
authenticator = lsogin_service.LoginService().get_authenticator_with_email_support()

# 打印对象类型
print(f"对象类型: {type(authenticator)}")

# 分开打印属性和方法，避免输出过长
print("\n=== 对象属性 ===")
attributes = []
for attr in dir(authenticator):
    if not attr.startswith('__'):
        method = getattr(authenticator, attr)
        if not callable(method):
            attributes.append(attr)

print("\n非方法属性:")
for attr in sorted(attributes):
    print(f"- {attr}")

print("\n=== 对象方法 ===")
methods = []
for method_name in dir(authenticator):
    if not method_name.startswith('__'):
        method = getattr(authenticator, method_name)
        if callable(method):
            methods.append(method_name)

print("\n方法列表:")
for method in sorted(methods):
    print(f"- {method}")

# 尝试使用Streamlit的方式查看session_state
print("\n=== Streamlit Session State ===")
# 这里我们只是展示session_state的内容，实际运行时可以通过浏览器查看
print("运行Streamlit应用时，可以在浏览器中查看session_state的内容")
print("主要包含authentication_status, username, logout等信息")