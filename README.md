## Description

This repository contains some of my scripts that i created to automate alot of my recon and scanning.
These files are free to take, edit and share.

### Install:  
git clone https://github.com/003random/003Recon.git;  
cd 003Recon;  
chmod 777 install.sh;  
./install.sh;  

#And then call it with:  

./recon.sh example.com  
  
  
This tools does the following things;  
1. Get subdomains of a domain    
2. Filter out only online domains    
3. Scan the domains for CRLF    
4. Check for a CORS misconfiguration  
5. Test for open redirects  
6. Grab sensitive headers  
7. Get senstive info from error pages  
8. Check for subdomain takeovers  
9. Extract javascript files  
10. Feed the javascript files into 'relative-url-extractor'  
11. Screenshot all domains  
12. Check if sites run wordpress  
13. Start a wpscan on the wordpress sites  
14. Do a nmap service scan  

All out will get saved in a folder named by the domain, in the output folder.   
In this folder it will create files with the discovered content.  
  
# 
*Created by [003random](http://hackerone.com/003random) - [@003random](https://twitter.com/rub003) - [003random.com](https://poc-server.com/blog/)*
