#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('./shared')
import functions as f

if __name__ == '__main__':
    
    d_results_v2_ogr2ogr_ESRI_Shapefile_format = dict(f.parse_json_file('results_v2_to_ogr2ogr_ESRI_Shapefile_format.json')[0])
    
    d_ogr2ogr_ESRI_Shapefile_format = {
    'type': 'FeatureCollection',
    'crs': '',
    'features': ''
    }
    
    d_crs, d_geometry_types = {}, {}
    
    l_features = []
    
    for task_id in d_results_v2_ogr2ogr_ESRI_Shapefile_format:
        
        task_info = d_results_v2_ogr2ogr_ESRI_Shapefile_format[task_id]
        
        crs = task_info['crs']['properties']['name']
        
        if crs not in d_crs:
            
            d_crs[crs] = task_info['crs']
            
        if len(d_crs) > 1:
            
            print n, '* Warning: Different crs', n
            
            print d_crs, n
            
            sys.exit()
            
        
        for d_feature in task_info['features']:
            
            geometry_type = d_feature['geometry']['type']
            
            if geometry_type not in d_geometry_types:
                
                d_geometry_types[geometry_type] = geometry_type
            
            if len(d_geometry_types) > 1:
                
                print n, '* Warning: Different objects', n
                
                print d_geometry_types, n
                
                sys.exit()
            
            d_object = {}
            
            d_object['geometry'] = d_feature['geometry']
            d_object['properties'] = d_feature['properties']
            d_object['type'] = d_feature['type']
            
            l_features.append(d_object)
        
    d_ogr2ogr_ESRI_Shapefile_format['crs'] = d_crs[crs]
    
    d_ogr2ogr_ESRI_Shapefile_format['features'] = l_features
    
    f.write_json_file('ogr2ogr_ESRI_Shapefile_format.json', d_ogr2ogr_ESRI_Shapefile_format, {'clasp': False})
