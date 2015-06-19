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

import json, re

def read_file(f_name):
    try:
        f_file = open(f_name)
        f_file_data = f_file.read()
        f_file.close()
        return f_file_data
    except Exception as e:
        print '* Exception:', str(e)
    

def write_file(f_name, info):
    try:
        f_file = open(f_name, 'w')
        f_file.write(info)
        f_file.close()
    except Exception as e:
        print '* Exception:', str(e)

def parse_json_file(f_name):
    try:
        return json.loads(read_file(f_name))
    except Exception as e:
        print '* Exception:', str(e)
    

def write_json_file(f_name, d_dict, d_options = {}):
    try:
        f_file = open(f_name, 'w')
        if 'indent' in d_options and 'sort_keys' in d_options:
            f_file.write(json.dumps(d_dict, indent = d_options['indent'], sort_keys = d_options['sort_keys']))
        else:
            if 'clasp' in d_options and d_options['clasp'] == False:
                f_file.write(json.dumps(d_dict))
            else:
                f_file.write('[' + json.dumps(d_dict) + ']')
                
            
        f_file.close()
    except Exception as e:
        print '* Exception:', str(e)
    

def encode_utf_8(v):
    try:
        return v.encode('utf-8')
    except Exception as e:
        print '* Exception:', str(e)
    

def formatTime(v): # 2014-03-26T21:53:39.933027
    try:
        time = v.split('T')
        return '-'.join(time[0].split('-')[::-1]) + ' ' + time[1]
    except Exception as e:
        print '* Exception:', str(e)
    

def append(output, item):
    try:
        return output.append(encode_utf_8(item))
    except Exception as e:
        print '* Exception:', str(e)
    

def strip_html_tags(v):
    try:
        return re.sub(r'<[^>]+>', '', v)
    except Exception as e:
        print '* Exception:', str(e)
    
