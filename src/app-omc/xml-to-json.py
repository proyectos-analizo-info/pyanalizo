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

import sys
sys.path.append('../shared')
import functions as f
import omc, os

def main():
    
    args = sys.argv[1:] # 0 - script name
    
    n = '\n'
    
    if len(args) == 2:
        
        d_all_xml_element_attributes, l_noticias = omc.parse_xml(args[0], args[1]) # Hoja1, item_noticia_enero2014, item_noticia_febrero2014, item_noticia_marzo2014
        
        output = []
        
        n = '\r\n'
        t = '\t'
        
        output.append(f.encode_utf_8(t.join(omc.tags) + n))
        
        f_dir = args[1] + '_json/'
        
        os.system('mkdir -p ' + f_dir)
        
        for d_noticia in l_noticias:
            
            print d_noticia['ID']
            print d_noticia['URL']
            print
            
            for attribute in d_all_xml_element_attributes:
                
                if attribute not in d_noticia:
                    
                    d_noticia[attribute] = 'NUL'
                
            f.write_json_file(f_dir + d_noticia['ID'] + '.json', d_noticia, {'clasp': False})
        
        print d_all_xml_element_attributes
    else:
        
        print n, 'Provide one .xml file and the item tag', n
    

if __name__ == '__main__':
    main()
