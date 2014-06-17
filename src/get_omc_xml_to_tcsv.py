#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('./shared')
import functions as f
import omc_xml_parser as xml

if __name__ == "__main__":
    
    args = sys.argv[1:] # 0 - script name
    
    n = '\n'
    
    if len(args) == 1:
        
        d_all_xml_element_attributes, l_noticias = xml.parse_xml(args[0], args[1]) # Hoja1, item_noticia_enero2014, item_noticia_febrero2014, item_noticia_marzo2014
        
        output = []
        
        t = '\t'
        n = '\r\n'
        
        output.append(f.encode_utf_8(t.join(xml.tags) + n))
        
        for d_noticia in l_noticias:
            
            print d_noticia['ID']
            print d_noticia['URL']
            print
            
            for attribute in d_all_xml_element_attributes:
                
                if attribute not in d_noticia:
                    
                    d_noticia[attribute] = 'NUL'
                
            l_tags = []
            
            for tag in xml.tags:
                
                l_tags.append(d_noticia[tag])
                
            output.append(f.encode_utf_8(t.join(l_tags) + n))
        
        f.write_file(args[0].split('.')[0] + '.tcsv', ''.join(output))
        
        print d_all_xml_element_attributes
    else:
        
        print n, 'Provide one .xml file and the item tag', n
    
