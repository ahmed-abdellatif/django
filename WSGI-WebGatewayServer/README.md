# Quickstart-WSGI-Application
A simple server connection using barebones python
# Installing nginx

"An open source software for web serving"
Source for Installing on Mac:
https://coderwall.com/p/dgwwuq/installing-nginx-in-mac-os-x-maverick-with-homebrew

1. brew install nginx
2. Sudo nginx
3. Test at https://localhost:8080
# Default place of configuration on Mac: 

/usr/local/etc/nginx/nginx.conf

vim /usr/local/etc/nginx/nginx.conf

If you'd like to actually see a WSGI app run, it's easy to do. First you'll need a WSGI compliant server. Here is 
uWSGI, which has a simple command line interface. It can be installed by running: 

`pip install uwsgi`

Run the python script called server.py. You can run the uWSGI server by typing this on the command line:

`uwsgi --http :8080 --wsgi-file server.py`

Now you can visit: 

http://localhost:8080

to see the script
