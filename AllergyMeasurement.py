import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime



#--------------------- FUNCTION TO LOAD HISTORICAL DATA ---------------------------
def load_data (path_file , headers, rows_to_delete, year, number_of_days):
    #Load historical csv file
    Data_df = pd.read_csv(path_file , delimiter= ';' , header=1 , encoding='latin1', usecols=headers)

    #Deleting unnecessary rows
    Data_df = Data_df.drop(Data_df.index[rows_to_delete] )
    Data_df = Data_df.reset_index(drop=True)

    # Creating the date value for each
    string_start_day = "01-01-" + str(year)
    start_day = datetime.strptime(string_start_day, "%d-%m-%Y")
    date_generated = pd.date_range(start_day, periods=number_of_days)
    Data_df['Date'] = date_generated
    #print(len(Data_df.index))
    #print(Data_df.tail(15))
    return Data_df


#--------------------- START MAIN -----------------------------------------------

def main():
    #Defining the headers for the Df
    Headers_df = pd.read_csv("C:\\Users\\user\\Desktop\\Python_project\\Datasets\\PolenBilbao2020.csv" , delimiter= ';' , header=1 , nrows=1 , encoding='latin1')
    Headers = list(Headers_df.columns)
    del Headers[1]
    del Headers[0]
    del Headers[-1]
    #print(Headers)

    #Create the final df that will be used
    MainData_df = pd.DataFrame(columns= Headers)
    MainData_df['Date'] = ''

    #Appending historical data. Call method:  load_data(csv_path, headers, range_rows_to_delete, year, number_of_days)
    MainData_df = MainData_df.append(load_data('C:\\Users\\user\\Desktop\\Python_project\\Datasets\\PolenBilbao2020.csv', Headers, list(range(-4, 2)) , 2020, 366 ) , ignore_index=True)
    MainData_df = MainData_df.append(load_data('C:\\Users\\user\\Desktop\\Python_project\\Datasets\\PolenBilbao2021.csv', Headers, list(range(-6, 4)) , 2021, 365 ) , ignore_index=True)
    MainData_df = MainData_df.append(load_data('C:\\Users\\user\\Desktop\\Python_project\\Datasets\\PolenBilbao2022.csv', Headers, list(range(-4, 0)) , 2022, 365 ) , ignore_index=True)

    #Ask user to enter a kind of allergy
    Kind_of_allergy = input("Enter a name: ")

    MainData_df.plot(x='Date' , y=Kind_of_allergy)
    plt.show()

    Analysis_data = pd.DataFrame()
    Analysis_data['mean'] = MainData_df.groupby(MainData_df['Date'].dt.week)[Kind_of_allergy].mean()

    Analysis_data['percentaje'] = (Analysis_data['mean'] / Analysis_data['mean'].max()) * 100
    print(Analysis_data['percentaje'])
    print(Analysis_data.head())
    Analysis_data.plot(y='percentaje')
    plt.show()



       #Ask user to enter a kind of allergy
    number_of_month = input("Enter a month number: ")

    #Analysis_data = pd.DataFrame()
    Analysis_data = MainData_df.groupby(MainData_df['Date'].dt.month).mean()
    del Analysis_data['TOTAL']
    print(Analysis_data)
    print(len(Analysis_data.index))
    Analysis_data = Analysis_data.iloc[int(number_of_month)]
    

    Analysis_data.plot(kind = 'bar')
    plt.show()






main()
