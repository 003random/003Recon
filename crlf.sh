#!/bin/bash

printf "\n-- Testing crlf on domains in $1 with output file, $2 -- \n\n"

green="tput setaf 2"
reset="tput sgr0"

#First loop trough the payloads to prevent 429 (rate limit)
while read payload; do 
    while read domain; do 
        if curl -vs "$domain/$payload" 2>&1 | grep -i '^< Set-Cookie: crlf' &> /dev/null; then 
            echo "${green}[+]${reset}$domain/$payload"
            echo "$domain/$payload" >> $2
        else
            echo "[-]$domain/$payload"
        fi
    done < $1
done < ~/Documents/Wordlists/crlf.txt 

printf "\n-- Done --"

