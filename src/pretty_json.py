#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('./shared')
import functions as f

if __name__ == "__main__":
    args = sys.argv[1:] # 0 - script name
    if len(args) >= 1:
        for item in args:
            f.write_json_file(item.split('.')[0] + '_pretty.json', f.parse_json_file(item), {'indent': 4, 'sort_keys': True})
        
    