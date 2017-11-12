'''
This file contains the various tasks, along with the configuration solutions.
The tasks are in dictionary format, with the task (question) as the key, and
the solution (answer) as the value.

Variables and meanings used inside the strings in this file:
These variables get passed to randomvar.py and are replaced with actual values.

These are just for quick easy personal reference, you should change these to whatever
 is appropraite for you.
 
SINT(1 - 4) = serial interface
EINT(1 - 8) = ethernet interface
USERNAME
PASSWORD
HOSTNAME(1 - 10)

Key/Value pairs below are separated with a #. This is just for visual clarity.

'''

tasks = {
'Configure the serial interface using a Cisco-proprietary encapsulation.\n': 'encapsulation hdlc\n',
#
'Configure the serial interface using a standard (non-frame-relay) encapsulation.\n': 'encapsulation ppp\n',
#
'Configure the synchronous serial interface to use the default encapsulation.\n': 'encapsulation hdlc\n',
#
'''
Configure the router to request PAP authentiction on the SINT1 interface.
The expected username is USERNAME, and the expected password is PASSWORD.
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
via PAP with the username USERNAME, and the password PASSWORD.
''':
'''
interface SINT1
 encapsulation ppp
 ppp pap sent-username USERNAME password PASSWORD
''',
#
'''
Configure the router to authenticate its neighbor on the SINT1 interface
via CHAP with the username USERNAME, and the password PASSWORD.
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
via CHAP. The router's hostname is rtr-HOSTNAME1. The neighbor
(rtr-HOSTNAME2) has already been properly configured. It uses the password
PASSWORD for CHAP authentication.
''':
'''
username rtr-HOSTNAME2 password PASSWORD
interface SINT1
 encapsulation ppp
 ppp authentication chap
 ppp chap hostname rtr-HOSTNAME1
''',
#


}
