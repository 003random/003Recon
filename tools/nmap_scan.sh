#!/bin/bash

printf "\n-- Scanning services from $1 with output file, $2 --\n"
echo "-- This might take around $((`wc -l < $1` / 1)) minutes --"

while read domain; do
    echo "-- $domain --"
    $3/nmap -sV $domain | sed -n '/PORT/,/report/p' | awk -F"Service" '{print $1}'
done < $1  >> $2

echo "-- Done --"


