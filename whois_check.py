# -*- coding: utf-8 -*-

import subprocess as sp

def get_whois(domain_name):
    try:
        whois_info = sp.check_output('whois %s' % domain_name, shell=True)
        return whois_info
    except sp.CalledProcessError:
        return 'Domain Input Error'


if __name__ == '__main__':

    dn = 'tang.com'
    dn_whois = get_whois(dn)
    dn_error = get_whois('ttt')
    print dn_error
    #print dn_whois
    #print type(dn_whois)
    dn_whois = dn_whois.replace('\n', '<br>')
    #print dn_whois