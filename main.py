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




month_dict = {"January":"1",
              "February":"2",
              "March":"3",
              "April":"4",
              "May":"5",
              "June":"6",
              "July":"7",
              "August":"8",
              "September":"9",
              "October":"10",
              "November":"11",
              "December":"12"}

def get_html_text(year):
    url = "https://lottomatic.org/uk-49s-teatime-lotto/results/"+str(year)+"/?latest=all"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    return BeautifulSoup(html, "html.parser").get_text()
         

def get_raw_data(soup_text):
    raw_data_it = 0

    day_str = []
    data_str_it = 0

    month_str = []

    result = []
    soup_text_it = soup_text.find("49s Teatime results drawn ")+ len("49s Teatime results drawn ")
    
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
        for i in range(0, len(raw_data), 2):
            if i == 0:
                result[data_str_it].append(int(raw_data[i+1]))
            else:    
                result[data_str_it].append(int(raw_data[i:i+2]))
                
        
        data_str_it += 1
        soup_text_it += 2
        soup_text_it += len("49s Teatime results drawn ")
    
    #print (day_str)
    #print (month_str)
    #print (result)
    return day_str, month_str, result


def get_formatted_dates(month_str):
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

    
    

year = 1998
soup_text = get_html_text(year)    
day_str, month_str, result = get_raw_data(soup_text)
formated_dates = get_formatted_dates(month_str)

print (formated_dates)

with open('C:\\Users\\Lenovo-G50\\Desktop\\yep.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter = '\t')
    writer.writerow(["Date", "result"])
    for i in range(len(formatted_dates)):
        writer.writerow(formatted_dates[i], results)
