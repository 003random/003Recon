#!/usr/bin/python

import httplib
import socket
import re
import sys

def online(host):
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        return False
    else:
        return True

def available(host, path="/"):
    try:
        conn = httplib.HTTPConnection(host, timeout=5)
        conn.request("HEAD", path)
        if re.match("^[23]\d\d$", str(conn.getresponse().status)):
            return True
    except StandardError:
        return False

input_file = sys.argv[1]
output_file = sys.argv[2]

input_file_open = open(input_file, 'r')
output_file_open = open(output_file, 'w+')

domains = input_file_open.readlines()

print("\n-- Writing online hosts in "+input_file+" to "+output_file+" --\n")

for domain in domains:
    domain = domain.strip()
    if online(domain) == True and available(domain) == True:
        print("[+]"+domain.strip())
        output_file_open.write(domain+"\n")
    else:
        print("[-]"+domain)

input_file_open.close()
output_file_open.close()
print("\n-- Done --")
