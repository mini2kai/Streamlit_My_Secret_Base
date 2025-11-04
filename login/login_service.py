import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth


class LoginService:
    def __init__(self):
        self.config = None
        self.authenticator = None
        # 加载配置文件
        self._load_config()

    def _load_config(self):
        """
        加载配置文件
        """
        with open('./login/config.yaml', 'r', encoding='utf-8') as file:
            self.config = yaml.load(file, Loader=SafeLoader)

    def get_authenticator(self):
        """
        获取认证器实例
        """
        if self.config is None:
            self._load_config()

        self.authenticator = stauth.Authenticate(
            self.config['credentials'],
            self.config['cookie']['name'],
            self.config['cookie']['key'],
            self.config['cookie']['expiry_days']
        )
        return self.authenticator

    def get_authenticator_with_email_support(self):
        """
        获取支持邮箱登录的认证器实例
        通过创建一个新的credentials字典，使邮箱可以作为用户名登录
        """
        if self.config is None:
            self._load_config()

        # 创建支持邮箱登录的credentials副本
        email_supported_credentials = {'usernames': {}}
        
        # 复制原始用户名登录信息
        for username, user_info in self.config['credentials']['usernames'].items():
            email_supported_credentials['usernames'][username] = user_info.copy()
            
        # 添加邮箱作为额外的用户名入口
        for username, user_info in self.config['credentials']['usernames'].items():
            if 'email' in user_info:
                email = user_info['email']
                # 确保邮箱不是None或空字符串
                if email and email not in email_supported_credentials['usernames']:
                    # 使用邮箱作为用户名的副本，保持密码和其他信息相同
                    email_supported_credentials['usernames'][email] = user_info.copy()

        # 创建支持邮箱登录的认证器
        self.authenticator = stauth.Authenticate(
            email_supported_credentials,
            self.config['cookie']['name'],
            self.config['cookie']['key'],
            self.config['cookie']['expiry_days']
        )
        return self.authenticator

    def save_cookie(self):
        """
        保存cookie配置
        """
        with open('./login/config.yaml', 'w', encoding='utf-8') as file:
            yaml.dump(self.config, file, default_flow_style=False, allow_unicode=True)
        return self.config['cookie']

