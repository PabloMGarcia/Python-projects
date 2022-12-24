
'''
------------- HOW TO STRUCTURE A PYTHON SCRIPT -----------
# Here comes your imports 
 
# Here comes your (few) global variables 
 
# Here comes your class definitions 
 
# Here comes your function definitions 

# Here comes your main() 


 '''

# Here comes your imports 
from tkinter import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox
from datetime import datetime


#Defining functions for the different elements in GUI
def RetreiveValues_CSV(df): 
  # df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d.%m.%Y %H:%M:%S')
   fig, axes = plt.subplots(nrows=2, ncols=1)
   df.plot(ax=axes[0], x='Timestamp', y='Value', kind='area', title='Full report' , color='y', xlabel='Timestamp', ylabel='Value' , legend=True)
  
   newdf = df.groupby([df["Timestamp"].dt.weekday])['Value'].mean().reset_index()
   newdf.plot(ax=axes[1], x='Timestamp', y='Value', kind='bar', title='Report by week day', color='r' , xlabel='ime', legend=False )
  # plt.show()

   fig2, axes2 = plt.subplots()
   filterdf_day1 = df.loc[df['Timestamp'].dt.weekday == 1].reset_index()
   filterdf_day1.plot(ax=axes2, x='Timestamp', y='Value')
   filterdf_day3 = df.loc[df['Timestamp'].dt.weekday == 3].reset_index()
   filterdf_day3.plot(ax=axes2, x='Timestamp', y='Value')
   filterdf_day5 = df.loc[df['Timestamp'].dt.weekday == 5].reset_index()
   filterdf_day5.plot(ax=axes2, x='Timestamp', y='Value')
   plt.show()           #with just 1 show() command I can show the fig and the fig2

# Here comes your main() 
def main():
    #Load the data
    Data_df = pd.read_csv("DataTest.txt" , delimiter= ',' , header=None, names =['Value','Timestamp'])
    #Convert string data to datetime data
    Data_df['Timestamp'] = pd.to_datetime(Data_df['Timestamp'], format='%d.%m.%Y %H:%M:%S')

    #Add 1 value to the df
    new_timestamp = datetime.strptime(str("01.04.2022 00:00:00"), '%d.%m.%Y %H:%M:%S')
    new_value = 100
  #  temporal_df = pd.DataFrame({'Timestamp': [new_timestamp] , 'Value': [new_value] })
    Data_df = Data_df.append( {'Timestamp': new_timestamp , 'Value': new_value } , ignore_index = True)
    print(Data_df.tail())

    #Create and show plot
    Data_df.plot(x='Timestamp' , y='Value' , color = 'y' , label= 'Sinusoid Tag' , ylabel = 'Value', title = 'This is my graph' , kind= 'area')
    plt.show()

    #Call to an already defined function
    RetreiveValues_CSV(Data_df)


main()
#print('print after main function')