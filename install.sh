#!/usr/bin/env bash

dependencies_dir="dependencies"  
output_dir="output"

mkdir $output_dir;
#mkdir -p $dependencies_dir/phantomjs; 
   
# Install sublis3r   
git clone https://github.com/aboul3la/Sublist3r.git $dependencies_dir/sublister; 

# Install wpscan
git clone https://github.com/wpscanteam/wpscan.git $dependencies_dir/wpscan; 

# Install Relative-URL-Extractor
git clone https://github.com/jobertabma/relative-url-extractor.git $dependencies_dir/relative-url-extractor; 

# Install WebScreenShot
git clone https://github.com/maaaaz/webscreenshot.git $dependencies_dir/webscreenshot; 

# Install PhantomJS
#wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 -O $dependencies_dir/phantomjs/phantomjs-2.1.1-linux-x86_64.tar.bz2
#tar xvjf $dependencies_dir/phantomjs/phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/
#ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/
    
 # Install Nmap
git clone https://github.com/nmap/nmap.git $dependencies_dir/nmap
cd $dependencies_dir/nmap;
./configure;
make;
make install;
cd ../../;
