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

"""
https://dev.twitter.com/docs/api/1.1
https://dev.twitter.com/docs/api/1.1/get/statuses/user_timeline
"""

from tcfg_mod import *
from twython import Twython
import os, datetime, sys

def main():
    
    os.system('clear')
    
    twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
    
    d_dirs = ['tweets', 'data']
    
    for d_dir in d_dirs:
        if not os.path.exists(d_dir):
            os.makedirs(d_dir)
    
    f_idx = open('last-diputado.txt', 'r')
    idx = int(f_idx.read())
    f_idx.close()
    
    f_diputados = open('diputados.txt', 'r')
    diputados = f_diputados.readlines()[idx:]
    f_diputados.close()
    
    n = ['\n', '\n\n']
    
    date_format = '%d/%m/%Y %H:%M:%S'
    
    date_period = (stringToDate('07/01/2014 00:00:00', date_format), stringToDate('07/02/2014 23:59:59', date_format))
    
    keys = ['created_at', 'text']
    
    for i in range(len(diputados)):
        
        user = diputados[i][1:-1]
        
        print i, '-', user
        
        try:
            
            user_tweets = twitter.get_user_timeline(screen_name = user, count = '200', exclude_replies = 'true', include_rts = 'false')
            
            f_user = open(d_dirs[1] + '/' + user + '.txt', 'w') # data
            f_user.write(str(user_tweets))
            f_user.close()
            
        except Exception as e:
            
            e = str(e)
            
            print n[0], 'Exception:', e, n[0]
            
            if '401' in e: # (Unauthorized), An error occurred processing your request.
                
                continue
            
            if '429' in e: # Twitter API returned a 429 (Too Many Requests), Rate limit exceeded
                
                f_idx = open('last-diputado.txt', 'w')
                f_idx.write(str(i + idx))
                f_idx.close()
                
                sys.exit()
            
        
        f_user = open(d_dirs[0] + '/' + user + '.txt', 'w') # tweets
        
        header, data = '', ''
        
        header += user + n[1]
        
        header += 'https://twitter.com/' + user + n[1]
        
        header += 'from ' + formatDate(date_period[0], date_format) + ' to ' + formatDate(date_period[1], date_format) + n[1]
        
        for tweet in user_tweets:
            
            if keys[0] in tweet and keys[1] in tweet:
                
                # Sun Feb 02 12:25:44 +0000 2014
                
                # %a    Weekday name.
                # %b    Abbreviated month name.
                # %d    Day of the month as a decimal number [01,31].
                # %H    Hour (24-hour clock) as a decimal number [00,23].
                # %M    Minute as a decimal number [00,59].
                # %S    Second as a decimal number [00,61].
                # %Y    Year with century as a decimal number.
                
                date = stringToDate(getValue(tweet, keys[0]), '%a %b %d %H:%M:%S +0000 %Y')
                
                date = stringToDate(date.strftime(date_format), date_format) # dd/mm/YYYY HH:MM:SS
                
                if checkDate(date, date_period):
                    data += formatDate(date, date_format) + n[0] + getValue(tweet, keys[1]) + n[1]
                    
                
            
        if data != '':
            f_user.write(header + data)
        
        f_user.close()
        
    f_idx = open('last-diputado.txt', 'w')
    f_idx.write(str(0))
    f_idx.close()

def checkDate(date, date_period):
    return True if date.date() >= date_period[0].date() and date.date() <= date_period[1].date() else False # date >= start_date and date <= end_date

def formatDate(date, date_format):
    return date.strftime(date_format)

def stringToDate(string, date_format):
    return datetime.datetime.strptime(string, date_format)

def getValue(d, k):
    return d[k].encode('utf-8')

if __name__ == '__main__':
    main()
