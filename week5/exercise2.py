#!/usr/bin/env python

sw1_show_cdp_neighbors = '''
SW1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                                 S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone
Device ID            Local Intrfce        Holdtme        Capability        Platform    Port ID
R1                    Fas 0/11              153            R S I           881          Fas 1
R2                    Fas 0/12              123            R S I           881          Fas 1
R3                    Fas 0/13              129            R S I           881          Fas 1
R4                    Fas 0/14              173            R S I           881          Fas 1
R5                    Fas 0/15              144            R S I           881          Fas 1
'''

sw1_show_cdp_neighbors_detail = '''
SW1> show cdp neighbors detail
--------------------------
Device ID: R1
Entry address(es):
   IP address: 10.1.1.1
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/11, Port ID (outgoing port): FastEthernet1
Holdtime: 153 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R2
Entry address(es):
   IP address: 10.1.1.2
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/12, Port ID (outgoing port): FastEthernet1
Holdtime: 123 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R3
Entry address(es):
   IP address: 10.1.1.3
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/13, Port ID (outgoing port): FastEthernet1
Holdtime: 129 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R4
Entry address(es):
   IP address: 10.1.1.4
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/14, Port ID (outgoing port): FastEthernet1
Holdtime: 173 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R5
Entry address(es):
   IP address: 10.1.1.5
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/15, Port ID (outgoing port): FastEthernet1
Holdtime: 144 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
'''

r1_show_cdp_neighbors = '''
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/11
'''

r1_show_cdp_neighbors_detail = '''
R1>show cdp neighbors detail
-------------------------
Device ID: SW1
Entry address(es):
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/11
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r2_show_cdp_neighbors = '''
R2>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/12
'''

r2_show_cdp_neighbors_detail = '''
R2>show cdp neighbors detail
-------------------------
Device ID: SW1
Entry address(es):
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/12
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r3_show_cdp_neighbors = '''
R3>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/13
'''

r3_show_cdp_neighbors_detail = '''
R3>show cdp neighbors detail
-------------------------
Device ID: SW1
Entry address(es):
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/13
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Versin 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r4_show_cdp_neighbors = '''
R4>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/14
'''

r4_show_cdp_neighbors_detail = '''
R4>show cdp neighbors detail
-------------------------
Device ID: SW1
Entry address(es):
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/14
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r5_show_cdp_neighbors = '''
R5>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/15
'''

r5_show_cdp_neighbors_detail = '''
R5>show cdp neighbors detail
-------------------------
Device ID: SW1
Entry address(es):
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/15
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

import pprint
network_devices = {}

def main():
    parsecdpdetail(sw1_show_cdp_neighbors_detail)
    parsecdpdetail(r1_show_cdp_neighbors_detail)
    parsecdpdetail(r2_show_cdp_neighbors_detail)
    parsecdpdetail(r3_show_cdp_neighbors_detail)
    parsecdpdetail(r4_show_cdp_neighbors_detail)
    parsecdpdetail(r5_show_cdp_neighbors_detail)

    parsecdp(sw1_show_cdp_neighbors)
    parsecdp(r1_show_cdp_neighbors)
    parsecdp(r2_show_cdp_neighbors)
    parsecdp(r3_show_cdp_neighbors)
    parsecdp(r4_show_cdp_neighbors)
    parsecdp(r5_show_cdp_neighbors)

    pprint.pprint(network_devices)


def parsecdpdetail(cdpdetaildata):
    cdpdetaildatalist = cdpdetaildata.split('-------------------------')
    i = 1
    while i < len(cdpdetaildatalist):
        innerdetaildict = {}
        tempdetaillist = cdpdetaildatalist[i].split('\n')
        for item in tempdetaillist:
            if 'Device ID:' in item:
                hostname = item.split(':')[-1].strip()
            if 'IP address:' in item:
                ip = item.split(':')[-1].strip()
            if 'Platform:' in item:
                model = item.split(',')[0].split(' ')[-1]
                vendor = item.split(',')[0].split(' ')[-2]
                if ('Router' in item) and ('Switch' in item):
                    device_type = 'Router'
                elif ('Router' not in item) and ('Switch' in item):
                    device_type = 'Switch'
                else:
                    device_type = 'Unknown'
        if hostname in network_devices.keys():
            pass
        else:
            innerdetaildict['ip'] = ip
            innerdetaildict['model'] = model
            innerdetaildict['vendor'] = vendor
            innerdetaildict['device_type'] = device_type
            network_devices[hostname] = innerdetaildict
        i += 1


def parsecdp(cdpdata):
    cdpdatalist = cdpdata.split('\n')
    j = 5
    innerlist = []
    while j < (len(cdpdatalist) - 1):
        hostname = cdpdatalist[(j - (j-1))].split('>')[0]
        templist = cdpdatalist[j].split()
        host = templist[0]
        innerlist.append(host)
        j += 1
    if hostname in network_devices.keys():
        network_devices[hostname]['adjacent_devices'] = innerlist
    else:
        pass

if __name__ == '__main__':
    main()
