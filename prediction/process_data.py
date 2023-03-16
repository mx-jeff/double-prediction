import pandas as pd
import matplotlib.pyplot as plt
import csv


def process_data(filepath:str="data/blaze_double.xlsx", output_path:str="data/clean.csv") -> pd.DataFrame:
    """get the data, clean and store to a csv model

    Args:
        filepath (str, optional): filepath. Defaults to "data/blaze_double.xlsx".
        output_path (str, optional): where the result file are being stored. Defaults to "data/blaze_double.xlsx".

    Returns:
        pd.DataFrame: a copy of dataframe for further process
    """
    df = pd.read_excel(filepath)
    deep_df = df.copy(deep = True)
    df = df[['Cor', "Minuto", "Data"]]

    df = df.replace({"\Dia: ": ''},regex=True)

    df['Tempo'] = df['Data'] + ' ' + df['Minuto']
    df = df.drop(columns=['Minuto', 'Data'], axis=1)
    df['Tempo'] = pd.to_datetime(df['Tempo'], format="%d/%m/%Y %H:%M")

    print(df.head())
    print(df.dtypes)

    df.index = df["Tempo"]
    
    numerical_columns = [col for col in df.columns if (df[col].dtype=='int64' or df[col].dtype=='float64')]
    print(numerical_columns)

    black = []
    white = []
    red = []

    for index, row in df.iterrows():
        if row['Cor'].lower() == "black":
            black.append(row['Cor'])

        if row['Cor'].lower() == "white":
            white.append(row['Cor'])
        
        if row['Cor'].lower() == "red":
            red.append(row['Cor'])

    print("black: ", len(black))
    print("white: ", len(white))
    print("red: ", len(red))

    df.to_csv(output_path)
    return deep_df
