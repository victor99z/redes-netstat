from easysnmp import Session
import os

# Create an SNMP session to be used for all our requests
session = Session(
    hostname= os.environ.get("TARGET_AGENT_ADDRESS"), 
    community='public', 
    version=3
    )

# Perform an SNMP walk
system_items = session.walk('ip')

# Each returned item can be used normally as its related type (str or int)
# but also has several extended attributes with SNMP-specific information
for item in system_items:
    print('{oid}.{oid_index} {snmp_type} = {value}'.format(
        oid=item.oid,
        oid_index=item.oid_index,
        snmp_type=item.snmp_type,
        value=item.value
    ))