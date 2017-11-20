#!/bin/bash
    
all_domains_file="domains-all"
domains_file="domains"
crlf_file="crlf"
open_redirects_file="redirects"
nmap_scan_file="nmap_scans"
screenshots_folder="screenshots"
wordpress_file="wordpress_sites"
headers_file="sensitive_headers"
subdomain_take_over_file="sub_take_over"
javascript_files_file="javascript_files"
javascript_extracted_urls="extracted_urls"
error_page_info_file="error_page_info"
cors_file="misconfigured_cors"

rm -rf ~/Desktop/$@; 
mkdir ~/Desktop/$@; 
cd ~/Desktop/$@; 
python ~/Documents/Tools/Sublist3r/sublist3r.py -o $all_domains_file -d $@;
python ~/Documents/Tools/online.py $all_domains_file $domains_file;
~/Documents/Tools/crlf.sh $domains_file $crlf_file;
~/Documents/Tools/cors_misconfiguration_scan.sh $domains_file $cors_file;
python ~/Documents/Tools/open_redirect.py $domains_file $open_redirects_file;
python ~/Documents/Tools/header_scan.py $domains_file $headers_file
python ~/Documents/Tools/error_page_info_check.py $domains_file $error_page_info_file;
python ~/Documents/Tools/subdomain_takeover_scan.py $domains_file $subdomain_take_over_file;
python ~/Documents/Tools/javascript_files_extractor.py $domains_file $javascript_files_file
~/Documents/Tools/javascript_files_link_extractor.sh $javascript_files_file $javascript_extracted_urls
python ~/Documents/Tools/webscreenshot/webscreenshot.py -i $domains_file -o $screenshots_folder
python ~/Documents/Tools/wordpress_check.py $domains_file $wordpress_file
~/Documents/Tools/wpscan/wpscan.rb --update
~/Documents/Tools/wpscan_domains.sh $wordpress_file
~/Documents/Tools/nmap_scan.sh $domains_file $nmap_scan_file;