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

def main():
    
    n = '\n'
    msg = [n + '* Must provide .shp and .dbf files for building .shx' + n]
    
    args = sys.argv[1:] # 0 - script name
    
    if len(args) != 2:
        
        print msg[0]
        
    else:
        
        try:
            
            import shapefile
            
            d_files = {}
            
            for f_file in args:
                
                f_ext = f_file.split('.')[1]
                
                if f_ext not in ['shp', 'dbf']:
                    
                    print msg[0]
                    
                    sys.exit()
                    
                else:
                    
                    d_files[f_ext] = f_file
                    
                
            if len(d_files.keys()) == 2:
                
                print n, '* Building a new shx file...'
                
                print '* Opening the shp file...'
                
                f_shp = open(d_files['shp'], 'rb')
                
                print '* Opening the dbf file...'
                
                f_dbf = open(d_files['dbf'], 'rb')
                
                print '* Reading both files...'
                
                shpr = shapefile.Reader(shp=f_shp, shx=None, dbf=f_dbf)
                
                shpw = shapefile.Writer(shpr.shapeType)
                
                print '* Cloning the current ERSI Shapefile object to a new one...'
                
                shpw._shapes = shpr.shapes()
                shpw.records = shpr.records()
                shpw.fields = list(shpr.fields)
                
                print '* Saving the new ERSI Shapefile object (.shp + .dbf + .shx)'
                
                import os
                
                f_dir = 'new_ERSI_Shapefile/'
                
                f_name = 'ERSI_Shapefile'
                
                os.system('mkdir -p ' + f_dir)
                
                shpw.save(f_dir + f_name)
                
                print
                
                os.system('zip ' + f_dir + f_name + ' ' + f_dir + '*.*')
                
                print n, "* ERSI Shapefile object succesfully created at \'" + f_dir + "\' folder.", n
                
                os.system('ls -l ' + f_dir)
                
                print
                
            else:
                
                print msg[0]
            
        except ImportError:
            
            print n, '* Missing shapefile.py, download first.', n
        
        except IOError:
            
            print n, '* Unable to locate the files.', n
        
    
if __name__ == '__main__':
    main()
