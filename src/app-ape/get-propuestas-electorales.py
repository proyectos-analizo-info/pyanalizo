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
import ape, operator

def main():
    
    d_output = ape.format_results('results.json')
    
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
        
    
    f.write_file('propuestas.txt', str(crlf * 2).join(output))

if __name__ == '__main__':
    main()
