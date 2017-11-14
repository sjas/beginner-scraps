'''
This file contains the various tasks, along with the configuration solutions.
The tasks are in dictionary format, with the task (question) as the key, and
the solution (answer) as the value.

Variables and meanings used inside the strings in this file:
These variables get passed to randomvar.py and are replaced with actual values.

These are just for quick easy personal reference, you should change these to whatever
 is appropriate for you.

SINT(1 - 4) = serial interface
EINT(1 - 4) = ethernet interface
USERNAME
PASSWORD
NAME(1 - 4) = hostnames, group names, etc.
PERCENT / REVPCNT (100 - PERCENT)
RNDIP(1-4) = single standalone random unicast IP, no mask
RNDIPRANGE(1-4) = standalone unicast IP range with /24   x.x.x.x - y
  RNDIPRANGEst(1-4) = starting address from that range   x.x.x.x
  RNDIPRANGEen(1-4) = ending address from that range     x.x.x.y
RNDPFX(1-4)C = random /8 - /30 CIDR
RNDPFX(1-4)M = corresponding subnet mask
RNDPFX(1-4)W = corresponding wildcard mask / broadcast address
RND100x1 = random 1 - 100
RND100x2 = random 1 - 100
RND100x3 = random 1 - 100
RND100x4 = random 1 - 100
RND1K = random 1 - 1000
RND4094 = random 1 - 4094, excluding 1002-1005
RND24 = random between 2 and 4

Key/Value pairs below are separated with a #. This is just for visual clarity.

'''

tasks = {





'''
Configure the SINT1 interface using a Cisco-proprietary encapsulation.
''':
'''
interface SINT1
 encapsulation hdlc
''',
#
'''
Configure the SINT1 interface using a standard (non-frame-relay) encapsulation.
''':
'''
interface SINT1
 encapsulation ppp
 ''',
#
'''
Configure the synchronous serial interface SINT1 to use the default
encapsulation.
''':
'''
interface SINT1
 encapsulation hdlc
 ''',
#
'''
Configure the router to request PAP authentication on the SINT1 interface.
The expected username is 'USERNAME', and the expected
password is 'PASSWORD'.
''':
'''
username USERNAME password PASSWORD
interface SINT1
 encapsulation ppp
 ppp authentication pap
''',
#
'''
Configure the router to authenticate to its neighbor on the SINT1 interface
via PAP with the username 'USERNAME', and the
password 'PASSWORD'.
''':
'''
interface SINT1
 encapsulation ppp
 ppp pap sent-username USERNAME password PASSWORD
''',
#
'''
Configure the router to authenticate its neighbor on the SINT1 interface
via CHAP with the username 'USERNAME', and the
password 'PASSWORD'.
''':
'''
username USERNAME password PASSWORD
interface SINT1
 encapsulation ppp
 ppp authentication chap
''',
#
'''
Configure the router to authenticate to its neighbor on the SINT1 interface
via CHAP. The router's hostname is 'rtr-NAME1'. The neighbor
(rtr-NAME2) has already been properly configured. It uses the password
'PASSWORD' for CHAP authentication.
''':
'''
username rtr-NAME2 password PASSWORD
interface SINT1
 encapsulation ppp
 ppp authentication chap
 ppp chap hostname rtr-NAME1
''',
#
'''
Configure the router to attempt to authenticate on the SINT1 interface with
CHAP. Fall back to PAP authentication if CHAP fails.
''':
'''
interface SINT1
 encapsulation ppp
 ppp authentication chap pap
''',
#
'''
Configure the router to drop the PPP session on the SINT1 interface if more
than PERCENT percent of the traffic is dropped.
''':
'''
interface SINT1
 encapsulation ppp
 ppp quality REVPCNT
 ''',
 #
'''
Configure the router to use PPP with Predictor compression on interface SINT1.
''':
'''
interface SINT1
 encapsulation ppp
 compress predictor
 ''',
 #
'''
Router 'rtr-NAME1' is configured for PPP on its SINT1 interface.
Configure the router to automatically assign IP address 'RNDIP1'
to the connected device.
''':
'''
interface SINT1
 peer default ip address RNDIP1
''',
#
'''
Router 'rtr-NAME1' is configured for PPP on its SINT1 interface.
Configure the router to automatically receive its IP address as part
of the PPP link establishment process.
''':
'''
interface SINT1
 ip address negotiated
''',
#
'''
Router 'rtr-NAME1' is configured for PPP on its SINT1 interface.
Configure the router to automatically assign IP addresses via PPP from
the pool 'NAME2' with the range of IP addresses
from RNDIPRANGE1.
''':
'''
ip address-pool local
ip local pool NAME2 RNDIPRANGEst1 RNDIPRANGEen1

interface SINT1
 peer default ip address pool NAME2
''',
#
'''
Prevent the router from automatically installing a PPP host route to the
other end of the link on interface SINT1.
''':
'''
interface SINT1
 no peer neighbor-route
''',
#
'''
Router 'rtr-NAME1' is configured for PPP on its SINT1 interface.
Configure the router to automatically install a default route to its
connected peer on the SINT1 interface.
''':
'''
interface SINT1
 ppp ipcp route default
''',
#
'''
Configure the router to use PPP to bundle together interfaces SINT1 and SINT2
using bundle number 'RND100x1'. Configure the bundle with IP 'RNDIP1'
and the prefix '/RNDPFX1C'.
''':
'''
interface multilink RND100x1
 ip address RNDIP1 RNDPFX1M
 encapsulation ppp
 ppp multilink
 ppp multilink group RND100x1

 interface SINT1
  no ip address
  encapsulation ppp
  ppp multilink
  ppp multilink group RND100x1

 interface SINT2
  no ip address
  encapsulation ppp
  ppp multilink
  ppp multilink group RND100x1
''',
#
'''
Configure the PPP multilink bundle RND100x1 to go down if there are fewer
than RND24 operational interfaces.
''':
'''
interface multilink RND100x1
 ppp multilink min-links RND24 mandatory
 ''',
#
'''
Configure rtr-NAME1 as a PPPoE server.

-Assign addresses to connected clients from the local IP
  pool 'NAME2' in the range of 'RNDIPRANGE1'.
-Configure Virtual Template RND100x1 to use interface Loopback RND100x2
  for its IP address source.
-Loopback RND100x2's IP address is 'RNDIP1' with a /RNDPFX1C mask.
-Account for PPPoE overhead on the Virtual Template interface.
-Assign the EINT1 interface to the 'NAME3' PPPoE server.
''':
'''
ip local pool NAME2 RNDIPRANGEst1 RNDIPRANGEen1

interface loopback RND100x2
 ip address RNDIP1 RNDPFX1M

interface virtual-template RND100x1
 ip unnumbered loopback RND100x2
 peer default ip address pool NAME2
 mtu 1492
 ip tcp adjust-mss 1452

bba-group pppoe NAME3
 virtual-template RND100x1

interface EINT1
 pppoe enable group NAME3
''',
#
'''
Configure rtr-NAME1 as a PPPoE client on interface EINT1. The PPPoE
server will assign an IP address. Be sure to account for PPPoE overhead,
and ensure a default route toward the PPPoE server is installed automatically.
''':
'''
interface dialer 1
 encapsulation ppp
 ip address negotiated
 ppp ipcp route default
 mtu 1492
 ip tcp adjust-mss 1452
 dialer pool 1

interface EINT1
 pppoe-client dial-pool-number 1
''',
#

}
