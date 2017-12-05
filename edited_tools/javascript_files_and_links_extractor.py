#!/usr/bin/python
#This is an edit of /tools/javascript_files_extractor.py and /tools/javascript_files_link_extractor.sh
#it combines those 2 and takes 1 domain as string as argument 1. not a domain file

import re, requests, sys, os

input_string = sys.argv[1]
output_file = sys.argv[2]
extractor_file = sys.argv[3]

print("\n-- Extracting javascript links from "+input_string+" with output file, "+output_file+" --\n")


black_listed_domains = ["ajax.googleapis.com",
                        "cdn.optimizely.com",
                        "googletagmanager.com",
                        "fontawesome.com"]

if input_string is not "":
	domain = input_string
	domain_written = False
	i = 0
	b_amount = 0
	full_domain = ""
	if domain != "":
		matches = ""
		r = ""
		regex = r'script src="(.*?)"'
		try:
			r = requests.get("http://"+domain).content
		except:
			print "[-]Error in http://"+domain

		matches = re.findall(regex, r, re.MULTILINE)
		if matches == []:
			regex = r"script src='(.*?)'"
			matches = re.findall(regex, r, re.MULTILINE)

		for m in matches:
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
				os.system("echo '"+full_domain + ": \n\r ' >> " + output_file)
				os.system("ruby " + extractor_file + " " + full_domain + " >> " + output_file)


print("\n-- Done --")
