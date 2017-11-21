    home_dir="/home/003random/Tools/recon" # Change to your own directory!

    output_dir="output"
    tools_dir="tools"
    payloads_dir="payloads"
    dependencies_dir="dependencies"  
    screenshots_dir="$output_dir/$@/screenshots"  

    [ -d $output_dir ] || mkdir $output_dir;
    [ -d $dependencies_dir ] || mkdir $dependencies_dir; git clone https://github.com/aboul3la/Sublist3r.git $dependencies_dir/sublister; git clone https://github.com/wpscanteam/wpscan.git $dependencies_dir/wpscan; git clone https://github.com/jobertabma/relative-url-extractor.git $dependencies_dir/relative-url-extractor; git clone https://github.com/maaaaz/webscreenshot.git $dependencies_dir/webscreenshot;



    all_domains_file="$output_dir/$@/domains-all.txt"
    domains_file="$output_dir/$@/domains.txt"
    crlf_file="$output_dir/$@/crlf.txt"
    open_redirects_file="$output_dir/$@/open_redirects.txt"
    nmap_scan_file="$output_dir/$@/nmap_scans.txt"
    wordpress_file="$output_dir/$@/wordpress_sites.txt"
    headers_file="$output_dir/$@/sensitive_headers.txt"
    subdomain_take_over_file="$output_dir/$@/sub_take_over.txt"
    javascript_files_file="$output_dir/$@/javascript_files.txt"
    javascript_extracted_urls="$output_dir/$@/extracted_urls.txt"
    error_page_info_file="$output_dir/$@/error_page_info.txt"
    cors_file="$output_dir/$@/misconfigured_cors.txt"

    crlf_payload_file="$payloads_dir/crlf.txt"
    error_pages_payload_file="$payloads_dir/error_pages.txt"
    headers_payload_file="$payloads_dir/sensitive_headers.txt"
    open_redirect_payload_file="$payloads_dir/sensitive_headers.txt"

    
    wpscan_location="dependencies/wpscan"
    url_extractor_location="dependencies/relative-url-extractor"
    sublister_location="dependencies/sublister"
    webscreenshot_location="dependencies/webscreenshot"

    cd $home_dir/$output_dir;
    rm -rf $@; 
    mkdir $@; 
    cd ../

    printf "\n -- $@ Started -- \n"

    python $sublister_location/sublist3r.py -o $all_domains_file -d $@;
    python $tools_dir/online.py $all_domains_file $domains_file;
    $tools_dir/crlf.sh $domains_file $crlf_file $crlf_payload_file;
    $tools_dir/cors_misconfiguration_scan.sh $domains_file $cors_file;
    python $tools_dir/open_redirect.py $domains_file $open_redirects_file $open_redirect_payload_file;
    python $tools_dir/header_scan.py $domains_file $headers_file $headers_payload_file;
    python $tools_dir/error_page_info_check.py $domains_file $error_page_info_file $error_pages_payload_file;
    python $tools_dir/subdomain_takeover_scan.py $domains_file $subdomain_take_over_file;
    python $tools_dir/javascript_files_extractor.py $domains_file $javascript_files_file;
    $tools_dir/javascript_files_link_extractor.sh $javascript_files_file $javascript_extracted_urls $url_extractor_location/extract.rb;
    python $webscreenshot_location/webscreenshot.py -i $domains_file -o $screenshots_dir;
    python $tools_dir/wordpress_check.py $domains_file $wordpress_file;
    $wpscan_location/wpscan.rb --update;
    $tools_dir/wpscan_domains.sh $wordpress_file;
    $tools_dir/nmap_scan.sh $domains_file $nmap_scan_file;
    
    printf "\n -- $@ Finished -- \n"
