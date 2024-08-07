from pysnmp.hlapi import *

def poll_device(ip, community='public'):
    data = {}
    for oid, name in [('1.3.6.1.4.1.2021.10.1.3.1', 'cpu'),
                      ('1.3.6.1.4.1.2021.4.5.0', 'memory'),
                      ('1.3.6.1.2.1.2.2.1.10.2', 'bandwidth')]:
        iterator = getCmd(SnmpEngine(),
                          CommunityData(community, mpModel=0),
                          UdpTransportTarget((ip, 161)),
                          ContextData(),
                          ObjectType(ObjectIdentity(oid)))

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                data[name] = float(varBind[1])

    return data
