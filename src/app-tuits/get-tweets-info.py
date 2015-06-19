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

import operator, re

def main():
    
    results = f.parse_json_file('results.json')
    
    output = []
    crlf = '\r\n'
    
    sep = [
    '=====================================================================',
    '=================',
    '------------------------------',
    '----------']
    
    a_def = [
    'El tweet',
    u'se refiere directamente a la ciudadanía, los ciudadanos y/o ciudadanas.',
    u'El diputado o diputada se refiere a la ciudadanía en ',
    ' persona.']
    
    f.append(output, sep[0])
    f.append(output, u'¿Están alejados los diputados y diputadas españoles de la ciudadanía?')
    f.append(output, sep[0] + crlf)
    
    for result in results:
        
        d_result = dict(result)
        
        for task_id in d_result:
            
            task = d_result[task_id]
            
            if 'answers' in task: # Allow partial results
                
                task_details = task['info']['details']
                
                f.append(output, 'Tarea - ' + str(task_id) + crlf + sep[1] + crlf)
                
                tweet = task_details['tweet']
                
                for match in re.finditer('http://t.co/', tweet):
                    
                    url_value = tweet[match.start():match.end() + 10]
                    
                    tweet = tweet.replace("<a title='" + url_value + "' href ='" + url_value + "' target='_blank'>" + url_value + "</a>", url_value)
                
                f.append(output, tweet + crlf)
                
                f.append(output, task_details['date'] + crlf)
                
                f.append(output, task_details['user'] + ' - ' + task_details['url'] + crlf)
                
                task_answers = task['answers']
                
                for answer in task_answers:
                    
                    analista = 'Analista '
                    
                    if 'desconocido' in answer:
                        
                        answ = answer.split('_')
                        analista += answ[0] + ' (' + answ[1] + ')'
                        
                    else:
                        
                        analista += '(' + str(answer) + ')'
                    
                    f.append(output, analista + crlf + sep[2] + crlf)
                    
                    a_answer = task_answers[answer]
                    
                    f.append(output, 'Hora de inicio: ' + f.formatTime(a_answer['answer_end_date']) + crlf + 'Hora de fin:    ' + f.formatTime(a_answer['answer_start_date']) + crlf)
                    
                    a_value = a_answer['answer']
                    
                    if a_value == 'NotKnown':
                        
                        f.append(output, a_def[0] + u' no sé si ' + a_def[1] + crlf + sep[3] + crlf)
                    
                    elif a_value == 'No':
                        
                        f.append(output, a_def[0] + ' no ' + a_def[1] + crlf + sep[3] + crlf)
                    
                    else:
                        
                        f.append(output, a_def[0] + ' ' +  a_def[1] + crlf + sep[3] + crlf)
                        
                        f.append(output, a_def[2] + a_value.lower() + a_def[3] + crlf + sep[3] + crlf)
                        
                    
                
            
        
    
    f.write_file('tweets.txt', crlf.join(output))

if __name__ == '__main__':
    main()
