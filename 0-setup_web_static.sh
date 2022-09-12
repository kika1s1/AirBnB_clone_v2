#!/usr/bin/env bash
# sets up web servers for deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo -e "This is a test" | sudo tee -a /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

static="\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n}"
sudo sed -i "38i\ $static" /etc/nginx/sites-available/default

sudo service nginx restart
