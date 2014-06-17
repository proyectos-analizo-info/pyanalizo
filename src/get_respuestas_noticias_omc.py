#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('./shared')
import functions as f
import omc_xml_parser as xml

import operator

if __name__ == '__main__':
    
    results = f.parse_json_file('results_v2.json')
    
    output = []
    crlf = '\r\n'
    
    s = ['========================', '----------']
    
    questions = {
    'p0': u'1) ¿Qué personas, grupos y/o asociaciones identificas en la noticia?',
    'p1': u'2) ¿Quién o qué organismo ha facilitado la información al periodista para redactar la noticia?',
    'p2': u'3) ¿Aparece una voz del sur (testimonio directo) que cuente su opinión en la noticia?',
    'p3': u'4) ¿La noticia identifica y/o explica las causas de la problemática planteada?'
    }
    
    for result in results:
        
        d_result = dict(result)
        
        for task_id in d_result:
            
            task = d_result[task_id]
            
            if 'answers' in task: # Allow partial results
                
                f.append(output, s[0] + crlf + 'Respuestas tarea (' + str(task_id) + ')' + crlf + s[0] + crlf)
                
                id_noticia = task['info']['details']['id_noticia']
                
                noticia_json = dict(f.parse_json_file('json/' + id_noticia + '.json'))
                
                for tag in xml.tags:
                    
                    if tag in noticia_json:
                        
                        tag_value = noticia_json[tag]
                        
                        if tag_value != 'NUL':
                            
                            f.append(output, tag + ': ' + tag_value + crlf)
                        
                    
                answers = task['answers']
                
                for answer in answers:
                    
                    answ = answer
                    
                    if 'desconocido' in answer:
                        answer = answer.split('_')
                        answer = answer[0] + ' (' + answer[1] + ')'
                    else:
                        answer = '(' + str(answer) + ')'
                    
                    f.append(output, 'Propuestas analista ' + answer + crlf + '---------------------------------------')
                    
                    f.append(output, 'Hora de inicio: ' + f.formatTime(answers[answ]['answer_end_date']) + crlf + 'Hora de fin:    ' + f.formatTime(answers[answ]['answer_start_date']) + crlf)
                    
                    f.append(output, u'Categorías' + crlf + s[1] + crlf * 2 + answers[answ]['answer']['tags'] + crlf)
                    
                    for q in ['p0', 'p1', 'p2', 'p3']:
                        
                        f.append(output, questions[q] + crlf)
                        
                        for item in answers[answ]['answer'][q].split('\n'):
                            
                            if item.replace(' ', '') != '':
                                
                                f.append(output, item + crlf + s[1] + crlf)
                                
                            
                        
                    
                    comments = answers[answ]['answer']['comentarios']
                    
                    if comments.replace(' ', '') != '':
                        
                        f.append(output, 'Comentarios' + crlf + s[1] + crlf * 2 + comments + crlf)
                
            
        
    f.write_file('noticias.txt', crlf.join(output))
