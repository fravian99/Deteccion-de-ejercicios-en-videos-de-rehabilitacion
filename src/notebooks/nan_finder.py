
import pandas as pd
import numpy as np
import os
import json




def get_names(filenames):
    data_path = "../datos/"
    path_df = data_path + "DataFrames"
    path_csv = data_path + "CSV"

    dataframes = []
    csvs = []
    for exercise in filenames:
        for ex_number in filenames[exercise]:
            for file in filenames[exercise][ex_number]:
                actual_df = path_df + os.sep + file + ".df"
                actual_csv = path_csv + os.sep + file + ".csv"
                dataframes.append(actual_df)
                csvs.append(actual_csv)
    return dataframes, csvs

            

def open_csv(csv_name):
    mycsv = pd.read_csv(csv_name)
    return mycsv

def open_dataframe(df_name):
    with open(df_name, 'rb') as fp:
            df = pd.read_pickle(fp)
    return df

def verify_data(data):
    nan_rows = {}
    for i in data[data.columns[0]]:
        nan_columns = []
        for column_name in data:
            cell = data[column_name][i] 
            if (np.isnan(cell)):
                nan_columns.append(column_name)
        if(len(nan_columns) != 0):
            nan_rows[i] = nan_columns
    return nan_rows


def verify(filepaths, open_file):
    nans = {}
    for filepath in filepaths:
        
        data = open_file(filepath)
        nan_columns = verify_data(data)
        if (len(nan_columns)>1):
            print()
            print(filepath)
            for i in nan_columns:
                print('\t',i)
                print('\t\t',nan_columns[i])
            nans[filepath] = nan_columns
    return nans
        


def main():
    filepaths_df, filepaths_csv = get_names(filenames)
    nans = verify(filepaths_csv,open_csv)
    with open("nan_csvs.json","w") as file:
        json.dump(nans, file, indent=4)

    nans = verify(filepaths_df,open_dataframe)
    with open("nan_df.json","w") as file:
        json.dump(nans, file, indent=4)
    
    #print(filepaths_csv)
    

if __name__ == "__main__":
    filenames = {
        "cruz_ej": {
            "1" : [
                "cruz_ej1_0.pos",
                "cruz_ej1_3.pos",
                "cruz_ej1_4.pos",
                "cruz_ej1_8.pos",
                "cruz_ej1_12.pos",
                "cruz_ej1_13.pos",
                "cruz_ej1_15.pos",
                "cruz_ej1_21.pos",
                "cruz_ej1_24.pos",
                "cruz_ej1_27.pos",
                "cruz_ej1_35.pos",
                "cruz_ej1_40.pos",
                "cruz_ej1_44.pos",
                "cruz_ej1_48.pos",
                "cruz_ej1_52.pos",
                "cruz_ej1_55.pos",
                "cruz_ej1_57.pos",
                ],
            "2" : [
                "cruz_ej2_1.pos",
                "cruz_ej2_9.pos",
                "cruz_ej2_5.pos",
                "cruz_ej2_14.pos",
                "cruz_ej2_19.pos",
                "cruz_ej2_22.pos",
                "cruz_ej2_23.pos",
                "cruz_ej2_25.pos",
                "cruz_ej2_26.pos",
                "cruz_ej2_28.pos",
                "cruz_ej2_29.pos",
                "cruz_ej2_36.pos",
                "cruz_ej2_37.pos",
                "cruz_ej2_41.pos",
                "cruz_ej2_45.pos",
                "cruz_ej2_47.pos",
                "cruz_ej2_49.pos",
                "cruz_ej2_53.pos",
                "cruz_ej2_60.pos",
            ],
            "3" : [
                "cruz_ej3_2.pos",
                "cruz_ej3_6.pos",
                "cruz_ej3_7.pos",
                "cruz_ej3_10.pos",
                "cruz_ej3_11.pos",
                "cruz_ej3_16.pos",
                "cruz_ej3_17.pos",
                "cruz_ej3_18.pos",
                "cruz_ej3_20.pos",
                "cruz_ej3_43.pos",
                "cruz_ej3_59.pos",
            ],
            "4" : [
                "cruz_ej4_30.pos",
                "cruz_ej4_31.pos",
                "cruz_ej4_32.pos",
                "cruz_ej4_33.pos",
                "cruz_ej4_34.pos",
                "cruz_ej4_38.pos",
                "cruz_ej4_39.pos",
                "cruz_ej4_42.pos",
                "cruz_ej4_46.pos",
                "cruz_ej4_50.pos",
                "cruz_ej4_51.pos",
                "cruz_ej4_54.pos",
                "cruz_ej4_56.pos",
                "cruz_ej4_58.pos",
            ]
        },
        "pelota" : {
            "1" : [
                "pelota1_4.pos",
                "pelota1_7.pos",
                "pelota1_0.pos",
                "pelota1_1.pos",
                "pelota1_11.pos",
                "pelota1_14.pos",
                "pelota1_17.pos",
                "pelota1_20.pos",
                "pelota1_23.pos",
                "pelota1_24.pos",
                "pelota1_28.pos",
                "pelota1_30.pos",
                "pelota1_31.pos",
            ],
            "2": [
                "pelota2_2.pos",
                "pelota2_5.pos",
                "pelota2_8.pos",
                "pelota2_12.pos",
                "pelota2_15.pos",
                "pelota2_18.pos",
                "pelota2_21.pos",
                "pelota2_29.pos",
                "pelota2_32.pos",
            ]
        }
    }
    main()