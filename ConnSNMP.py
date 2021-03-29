from easysnmp import session

class ConnSNMP:
    def __init__(self, pw_priv = "", pw_auth = ""):
        self.pw_priv = pw_priv
        self.pw_auth = pw_auth
        
    def create_session(self):
        session.Session()