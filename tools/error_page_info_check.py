#!/usr/bin/python

import requests, sys

input_file = sys.argv[1]
output_file = sys.argv[2]
payload_file = sys.argv[3]
is_closed = True

domains = open(input_file,'r').read().split('\n')
info = [line.rstrip('\n').lower() for line in open(payload_file)]

print("\n-- Checking for sensitive info in error pages "+input_file+" with output file, "+output_file+" --")

payloads = ["/",
            "/NotFound123",
            "/.htaccess",
            "/<>"]

for payload in payloads:
    print "\n - Trying payload "+payload+" - "
    for domain in domains:
        info_found = ""
        if domain != "":
            found = False
            try:
                response = requests.get("http://"+domain+payload)
            except:
                print("[-]Error on http://"+domain+payload)
            for i in info:
                if i.lower() in response.content.lower():
                    found = True
                    #Search and get the line in the response that contains i.lower()
                    info_found = [x for x in [x.lower() for x in response.content.split("\n")] if i.lower() in x]

            if found:
                if is_closed:
                    file = open(output_file,"w+")
                is_closed = False
                print("[+]"+domain+payload+" - "+str(info_found))
                file.write(domain + payload +" - "+str(info_found)+ "\n")
            else:
               print("[-]"+domain+payload+" - "+str(info_found))
                
        else:
            print("[-]Domain is invalid")
        
if is_closed == False:
    file.close()

print("\n-- Done --")
