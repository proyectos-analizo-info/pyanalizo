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
sys.path.append('./shared')
import functions as f

if __name__ == '__main__':
    
    tasks, answers = f.parse_json_file('tasks.json'), f.parse_json_file('answers.json')
    
    d_results = {}
    
    for task in tasks:
        
        d_task = dict(task)
        
        idx = d_task['id']
        
        d_results.setdefault(idx, {})
        
        d_results[idx].setdefault('info', {})
        
        d_results[idx]['info']['details'] = d_task['info']
        d_results[idx]['info']['n_answers'] = d_task['n_answers']
        d_results[idx]['info']['created'] = d_task['created']
    
    d_null_users = {}
    
    id_unknown = 1
    
    for answer in answers:
        
        d_answer = dict(answer)
        
        idx = d_answer['task_id']
        idu = d_answer['user_id']
        
        d_results[idx].setdefault('answers', {})
        
        ok = True if idu == None else False
        
        if ok:
            idu = 'desconocido_' + str(id_unknown)
            d_null_users[idu] = idu
            id_unknown += 1
        
        d_results[idx]['answers'].setdefault(idu, {})
        
        d_user = {}
        
        d_user['answer'] = d_answer['info']
        d_user['answer_start_date'] = d_answer['created']
        d_user['answer_end_date'] = d_answer['finish_time']
        
        d_results[idx]['answers'][idu] = d_user
    
    f.write_json_file('results.json', d_results)
