#!/bin/bash
TOKEN=$(curl -d "username=$USERNAME&password=$PASSWORD" http://cotapi:8000/token | python3 -c "import sys, json; token = json.load(sys.stdin); print(token['access_token'])"); 
curl --header "Authorization: Bearer $TOKEN" http://cotapi:8000/transactions/update >> /home/update_log.txt; 
echo "\n" >> /home/update_log.txt