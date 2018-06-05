#!/usr/bin/python

import sys, requests

input_file = sys.argv[1]
output_file = sys.argv[2]

input_file_open = open(input_file, 'r')
output_file_open = open(output_file, 'w+')

domains = input_file_open.readlines()

print("\n-- Writing online hosts in "+input_file+" to "+output_file+" --\n")


def available(domain):
        try:
                r = requests.get(domain, timeout=3)
                return True
        except:
                return False

for domain in domains:
        domain = domain.strip()

        http = available("http://" + domain)
        https = available("https://" + domain)

        if http == True or https == True:
                print("[+]" + domain.strip())
                output_file_open.write(domain+"\n")
        else:
                print("[-]" + domain.strip())


input_file_open.close()
output_file_open.close()
print("\n-- Done --")
