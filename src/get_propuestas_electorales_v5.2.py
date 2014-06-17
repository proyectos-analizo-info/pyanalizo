#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('./shared')
import functions as f
import propuestas_electorales as pe

import operator

if __name__ == '__main__':
    
    d_output = pe.format_results_v2_json('results_v2.json')
    
    crlf = '\r\n'
    output = []
    
    s = ['========================', '----------']
    
    for item in sorted(d_output.iteritems(), key = operator.itemgetter(0)):
        
        d_item = item[1]
        
        f.append(output, s[0] + crlf + 'Propuestas tarea - ' + item[0] + (' (' + d_item['task_id'] + ')') + crlf + s[0])
        
        f.append(output, d_item['breadcrumbs'])
        
        f.append(output, d_item['pages'] + crlf + '------------------')
        
        answers = d_item['answers']
        
        for answer in answers:
            
            answ = answer
            
            if 'desconocido' in answer:
                answer = answer.split('_')
                answer = answer[0] + ' (' + answer[1] + ')'
            else:
                answer = '(' + str(answer) + ')'
            
            f.append(output, 'Propuestas analista ' + answer + crlf + '---------------------------------------')
            
            f.append(output, 'Hora de inicio: ' + f.formatTime(answers[answ]['answer_end_date']) + crlf + 'Hora de fin:    ' + f.formatTime(answers[answ]['answer_start_date']))
            
            for item in answers[answ]['answer']['propuestas'].split('\n'):
                
                if item.replace(' ', '') != '':
                    
                    f.append(output, item + crlf + s[1])
                
            
            comments = answers[answ]['answer']['comentarios']
            
            if comments.replace(' ', '') != '':
                
                f.append(output, 'Comentarios' + crlf + s[1] + crlf * 2 + comments)
        
    
    f.write_file('propuestas_v5.2.txt', str(crlf * 2).join(output))
