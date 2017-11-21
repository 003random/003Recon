#!/usr/bin/python
import requests,sys

def start():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    payload_file = sys.argv[3]

    print("\n-- Testing open redirects on domains in "+input_file+" with output file, "+output_file+" --")

    is_closed = True

    payloads = open(payload_file,'r').read().split('\n')

    #First loop trough the payloads to prevent 429 (rate limit)
    for payload in payloads: 
        domains = open(input_file,'r').read().split('\n')   
        print "\n - Trying payload "+payload+" - "
        for domain in domains:
            if domain != "":

                url = "https://" + domain + payload
                url = url.strip()
            
                try:
                    r = requests.head(url, allow_redirects=True, timeout=5)
                except:
                    print "[-]Error on " + url

                if r.history:  
                    if r.url == "https://example.com":
                        print "[+]"+url
                        if is_closed:
                            file = open(output_file,"w+")
                        is_closed = False
                        file.write(url + "\n")
                    else:
                        print "[-]"+url
                else:
                    print "[-]"+url
        else:
            print "[-]Domain is invalid"

    if is_closed == False:
        file.close()
    print("\n-- Done --")

start()

