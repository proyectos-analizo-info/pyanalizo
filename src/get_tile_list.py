#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('./shared')
import functions as f

if __name__ == "__main__":
    
    """
    http://terramapas.icv.gva.es/odcv05_etrs89h30_2010/?
    &SERVICE=WMS
    &VERSION=1.3.0
    &REQUEST=GetMap
    &LAYERS=ortofoto_2010_valencia
    &FORMAT=image/png
    &CRS=EPSG:25830
    &BBOX=727955.71890415,4372723.5411562,728125.05214607,4372892.8743981 # minx miny maxx maxy
    &WIDTH=256
    &HEIGHT=256
    """
    
    ######################
    # DO NOT CHANGE THIS #
    ######################
    
    # DEFAULT TILE SIZE
    
    def_tile_width = 256
    def_tile_height = 256
    
    # DEFAULT LIMITS
    
    def_min_x_y = [727955.71890415, 4372723.5411562] # [min_x, min_y]
    def_max_x_y = [728125.05214607, 4372892.8743981] # [max_x, max_y]
    
    # DEFAULT DIFF
    
    def_diff_width = def_max_x_y[0] - def_min_x_y[0] # [max_x, min_x]
    def_diff_height = def_max_x_y[1] - def_min_x_y[1] # [max_y, min_y]
    
    ####################################################################
    
    ###############
    # CHANGE THIS #
    ###############
    
    # SET NEW TILE SIZE
    
    new_tile_width = 940
    new_tile_height = 356
    
    # SET NEW LIMITS
    
    new_min_x_y = [727814.88208, 4373064.54349] # [min_x, min_y]
    new_max_x_y = [729355.75638, 4374066.81196] # [max_x, max_y]
    
    # NEW DIFF
    
    """
    def_tile_width - def_diff_width
    new_tile_width - x
    """
    
    def_diff_width = (new_tile_width * def_diff_width) / def_tile_width
    
    """
    def_tile_height - def_diff_height
    new_tile_height - x
    """
    
    def_diff_height = (new_tile_height * def_diff_height) / def_tile_height
    
    ####################################################################
    
    # FIRST START POINT
    
    first_start_point = [new_min_x_y[0], new_max_x_y[1]] # [min_x, max_y] top_left
    
    # FIRST END POINT
    
    first_end_point = [new_max_x_y[0], new_max_x_y[1]] # [max_x, max_y] top_right
    
    # LAST END POINT
    
    last_end_point = [new_max_x_y[0], new_min_x_y[1]] # [max_x, min_y] bottom_right
    
    """
    [fsp]-------[fep] # first_start_point | # first_end_point
      |           |
    [nsp]       [nep] # n_start_point     | # n_end_point
      |           |
    [lsp]-------[lep] # last_start_point  | # last_end_point
    """
    
    # GET THE TILES
    
    current_row = 0
    
    tiles = []
    
    current_point = [first_start_point[0], first_start_point[1], 0, first_start_point[1]] # min_x min_y max_x max_y
    
    current_end_point = [0, 0, first_end_point[0], first_end_point[1]] # min_x min_y max_x max_y
    
    while True:
        
        current_min_y = current_point[1] - def_diff_height # max_y - def_diff_height
        
        current_max_x = current_point[0] + def_diff_width # min_x + def_diff_width
        
        current_tile = [current_point[0], current_min_y, current_max_x, current_point[3]] # min_x min_y max_x max_y
        
        tiles.append(current_tile)
        
        print current_tile
        
        if current_tile[2] > current_end_point[2]: # max_x > max_x (n_end_point)
            
            print
            
            current_row += 1
            
            new_y = first_start_point[1] - (def_diff_height * current_row)
            
            current_point[0] = first_start_point[0] # min_x
            
            current_point[1] = new_y # min_y
            
            current_point[3] = new_y # max_y
            
        else:
            
            current_point[0] = current_max_x # min_x
        
        if current_tile[2] > current_end_point[2] and current_tile[1] < last_end_point[1]: # min_y > min_y (bottom_right)
            break
            
        
    
    output = []
    
    t = '\t'
    crlf = '\r\n'
    
    # WRITE RESULT
    
    for tile in tiles:
        
        min_x = "'" + str(tile[0]) + t
        min_y = "'" + str(tile[1]) + t
        max_x = "'" + str(tile[2]) + t
        max_y = "'" + str(tile[3]) + crlf
        
        output.append(min_x + min_y + max_x + max_y)
    
    f.write_file('tiles.txt', ''.join(output))
    
