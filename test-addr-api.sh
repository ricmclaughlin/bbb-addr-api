#!/usr/bin/env bash

URL="http://127.0.0.1:3000/address?q="
OUTPUT_FILE=$(date +%s)'.json'

uuid='&rid='$(uuidgen)
curl $URL'1863%20Union%20Ave'$uuid > $OUTPUT_FILE
echo "\n" >> $OUTPUT_FILE

uuid='&rid='$(uuidgen)
curl $URL'12497%20Leopard%20St%2078410'$uuid >> $OUTPUT_FILE
echo "\n" >> $OUTPUT_FILE
