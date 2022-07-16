# Feedparser
Repo: https://github.com/kurtmckee/feedparser

Install: `pip install feedparser`

# Install

## As root, do the following
```
apt update && apt upgrade
apt install nginx python3-feedparser
systemctl start nginx
curl -O https://raw.githubusercontent.com/arildjensen/acs/main/simple-alert-website/generate-site.py
mv generate-site.py /usr/local/bin
```

## Add to crontab
`* * * * * cd /var/www.html && python /usr/local/bin/generate-site.py`