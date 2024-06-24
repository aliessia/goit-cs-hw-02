#!/bin/bash


websites=("https://google.com" "https://facebook.com" "https://twitter.com")


logfile="website_status.log"

> $logfile

for site in "${websites[@]}"; do
  response=$(curl -o /dev/null -s -w "%{http_code}" -L "$site")
  
  if [ "$response" -eq 200 ]; then
    echo "$site is UP" | tee -a $logfile
  else
    echo "$site is DOWN" | tee -a $logfile
  fi
done


echo "Результати перевірки записані у файл $logfile"
