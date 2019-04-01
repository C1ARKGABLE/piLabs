#!/usr/bin/env python3

import subprocess

ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)

print('My IP address is %s' % ip_address.decode('utf-8'))
