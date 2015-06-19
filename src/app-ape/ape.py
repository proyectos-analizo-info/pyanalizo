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

def format_results(f_file_name):
    
    results = f.parse_json_file(f_file_name)
    
    d_output = {}
    crlf = '\r\n'
    
    for result in results:
        
        d_result = dict(result)
        
        for task_id in d_result:
            
            task = d_result[task_id]
            
            if 'answers' in task: # Allow partial results
                
                task_details = task['info']['details']
                
                idx = task_details['file']
                
                d_output.setdefault(idx, {})
                
                d_output[idx]['task_id'] = str(task_id)
                
                if task_details['pdf_page_end'] != '':
                    d_output[idx]['pages'] = u'Páginas: ' + task_details['pdf_page_start'] + ' a ' + task_details['pdf_page_end']
                else:
                    d_output[idx]['pages'] = u'Página: ' + task_details['pdf_page_start']
                
                breadcrumbs = []
                
                for i in range(1, 11):
                    
                    breadcrumb = task_details['pdf_title_' + str(i)]
                    
                    if breadcrumb != '':
                        
                        breadcrumbs.append(breadcrumb)
                        
                    
                d_output[idx]['breadcrumbs'] = crlf.join(breadcrumbs)
                
                d_output[idx]['answers'] = task['answers']
            
        
    return d_output
