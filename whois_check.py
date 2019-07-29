# -*- coding: utf-8 -*-

import subprocess as sp
import re

def get_whois(domain_name):
    try:
        domain_name_match = re.match(r'[a-zA-Z0-9][-a-zA-Z0-9]{0,62}\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62}', domain_name)
        domain_name_match_www = re.match(r'[a-zA-Z0-9][-a-zA-Z0-9]{0,4}\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62}\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62}', domain_name)
        if domain_name_match == None:
            return 'Input Error \n Please input correct domain name!'
        else:
            if domain_name_match_www == None:
                domain_name = domain_name_match.group()
            else:
                dnw = domain_name_match_www.group()
                domain_name = dnw.split('.')[1]+ '.' + dnw.split('.')[2]
            whois_info = sp.check_output('whois %s' % domain_name, shell=True)
            return whois_info
    except sp.CalledProcessError as e:
        return e.output


if __name__ == '__main__':

    dn = 'tang.com'
    dn_whois = get_whois(dn)
    dn_error = get_whois('ttt')
    print(dn_error)
    #print dn_whois
    #print type(dn_whois)
    dn_whois_check = dn_whois.decode('utf-8')
    if re.match(r'\n', dn_whois_check) != None:
        dn_whois = dn_whois.encode().replace('\n', '<br>')
    #print dn_whois
