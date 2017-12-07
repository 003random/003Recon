    dependencies_dir="dependencies"  
    dependencies_dir="output"  


    mkdir $output_dir;
    mkdir $dependencies_dir; 
    git clone https://github.com/aboul3la/Sublist3r.git $dependencies_dir/sublister; 
    git clone https://github.com/wpscanteam/wpscan.git $dependencies_dir/wpscan; 
    git clone https://github.com/jobertabma/relative-url-extractor.git $dependencies_dir/relative-url-extractor; 
    git clone https://github.com/maaaaz/webscreenshot.git $dependencies_dir/webscreenshot; 
    git clone https://github.com/nmap/nmap.git $dependencies_dir/nmap
    cd $dependencies_dir/nmap;
    ./configure;
    make;
    make install;
    cd ../../;
