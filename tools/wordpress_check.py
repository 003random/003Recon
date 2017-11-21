#!/usr/bin/python

import requests, sys

input_file = sys.argv[1]
output_file = sys.argv[2]
is_closed = True

domains = open(input_file,'r').read().split('\n')

print("\n-- Checking for wordpress sites in "+input_file+" with output file, "+output_file+" --\n")

for domain in domains:
    if domain != "":
        try:
            response = requests.get("https://"+domain)
        except:
            print("[-]Error on https://"+domain)

        if "/wp-content/" in response.content:
            if is_closed:
                file = open(output_file,"w+")
            is_closed = False
            print("[+]"+domain)
            file.write(domain + "\n")
        else:
            print("[-]"+domain)
    else:
        print("[-]Domain is invalid")
        
if is_closed == False:
    file.close()

print("\n-- Done --")
