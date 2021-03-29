from easysnmp import Session
from dotenv import load_dotenv
import os
import sys

load_dotenv('.env')

session = Session(
    hostname=os.getenv("TARGET_AGENT_ADDRESS"),
    community='public',
    version=3,
    security_username=os.getenv("USERNAME_SNMP"),
    auth_password=os.getenv("PASSWORD"),
    privacy_password=os.getenv("PASSWORD"),
    security_level='authPriv',
    auth_protocol='MD5',
    privacy_protocol="DES"
)

# Perform an SNMP walk

description = session.get('.1.3.6.1.2.1.1.1.0')

print(f'Descrição:  {description.value}')

system_items = session.walk('.1.3.6.1.2.1.6.13.1.1')
print(system_items)

for item in system_items:
    print('{oid}.{oid_index} {snmp_type} = {value}'.format(
        oid=item.oid,
        oid_index=item.oid_index,
        snmp_type=item.snmp_type,
        value=item.value
    ))

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")
