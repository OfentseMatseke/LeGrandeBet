# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 07:41:26 2022

@author: Lenovo-G50
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date
import string
import csv
from consts import *
from data_scraper import *
from file_io import *

data_storage_path = ""






    
    
#lll = ["lunchtime",lunchtime,lunchtime_html_delimiter, "teatime",teatime, teatime_delimiter]



#year = 1999
#soup_text = get_html_text(year, lunchtime)    
#day_str, month_str, result = get_raw_data(soup_text, lunchtime_html_delimiter, year)
    
    #print (result[0:10])
#formatted_dates = get_formatted_dates(month_str, year)
    
#print (formatted_dates)
    
#with open('C:\\Users\\Lenovo-G50\\Desktop\\kk3.csv', 'w', newline='') as file:
#    writer = csv.writer(file, delimiter = '\t')
#    writer.writerow(["Date", "Day", "result"])
#    for i in range(len(formatted_dates)):
#        writer.writerow([formatted_dates[i], day_str[i], result[i]])




#get_local_files('C:\\Users\\Lenovo-G50\\Desktop\\test\\'\
#                , [2003, 2022], "teatime",sa_lotto_plus, sa_lotto_plus_html_delimiter)
    
obj = read_local_files('C:\\Users\\Lenovo-G50\\Desktop\\test\\'\
                 , [2004, 2006], "teatime",sa_lotto_plus, sa_lotto_plus_html_delimiter)


for i in range(len(obj)):
    print(obj[i][1].result)

