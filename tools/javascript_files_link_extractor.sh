#!/bin/bash

printf "\n-- Extracting links out of javascript files in $1 with output file, $2  --\n"

if [ ! -f $1 ]; then
    printf  "\n[-]File not found!"
else
    while read domain; do 
        if [[ $domain == "-"* ]]; then
            printf  "\n\n\n[+]-$domain--"
        else
            if [ -z "$domain" ]; then
                printf "\n[-]Invalid domain $domain"
            else
                printf "\n[+]$domain \n"
		echo "----------------------"
                command="ruby $3 $domain"
                eval $command
            fi
        fi
    done < $1 >> $2
printf "\n -- Done -- \n"
fi
