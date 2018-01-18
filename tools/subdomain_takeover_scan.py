#!/usr/bin/python

import requests, sys, dns.resolver

input_file = sys.argv[1]
output_file = sys.argv[2]
is_closed = True

domains = open(input_file,'r').read().split('\n')

take_over_cnames = ["createsend",
"cargocollective",
"cloudfront",
"desk.com",
"fastly.net",
"feedpress.me",
"freshdesk.com",
"github.io",
"helpjuice.com",
"helpscoutdocs.com",
"herokudns.com",
"herokussl.com",
"herokuapp.com",
"pageserve.co",
"pingdom.com",
"amazonaws.com",
"myshopify.com",
"stspg-customer.com",
"sgizmo.com",
"surveygizmo.eu",
"sgizmoca.com",
"sgizmoca.com",
"tictail.com",
"domains.tumblr.com",
"uservoice.com",
"wpengine.com",
"squarespace.com",
"unbounce.com",
"zendesk.com"]

take_over_content = ["<strong>Trying to access your account",
"Use a personal domain name",
"The request could not be satisfied",
"Sorry, We Couldn't Find That Page",
"Fastly error: unknown domain",
"The feed has not been found",
"You can claim it now at",
"Publishing platform",                        
"There isn't a GitHub Pages site here",                       
"No settings were found for this company",
"<title>No such app</title>",                        
"You've Discovered A Missing Link. Our Apologies!",
"Sorry, couldn&rsquo;t find the status page",                        
"NoSuchBucket",
"Sorry, this shop is currently unavailable",
"<title>Hosted Status Pages for Your Company</title>",
"data-html-name=\"Header Logo Link\"",                        
"<title>Oops - We didn't find your site.</title>",
"class=\"MarketplaceHeader__tictailLogo\"",                        
"Whatever you were looking for doesn't currently exist at this address",
"The requested URL was not found on this server",
"The page you have requested does not exist",
"This UserVoice subdomain is currently available!",
"but is not configured for an account on our platform",
"<title>Help Center Closed | Zendesk</title>"]

print("\n-- Checking possible subdomain take overs in "+input_file+" with output file, "+output_file+" --\n")


for domain in domains:
	#Skip first row, lol
	if domain != domains[0]:
		found_content = False
		found_cname = False
		try:
			r=requests.get("http://"+domain, timeout=5).text
		except:
			print("[-]Error in http://"+domain)

		for content in take_over_content:
			if str(content) in r:
				found_content = True

		try:
			cnames = dns.resolver.query(domain, 'CNAME')
			for cname in cnames:
    				for cname_url in take_over_cnames:
					if str(cname_url) in str(cname.target):
						found_cname = True

			if found_cname and found_content:
				print("[+]"+domain)
				if is_closed:
					file = open(output_file,"w+")
					is_closed = False
				file.write(domain+"\n")
			else:
				print("[-]"+domain)
		except:
			print "[-]No cnames for "+domain

if is_closed == False:
	file.close()

print("\n-- Done --")












