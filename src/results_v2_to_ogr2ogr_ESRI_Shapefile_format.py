#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('./shared')
import functions as f

if __name__ == '__main__':
    
    d_results_v2 = dict(f.parse_json_file('results_v2.json')[0])
    
    d_results, d_crs, d_geometry_types = {}, {}, {}
    
    item_id = 1
    
    n = '\n'
    
    for task_id in d_results_v2:
        
        d_results.setdefault(task_id, {})
        
        d_results[task_id].setdefault('answers', {})
        
        d_results[task_id].setdefault('info', {})
        
        d_task = d_results_v2[task_id]
        
        d_task_answers = d_task['answers']
        
        d_ogr2ogr_ESRI_Shapefile_format = {
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
                        
                        print n, '* Warning: Different crs', n
                        
                        print d_crs, n
                        
                        sys.exit()
                    
                    answer_info_geometry = answer_info['geometry']
                    
                    geometry_type = answer_info_geometry['type']
                    
                    if geometry_type not in d_geometry_types:
                        
                        d_geometry_types[geometry_type] = geometry_type
                    
                    if len(d_geometry_types) > 1:
                        
                        print n, '* Warning: Different objects', n
                        
                        print d_geometry_types, n
                        
                        sys.exit()
                    
                    d_ogr2ogr_ESRI_Shapefile_format['crs'] = d_crs[crs]
                    
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
                    
                d_ogr2ogr_ESRI_Shapefile_format['features'] = features
                
            
        
        if d_ogr2ogr_ESRI_Shapefile_format['features'] != '':
            
            d_results[task_id] = d_ogr2ogr_ESRI_Shapefile_format
            
        else:
            
            del d_results[task_id]
            
        
    f.write_json_file('results_v2_to_ogr2ogr_ESRI_Shapefile_format.json', d_results)
