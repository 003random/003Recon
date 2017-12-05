#!/bin/bash
#This script uses wpscan that is installed in the dependencies folder

printf "\n-- Starting a wpscan for the domains in $1 --\n\n"

if [ ! -f $1 ]; then
    echo "[-]File not found!"
else
    while read domain; do 
        echo "[+]Opening $domain"
        xterm -hold -e "$2 --url https://$domain" &
    done < $1
fi
printf "\n -- Done -- \n"
