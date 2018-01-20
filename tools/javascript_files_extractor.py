#!/usr/bin/python

import re, requests, sys

input_file = sys.argv[1]
output_file = sys.argv[2]

print("\n-- Extracting javascript files from domains in "+input_file+" with output file, "+output_file+" --\n")

domains_file = open(input_file,'r')
domains = domains_file.read().split('\n')

file = open(output_file,"w+")

black_listed_domains = ["ajax.googleapis.com",
                        "cdn.optimizely.com",
                        "googletagmanager.com",
                        "fontawesome.com"]

for domain in domains:
	domain_written = False
	i = 0
	b_amount = 0
	full_domain = ""
	if domain != "":
		matches = ""
		r = ""
		regex = r'<script.*src=[\'|"]([^\'"]*)[\'|"]'
		try:
			r = requests.get("http://"+domain).content
		except:
			print "[-]Error in http://"+domain

		matches = re.findall(regex, r, re.MULTILINE)

		for m in matches:
			if domain_written != True:
				file.write("\n-"+domain+"\n")
				domain_written = True
	
			black_listed = False
			for b in black_listed_domains:
				if b in m:
					black_listed = True

			if black_listed != True:
				if m.startswith("/"):
					if m.startswith("//"):
						full_domain = "https:"+m
					else:
						full_domain = "https://"+domain+m
				elif m.startswith("http"):
					full_domain = m
				else:
					full_domain = "https://"+domain+"/"+m
			else:
				b_amount += 1

			if black_listed != True:
				i += 1
				file.write(full_domain+"\n")
		print "[+]"+str(i)+" scripts, "+str(b_amount)+" blacklisted in "+domain
	else:
		print "[-]Domain is invalid " + domain



file.close()
domains_file.close()

print("\n-- Done --")
