from easysnmp import Session
from dotenv import load_dotenv
import os

# Import our variables from .env file
load_dotenv('.env')

# FIXME: arrumar a session para o snmpv3, nao funcionando auth

# Create an SNMP session to be used for all our requests
session = Session(
    hostname= os.getenv("TARGET_AGENT_ADDRESS"), 
    community='public', 
    version=3,
    security_username= 'bootstrap',
    auth_password= 'udescUdesc',
    privacy_password= 'udescUdesc',
    )

# Perform an SNMP walk
# system_items = session.walk('system')

description = session.get('.1.3.6.1.2.1.6.13')

print(f'Descrição:  {description}')

# Each returned item can be used normally as its related type (str or int)
# but also has several extended attributes with SNMP-specific information
'''
for item in system_items:
    print('{oid}.{oid_index} {snmp_type} = {value}'.format(
        oid=item.oid,
        oid_index=item.oid_index,
        snmp_type=item.snmp_type,
        value=item.value
    ))

'''