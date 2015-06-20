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
    
    d_intput = dict(f.parse_json_file('results.json')[0])
    
    d_results, d_crs, d_geometry_types = {}, {}, {}
    
    item_id = 1
    
    for task_id in d_intput:
        
        d_results.setdefault(task_id, {})
        
        d_results[task_id].setdefault('answers', {})
        
        d_results[task_id].setdefault('info', {})
        
        d_task = d_intput[task_id]
        
        d_task_answers = d_task['answers']
        
        d_geojson = {
            'type': 'FeatureCollection',
            'crs': '',
            'features': ''
        }
        
        features = []
        
        for answer_id in d_task_answers:
            
            d_results[task_id]['answers'].setdefault(answer_id, {})
            
            d_answer = d_task_answers[answer_id]
            
            if d_answer['answer'] != 'unknown': # Skip unuseful (empty) answer
                
                for answer_info in d_answer['answer']:
                    
                    crs = answer_info['crs']['properties']['name']
                    
                    if crs not in d_crs:
                        
                        d_crs[crs] = answer_info['crs']
                        
                        if len(d_crs) > 1:
                            
                            print '\n* Different crs:', d_crs, '\n'
                            
                            sys.exit()
                        
                    answer_info_geometry = answer_info['geometry']
                    
                    geometry_type = answer_info_geometry['type']
                    
                    # Shapefiles can only support one geometry type (Polygon)
                    
                    if geometry_type not in d_geometry_types:
                        
                        d_geometry_types[geometry_type] = geometry_type
                        
                    if geometry_type.lower() == 'point':
                        
                        continue
                        
                    d_geojson['crs'] = d_crs[crs]
                    
                    d_object = {}
                    
                    d_object['type'] = answer_info['type']
                    
                    d_geometry = {}
                    
                    d_geometry['type'] = geometry_type
                    
                    coordinates = answer_info_geometry['coordinates']
                    
                    longitude, latitude = [], []
                    
                    for coordinate in coordinates[0]: 
                        
                        longitude.append(coordinate[0])
                        
                        latitude.append(coordinate[1])
                    
                    d_geometry['coordinates'] = coordinates
                    
                    d_object['geometry'] = d_geometry
                    
                    d_properties = {}
                    
                    id_id = str(answer_id) + str(task_id) + str(item_id)
                    
                    d_properties['ID'] = id_id
                    
                    item_id += 1
                    
                    d_properties['XMIN'] = min(longitude)
                    d_properties['XMAX'] = max(longitude)
                    d_properties['YMIN'] = min(latitude)
                    d_properties['YMAX'] = max(latitude)
                    
                    d_object['properties'] = d_properties
                    
                    features.append(d_object)
                    
                d_geojson['features'] = features
            
        if d_geojson['features'] != '':
            
            d_results[task_id] = d_geojson
            
        else:
            
            del d_results[task_id]
        
    f.write_json_file('results-geojson.json', d_results)

if __name__ == '__main__':
    main()
