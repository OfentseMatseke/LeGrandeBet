# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 01:08:46 2022

@author: Lenovo-G50
"""

from data_scraper import *
from consts import *
import csv
import re



class result:
    result = []
    date = 0
    month = 0
    weekday = ""
    weekday_numb = 0
    year = 0
    


def get_local_files(directory, year_range, bet_type,bet_type_url, bet_type_delimiter):
    for year in range(year_range[0], year_range[1]):
        
        print ("Retrieving "+bet_type_dict[bet_type_url]+" Results from the year %r"%year)
        soup_text = get_html_text(year, bet_type_url)    
        day_str, month_str, result = get_raw_data(soup_text, bet_type_delimiter, year)
        
        #print (result[0:10])
        formatted_dates = get_formatted_dates(month_str, year)
        
        #print (formatted_dates)
        
        with open(directory+bet_type_file_dict[bet_type_url]+"_"+str(year)+".csv", 'w', newline='') as file:
            writer = csv.writer(file, delimiter = '\t')
            writer.writerow(["Date", "Day", "result"])
            for i in range(len(formatted_dates)):
                writer.writerow([formatted_dates[i], day_str[i], result[i]])
 
    
def read_local_files(directory, year_range, bet_type,bet_type_url, bet_type_delimiter):     
         
    ret_obj = []
    for year in range(year_range[0], year_range[1]):
        dates = []
        results = []
        day = []
        with open (directory+bet_type_file_dict[bet_type_url]+"_"+str(year)+".csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = '\t')
            i = 0
            for row in csv_reader:
                if not(i == 0):
                    #print("%r %r"%(row[0], row[1][0:4]))
                    dates.append(row[0])
                    day.append(row[1])
                    results.append(row[2])
                i+=1                  
        total_results = []
        
        for j in range(0, len(results)):
            current_result = []
            #current_result.result.append([])
            for i in range(0, len(results[j])):
                #current_result = result()
                if results[j][i] == "," or results[j][i] == "]":
                    k = i-1
                    temp = ""
                    
                    while not(results[j][k] == '[') and not(results[j][k] == ",") and not(results[j][k] == " "):
                        temp += results[j][k]
                        k-=1
                      
                    if len(temp) >= 2:
                        temp2 = temp[0]
                        temp3 = temp[1]
                        temp = ""
                        temp += temp3
                        temp += temp2
                    #print (temp)
                    current_result.append(int(temp))
                    #current_result.result.append(int(temp))
            #print (current_result)
            new_node = result()
            new_node.result = current_result;        
            new_node.weekday = day[j]
            new_node.weekday_numb = day_dict[day[j]]
            new_node.year = year
            
            
            temp = re.split("/",dates[j])
            #print (temp)
            new_node.month = int (temp[1])
            new_node.date = int(temp[2])
                
                
                    
                
            total_results.append(new_node)            
        ret_obj.append(total_results)
    return ret_obj