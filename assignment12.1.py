# -*- coding: utf-8 -*-
"""
Created on Mon May 28 22:56:47 2018

@author: avatash.rathore
"""
import pandas as pd
import numpy as np


flight_list = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'], 
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]], 
                   'Airline': ['KLM(!)', ' (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})


print('Update NaN for Flight numbers')
flight_list['FlightNumber'] =flight_list['FlightNumber'].interpolate().astype(int)
print(flight_list)

print('Create To and From Seprate column from From_To')
flight_list['From'] = flight_list['From_To'].str.split('_').str[0]
flight_list['To'] = flight_list['From_To'].str.split('_').str[0]
print(flight_list)
print('Delete column From_To')
flight_list.drop(flight_list.columns[flight_list.columns.str.contains('From_TO',case = False)],axis = 1,inplace=True)
#flight_list.drop('From_To', axis=1, inplace=True)
#flight_list['To'] = flight_list['To'].str.title()
print(flight_list)
print('Noramlize data of  To and From')
flight_list['To'] = flight_list['To'].str.capitalize()
flight_list['From'] = flight_list['From'].str.capitalize()
print(flight_list)
print('Create seperate Delay Columns')
delays = pd.DataFrame(flight_list['RecentDelays'].values.tolist())

delays = delays.rename(columns={0: "delay_1", 1: "delay_2", 2: "delay_3"})

flight_list= pd.concat([flight_list,delays],axis=1)
flight_list.drop('RecentDelays', axis=1, inplace=True)
print(flight_list)

