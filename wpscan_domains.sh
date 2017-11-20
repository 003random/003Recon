#!/bin/bash

printf "\n-- Starting a wpscan for the domains in $1 --\n\n"

if [ ! -f $1 ]; then
    echo "[-]File not found!"
else
    while read domain; do 
        echo "[+]Opening $domain"
        xterm -hold -e "/home/YOUR_USER/Documents/Tools/wpscan/wpscan.rb --url https://$domain" &
    done < $1
fi
printf "\n -- Done -- \n"
