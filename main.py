import pandas as pd
from datetime import date
import numpy as np


def main():
    df = pd.read_csv('db-bonds-data.csv')
    indexes_list = []
    for row in range(len(df)):
        current_date = date.today()
        maturity_day, maturity_month, maturity_year = (df.at[row, 'bond_maturity_date']).split('/')
        maturity_date = date(int(maturity_year), int(maturity_month), int(maturity_day))
        days = np.busday_count(maturity_date, current_date)
        if abs(days) > 5:
            indexes_list.append(row)
    new_df = df.drop(indexes_list)
    new_df = new_df.reset_index(drop=True)
    print(new_df.to_string())




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
