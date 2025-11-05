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





