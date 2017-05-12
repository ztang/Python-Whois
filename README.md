# Python Whois Website

A simple whois script written in Python with the support of Flask.

I've tried `whois`, `python-whois` module etc. from pypi, but no one satisfy my requirements. 
And I found the whois tool from Ubuntu is very useful. So I get 
whois information from Ubuntu shell. 

**Only support Ubuntu OS now.**

**Support all tlds.**

Visit http://wxapp.me for a demo.

## Deployment

Requirements:

 - Ubuntu >= 16.04LTS
 - Python 2.7

Install dependency:

 - sudo apt install whois
 - pip install flask
 
Install a web server. You can choose apache, nginx or whatever you like.

Configura the web server.

For more deployment options, see:http://flask.pocoo.org/docs/0.12/deploying/

Or you can just run this script with `nohup` and redirect the domain name to `localhost:5000`

    nohup python -u pywhois.py > out.log 2>&1 &

Here is my example conf file for apache server:

    <VirtualHost *:80>
    ServerName YOURDOMAIN.NAME
    ServerAlias YOURDOMAIN.NAME www.YOURDOMAIN.NAME
    ProxyPass / http://localhost:5000/
    ProxyPassReverse / http://localhost:5000/
    ErrorLog  /data/wwwlog/YOURDOMAIN.NAME/error.log
    TransferLog  /data/wwwlog/YOURDOMAIN.NAME/access.log
    </VirtualHost>

## Usage

This tool support two usages:
 - Search whois information directly through home page
 - Get whois information with '/whois/your_domain'
 
 ## TODO
 
 - Input check.
 - Whois information extract.
 - Error detection.
 - Rewrite the templates.
 
 ## Contact
 
 Email: mail@ztang.com
 
 ## Changelog
 
[0.3] - 2017-05-12
 - Rebuild with Python.
 - Change the whois lookup method.
 - Support all tlds.

[0.2] - 2015-12-10
 - Rebuild the page with Bootstrap.
 - Fix some problems with domain lookup.
 - Add some common tlds.

[0.1] - 2014-07-19
 - Whois Lookup online.
