import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth


class LoginService:
    def __init__(self):
        pass

    def get_authenticator(self):
        # 此处应有缩进块
        with open('./login/config.yaml') as file:
            self.config = yaml.load(file, Loader=SafeLoader)

        self.authenticator = stauth.Authenticate(
            self.config['credentials'],
            self.config['cookie']['name'],
            self.config['cookie']['key'],
            self.config['cookie']['expiry_days']
        )
        return self.authenticator

    def save_cookie(self):
        with open('./login/config.yaml', 'w') as file:
            yaml.dump(self.config, file, default_flow_style=False, allow_unicode=True)
        return self.config['cookie']

