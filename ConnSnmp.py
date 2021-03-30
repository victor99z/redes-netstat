from easysnmp import Session
import os
from dotenv import load_dotenv


class ConnSnmp:
    def __init__(self, address="localhost"):
        load_dotenv('.env')
        try:
            self.session = Session(
                hostname=address,
                community='public',
                version=3,
                security_username=os.getenv("USERNAME_SNMP"),
                auth_password=os.getenv("PASSWORD"),
                privacy_password=os.getenv("PASSWORD"),
                security_level='authPriv',
                auth_protocol='MD5',
                privacy_protocol="DES"
            )
        except SystemError:
            print("\033[91m Erro no IP do agente!")
