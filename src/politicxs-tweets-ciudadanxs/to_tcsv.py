#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, glob

if __name__ == '__main__':
    
    def read_file(f_name):
        f_file = open(f_name, 'r')
        f_file_data = f_file.read()
        f_file.close()
        return f_file_data
    
    def getFiles(d): 
        l = []
        if os.path.isdir(d):
            os.chdir(d)
            l = glob.glob('*.txt')
        return l
    
    c_dir = os.getcwd() + '/'
    
    l_files = getFiles('tweets')
    
    t = '\t'
    
    line = []
    
    line.append('user')
    line.append('url')
    line.append('date')
    line.append('tweet')
    
    f_tcsv = open(c_dir + 'tdata.csv', 'w')
    
    f_tcsv.write(t.join(line) + '\n')
    
    line, items = [], []
    
    for txt in l_files:
        
        f_file = read_file(txt).split('\n')
        
        print txt
        
        if len(f_file) > 1:
            
            user = f_file[0]
            url = f_file[2]
            
            f_file = f_file[5:]
            
            for i in range(len(f_file)):
                
                if f_file[i] != '':
                    
                    items.append(f_file[i])
                    
                
            date, text = '', ''
            
            for i in range(len(items)):
                
                iitem = items[i]
                
                if len(iitem) == 19 and '/' in iitem and ':' in iitem:
                    
                    date = iitem
                    
                    next_items = items[i+1:]
                    
                    for j in range(len(next_items)):
                        
                        jitem = next_items[j]
                        
                        if len(jitem) != 19:
                            
                            if text != '':
                                text += ' ' + jitem
                            else:
                                text += jitem
                            
                        else:
                            
                            if text != '':
                                
                                line.append(user)
                                line.append(url)
                                line.append(date)
                                line.append(text)
                                
                                f_tcsv.write(t.join(line) + '\n')
                            
                            line = []
                            
                            text = ''
                            
                            break
                        
                    
                
            items = []
        
    
    f_tcsv.close()
