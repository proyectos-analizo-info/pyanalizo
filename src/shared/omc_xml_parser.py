#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functions as f
import operator, re
from xml.dom.minidom import parseString

tags = ['ID', 'Titulo', 'Medio', 'Autor', 'Fecha', 'URL', 'Imagen'] # u'Subtítulo'

def get_xml_elements(f_file_name, element_name):
    return parseString(f.read_file(f_file_name)).getElementsByTagName(element_name)

def parse_xml(f_file_name, element_name):
    
    l_items = []
    
    xml_elements = get_xml_elements(f_file_name, element_name)
    
    d_all_xml_element_attributes = {}
    
    for xml_element in xml_elements:
        
        if xml_element.hasChildNodes():
            
            d_xml_element_attributes = {}
            
            for xml_element_child_node in xml_element.childNodes:
                
                xml_element_attribute = xml_element_child_node.localName
                
                if xml_element_attribute != None:
                    
                    d_xml_element_attributes[xml_element_attribute] = ''
                    
                    d_all_xml_element_attributes[xml_element_attribute] = ''
                    
                
            d_noticia = {}
            
            for xml_element_attribute in d_xml_element_attributes:
                
                for node in (xml_element.getElementsByTagName(xml_element_attribute)[0]).childNodes:
                    
                    if node.nodeType == node.TEXT_NODE:
                        
                        d_noticia[xml_element_attribute] = re.sub(ur'\u00a0+', '', f.strip_html_tags(f.formatTime(node.nodeValue) if xml_element_attribute == 'Fecha' else node.nodeValue), re.UNICODE)
                    
                
            l_items.append(d_noticia)
        
    return d_all_xml_element_attributes, l_items
