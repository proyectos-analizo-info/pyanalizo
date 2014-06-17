#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':
    
    def read_file(f_name):
        f_file = open(f_name, 'r')
        f_file_data = f_file.read()
        f_file.close()
        return f_file_data
    
    lines = read_file('tdata.csv').split('\n')
    
    d = {}
    
    n = '\n'
    t = '\t'
    
    f_tcsv = open('mtdata.csv', 'w')
    
    for line in lines:
        
        if line !="":
            
            line = line.split('\t') # user url date tweet
            
            print line[0]
            
            text = line[3]
            
            for match in re.finditer('http://t.co/', text):
                
                start = match.start()
                end = match.end() + 10
                
                current_value = text[start:end]
                
                new_value = "<a title='" + current_value + "' href ='" + current_value + "' target='_blank'>" + current_value + "</a>"
                
                d[current_value] = new_value
                
                
            for k in d.keys():
                
                text = text.replace(k, d[k])
            
            f_tcsv.write(line[0] + t + line[1] + t + line[2] + t + text + n)
            
        
    f_tcsv.close()
