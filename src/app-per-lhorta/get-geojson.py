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

def main():
    
    d_intput = dict(f.parse_json_file('results-geojson.json')[0])
    
    d_geojson = {
        'type': 'FeatureCollection',
        'crs': '',
        'features': ''
    }
    
    l_features = []
    
    for task_id in d_intput:
        
        task_info = d_intput[task_id]
        
        for d_feature in task_info['features']:
            
            d_object = {}
            
            d_object['geometry'] = d_feature['geometry']
            d_object['properties'] = d_feature['properties']
            d_object['type'] = d_feature['type']
            
            l_features.append(d_object)
        
    d_geojson['crs'] = task_info['crs']
    
    d_geojson['features'] = l_features
    
    f.write_json_file('geojson.json', d_geojson, {'clasp': False})

if __name__ == '__main__':
    main()
