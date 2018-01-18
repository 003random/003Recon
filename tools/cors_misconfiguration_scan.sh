#!/bin/bash

printf "\n-- Scanning for misconfigured cors headers in $1 with output file, $2 --\n\n"

if [ ! -f $1 ]; then
    echo "[-]File not found!"
else
    while read domain; do
        for origin in https://evil.com null https://$domain.evil.com https://${domain}evil.com https://evil${domain}; do
            if curl -vs "$domain" -H"Origin: $origin" 2>&1 | grep -i "< Access-Control-Allow-Origin: $origin" &> /dev/null; then
                echo "[+](Access-Control-Allow-Origin) $domain [$origin]"
                echo "(Access-Control-Allow-Origin) $domain [$origin]" >> $2

                if curl -vs "$domain" -H"Origin: $origin" 2>&1 | grep -i '< Access-Control-Allow-Credentials: true' &> /dev/null; then
                    echo "[+](Allow-Credentials) $domain [$origin]"
                    echo "(Allow-Credentials) $domain [$origin]" >> $2
                fi
            else
                echo "[-]$domain [$origin]"
            fi
        done
    done < $1 
fi

printf "\n -- Done -- \n"
