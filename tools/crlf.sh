#!/bin/bash

printf "\n-- Testing crlf on domains in $1 with output file, $2 -- \n\n"

#First loop trough the payloads to prevent 429 (rate limit)
while read payload; do 
    while read domain; do 
        if curl -vs "$domain/$payload" 2>&1 | grep -i '^< Set-Cookie: crlf' &> /dev/null; then 
            echo "[+]$domain/$payload"
            echo "$domain/$payload" >> $2
        else
            echo "[-]$domain/$payload"
        fi
    done < $1
done < $3 

printf "\n-- Done --"
#Credits to Tomnomnom for the help

