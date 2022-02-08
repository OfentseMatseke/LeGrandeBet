# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 00:58:26 2022

@author: Lenovo-G50
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date
import string
import csv
from consts import *

def get_html_text(year, draw_name):
    url = "https://lottomatic.org/"+draw_name+"/results/"+str(year)+"/?latest=all"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    return BeautifulSoup(html, "html.parser").get_text()
         

def get_raw_data(soup_text, html_delimiter, year):
    raw_data_it = 0

    day_str = []
    data_str_it = 0

    month_str = []

    result = []
    soup_text_it = soup_text.find(html_delimiter) + len(html_delimiter)
    
    done = 0
    while(not(done)):
        
        raw_data = ""
        while(not(soup_text[soup_text_it] == "\n")):
            raw_data+=soup_text[soup_text_it]
            soup_text_it+=1
        
        day_str.append("")
        while(not(raw_data[raw_data_it] == ",")):
            day_str[data_str_it] += raw_data[raw_data_it]
            raw_data_it += 1
            
            if raw_data[raw_data_it] == "\t":
                done = 1
                break
        if done == 1:
            break
        #print (day_str)
        
        raw_data_it += 2
        month_str.append("")
        while(not(raw_data[raw_data_it] == ",")):
            month_str[data_str_it] += raw_data[raw_data_it]
            raw_data_it += 1
        
        raw_data = ""
        raw_data_it = 0
        
        soup_text_it += 1
        while(not(soup_text[soup_text_it] == "\n")):
            raw_data+=soup_text[soup_text_it]
            soup_text_it+=1
        

        result.append([])
        #print (raw_data)
        remove_plus = ""
        for i in range(0, len(raw_data)):
            if not(raw_data[i] == '+'):
                remove_plus += raw_data[i]
        raw_data = remove_plus
        remove_plus = 0        
        for i in range(0, len(raw_data), 2):
            #print ("reading %r"%(raw_data[i:i+2]))
            if raw_data[i] == 0 :
                result[data_str_it].append(int(raw_data[i+1]))
              #  print ("appending %r"%raw_data[i+1])
            else:    
                result[data_str_it].append(int(raw_data[i:i+2]))
             #   print ("appending %r"%raw_data[i:i+2])
            #c = input()    
                
        
        data_str_it += 1
        soup_text_it += 2
        soup_text_it += len(html_delimiter)
    
    #print (day_str)
    #print (month_str)
    #print (result)
    return day_str, month_str, result


def get_formatted_dates(month_str, year):
    formated_date = []
    #print (len(month_str[0]))
    for i in range(0, len(month_str)):
        temp = ""
        num = ""
        j = 0
        while(not(month_str[i][j] == " ")):
            temp += month_str[i][j]
            j += 1
            #print (temp)
        
        j+=1
        
        while(not(month_str[i][j] == "s") and not(month_str[i][j] == "n") and not(month_str[i][j] == "r") and not(month_str[i][j] == "t")):
            #temp += month_str[i][j]
            
            num+=month_str[i][j]
            j += 1
            #print (num)
        formated_date.append(str(year)+"/"+month_dict[temp]+"/"+num)            
    return formated_date  
