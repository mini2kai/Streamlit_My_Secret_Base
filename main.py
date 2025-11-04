import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import datetime

# 设置页面配置
st.set_page_config(
    page_title="我的秘密基地",
    page_icon="🔒",
    layout="wide"
)

# 加载配置
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# 登录界面
authenticator.login(key='login')

# 从session_state获取认证状态
authentication_status = st.session_state.get('authentication_status')
username = st.session_state.get('username')
name = st.session_state.get('name')

# 主应用逻辑
if authentication_status:
    # 登录成功后显示的内容
    st.title(f"欢迎回来，{name}！")
    st.markdown("---")
    
    # 在侧边栏显示登出按钮和导航
    with st.sidebar:
        authenticator.logout("登出", "sidebar")
        st.title("导航菜单")
        # 创建导航选项
        page = st.radio(
            "选择功能：",
            ["个人信息", "笔记记录", "任务管理", "设置"]
        )
    
    # 显示当前时间
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.sidebar.caption(f"当前时间: {current_time}")
    
    # 不同页面的内容
    if page == "个人信息":
        st.header("个人信息")
        st.subheader("用户详情")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**用户名:** {username}")
            st.write(f"**姓名:** {name}")
            st.write(f"**上次登录:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        with col2:
            st.info("这里是您的个人信息区域。")
            st.markdown("### 安全提示")
            st.markdown("- 定期更改密码")
            st.markdown("- 不要与他人共享您的账户")
    
    elif page == "笔记记录":
        st.header("我的笔记")
        
        # 笔记标题输入
        note_title = st.text_input("笔记标题")
        
        # 笔记内容输入
        note_content = st.text_area("笔记内容", height=300)
        
        # 保存按钮
        if st.button("保存笔记"):
            if note_title and note_content:
                st.success(f"笔记 '{note_title}' 已保存！")
                # 这里可以添加保存到文件或数据库的逻辑
            else:
                st.warning("请输入笔记标题和内容")
        
        # 显示已保存的笔记（模拟）
        st.subheader("已保存的笔记")
        st.info("这里将显示您保存的笔记列表")
    
    elif page == "任务管理":
        st.header("任务管理")
        
        # 添加新任务
        st.subheader("添加新任务")
        task_name = st.text_input("任务名称")
        task_date = st.date_input("截止日期")
        
        if st.button("添加任务"):
            if task_name:
                st.success(f"任务 '{task_name}' 已添加到 {task_date}！")
                # 这里可以添加保存到文件或数据库的逻辑
            else:
                st.warning("请输入任务名称")
        
        # 显示任务列表（模拟）
        st.subheader("我的任务")
        st.info("这里将显示您的任务列表")
    
    elif page == "设置":
        st.header("设置")
        st.subheader("账户设置")
        
        # 修改密码
        if st.button("修改密码"):
            try:
                # 这里调用重置密码的方法
                st.info("密码修改功能即将上线")
            except Exception as e:
                st.error(f"错误: {str(e)}")
        
        # 其他设置选项
        st.subheader("应用设置")
        theme = st.selectbox(
            "选择主题",
            ["浅色", "深色", "跟随系统"]
        )
        if st.button("应用设置"):
            st.success("设置已保存！")
            # 这里可以添加保存设置的逻辑

elif authentication_status == False:
    st.error("用户名或密码错误")
elif authentication_status == None:
    st.warning("请输入你的登录信息")
    # 添加一些说明文本
    with st.expander("登录说明"):
        st.markdown("- 用户名: alice  密码: alice123")
        st.markdown("- 用户名: bob  密码: bob123")
        st.markdown("*注意：这是演示账户，请仅用于测试*")
