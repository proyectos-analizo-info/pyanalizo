#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('./shared')
import functions as f

import operator

if __name__ == '__main__':
    
    results = f.parse_json_file('results.json')
    
    d_output = {}
    
    for result in results:
        
        d_result = dict(result)
        
        for task_id in d_result:
            
            task = d_result[task_id]
            
            if 'answers' in task: # Allow partial results
                
                task_info = task['info']
                
                idx = task_info['file']
                
                d_output.setdefault(idx, {})
                
                if task_info['pdf_page_end'] != '':
                    d_output[idx]['pages'] = u'Páginas: ' + task_info['pdf_page_start'] + ' a ' + task_info['pdf_page_end']
                else:
                    d_output[idx]['pages'] = u'Página: ' + task_info['pdf_page_start']
                
                breadcrumbs = []
                
                for i in range(1, 11):
                    
                    breadcrumb = task_info['pdf_title_' + str(i)]
                    
                    if breadcrumb != '':
                        
                        breadcrumbs.append(breadcrumb)
                        
                    
                d_output[idx]['breadcrumbs'] = ' >> '.join(breadcrumbs)
                
                d_output[idx]['answers'] = task['answers']
            
        
    
    output = []
    
    crlf = '\r\n'
    
    for item in sorted(d_output.iteritems(), key = operator.itemgetter(0)):
        
        output.append(f.encode_utf_8(item[0]))
        
        d_item = item[1]
        
        output.append(f.encode_utf_8(d_item['breadcrumbs']))
        
        output.append(f.encode_utf_8(d_item['pages']))
        
        output.append(f.encode_utf_8(d_item['answers']))
    
    f.write_file('propuestas.txt', str(crlf * 2).join(output))
