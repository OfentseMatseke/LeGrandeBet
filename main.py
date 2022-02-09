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
from database import *

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




#get_local_files('C:\\Users\\Lenovo-G50\\Documents\\Code\\LeGrandeBet\\data\\UK49\\teatime\\'\
#                , [1997, 2023], "teatime",teatime, teatime_html_delimiter)

#get_local_files('C:\\Users\\Lenovo-G50\\Documents\\Code\\LeGrandeBet\\data\\UK49\\lunchtime\\'\
#                , [1997, 2023], "teatime",lunchtime, lunchtime_html_delimiter)    
#obj = read_local_files('C:\\Users\\Lenovo-G50\\Desktop\\test\\'\
#                 , [2005, 2006], "teatime",sa_lotto_plus, sa_lotto_plus_html_delimiter)

 

db = init_database("localhost", "root", "mpsbhcup", "mydatabase")
#create_table(db, "test_lotto", 0)

#add_column(db, "test_lotto", "Date", "DATE")
#add_column(db, "test_lotto", "Day", "VARCHAR(255)")
#add_column(db, "test_lotto", "Result", "VARCHAR(255)")


#print (len(obj))

#for i in range(len(obj)):
#    print (len(obj[i]))
    #for j in range(len(obj[i])):
        
        #print([date_to_str(obj[i][j]),\
        #       obj[i][j].weekday, \
        #       str(obj[i][j].result)[1:len(str(obj[i][j].result))-1]])
    #print(obj[i][1].weekday)
    #print(obj[i][1].date)
        
    
        #print(date_to_str(obj[i][1]))
        
        #print (str(obj[i][1].result)[1:len(str(obj[i][1].result))-1])
        #   print (obj[i][1].weekday)
       # add_row(db, "test_lotto", "Date, Day, Result", 3, [date_to_str(obj[i][j]),\
        #                                              obj[i][j].weekday, \
        #                                                  str(obj[i][j].result)[1:len(str(obj[i][j].result))-1]])     
#db = init_database("localhost", "root", "mpsbhcup")   
#add_row(db, "lotto", "Date, Day, Result", 3, []) 


retr = select_all(db, "test_lotto")
print (retr)











