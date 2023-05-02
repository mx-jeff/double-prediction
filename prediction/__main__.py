import pandas as pd
from ydata_profiling import ProfileReport


def get_profile_report(df, filename:str="data/blaze.html"):
    profile = ProfileReport(df)
    profile.to_file(filename)


def main():
    df = pd.read_excel("data/blaze_double.xlsx")
    # get_profile_report(df)
    df = df[['Cor', 'Número']]
    df = df.drop_duplicates()
    df['Número'].dropna(axis=0)
    print(df)
    get_profile_report(df, 'data/clean.html')
    

if __name__ == "__main__":
    main()
