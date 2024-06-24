#!/bin/bash

# Список вебсайтів
websites=("https://google.com" "https://facebook.com" "https://twitter.com")

# Назва файлу логів
log_file="website_status.log"

# Очищення файлу логів
> $log_file

# Перевірка доступності вебсайтів
for website in "${websites[@]}"
do
  response=$(curl -s -o /dev/null -w "%{http_code}" -L $website)
  echo "Checking $website, Response code: $response"

  if [ "$response" -eq 200 ]; then
    echo "[$website] is UP" | tee -a $log_file
  else
    echo "[$website] is DOWN" | tee -a $log_file
  fi
done

echo "Results have been written to $log_file"

