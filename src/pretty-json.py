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

if __name__ == "__main__":
    args = sys.argv[1:] # 0 - script name
    if len(args) >= 1:
        for item in args:
            f.write_json_file(item.split('.')[0] + '-pretty.json', f.parse_json_file(item), {'indent': 4, 'sort_keys': True})
        
    
