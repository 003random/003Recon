import requests, sys

input_file = sys.argv[1]
output_file = sys.argv[2]

print("\n-- Testing for sensitive info in headers on domains in "+input_file+" with output file, "+output_file+" --\n")

is_closed = True
domains = open(input_file,'r').read().split('\n')
headers = [line.rstrip('\n').lower() for line in open('/home/rjp/Documents/Wordlists/headers.txt')]

for domain in domains:
	if domain != "":
		try:
			r = requests.head("https://"+domain, timeout=5)
		except:
			print("[-]Error on https://"+domain)
		headers_found = []

		for header in headers:
			current_header = r.headers.get(header.lower())
			if current_header != None:
				headers_found.append(str(current_header))
		if headers_found != []:
			if is_closed:
        			file = open(output_file,"w+")
				is_closed = False
			print("[+]"+domain+" - "+str(headers_found))
			file.write(domain+" - "+str(headers_found)+"\n")
		else:
			print("[-]"+domain+" - "+str(headers_found))
	else:
            print "[-]Domain is invalid"

if is_closed == False:
	file.close()

print("\n-- Done --")
