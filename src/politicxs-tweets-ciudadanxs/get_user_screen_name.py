#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

if __name__ == '__main__':
    
    n = '\n'
    
    print 'parsing html...'
    
    f_file = open('congreso_de_los_diputados.html', 'r')
    
    web_page = BeautifulSoup(f_file)
    
    f_file.close()
    
    diputados = {}
    
    # <li class="mention-text pretty-link not-blocked"><button class="dropdown-link" type="button">Twittear a @cesarluena</button></li>
    
    for line in web_page.find_all('li', {'class':'mention-text pretty-link not-blocked'}):
        
        diputados[((str(line).split('Twittear a ')[1]).split('</button></li>')[0]).strip()] = ''
    
    f_out = 'diputados.txt'
    
    f_file = open(f_out, 'w')
    
    for user in diputados.keys():
        
        f_file.write(user + n)
        
    f_file.close()
    
    print f_out, '(' + str(len(diputados.keys())) + ')'
