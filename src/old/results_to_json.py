#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('./shared')
import functions as f

if __name__ == '__main__':
    
    tasks, answers = f.parse_json_file('tasks.json'), f.parse_json_file('answers.json')
    
    d_results = {}
    
    for task in tasks:
        
        d_task = dict(task)
        
        idx = d_task['id']
        
        d_results.setdefault(idx, {})
        
        d_results[idx]['info'] = d_task['info']
        d_results[idx]['n_answers'] = d_task['n_answers']
        d_results[idx]['task_date'] = d_task['created']
    
    for answer in answers:
        
        d_answer = dict(answer)
        
        idx = d_answer['task_id']
        
        if 'answers' in d_results[idx]:
            d_results[idx]['answers'] += '\n' + d_answer['info']
        else:
            d_results[idx]['answers'] = d_answer['info']
        
        d_results[idx]['user_id'] = d_answer['user_id']
        d_results[idx]['answer_start_date'] = d_answer['created']
        d_results[idx]['answer_end_date'] = d_answer['finish_time']
    
    f.write_json_file('results.json', d_results)
