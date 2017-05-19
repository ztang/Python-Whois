# -*- coding: utf-8 -*-


from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from whois_check import get_whois
import sys


# fix the problem of chinese
reload(sys)
sys.setdefaultencoding('utf-8')


app = Flask(__name__)

#bootstrap_css = url_for('static', filename='css/bootstrap.css')

@app.route('/')
def index():
    return render_template('whois_info.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/whois', methods=['POST'])
def whois_check():
    domain_name = request.form['domain_name']
    dn_info_str = get_whois(domain_name)
    dn_info = dn_info_str.replace('\n', '<br>')
    return render_template('whois_info.html', dn_info=dn_info, dn_value=domain_name)

@app.route('/whois/<domain_name>')
def whois_info(domain_name):
    dn_info_str = get_whois(domain_name)
    dn_info = dn_info_str.replace('\n', '<br>')
    return render_template('whois_info.html', dn_info=dn_info, dn_value=domain_name)


if __name__ == '__main__':
    app.run()
