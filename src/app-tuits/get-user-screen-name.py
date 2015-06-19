#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''

from bs4 import BeautifulSoup

def main():
    
    n = '\n'
    
    print 'parsing html...'
    
    f_file = open('congreso-de-los-diputados.html', 'r')
    
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

if __name__ == '__main__':
    main()
