import pandas as pd
import numpy as np


class FetchRowCSV:
    total_rows = 0
    previous_row = 0
    current_row = 0
    Row_list = []

    def __init__(self):

        df = pd.read_csv("./dataset/sensors.csv", dtype=np.float)

        for index, rows in df.iterrows():
            # Create list for the current row
            record_list = [int(rows.id), float(rows.Bearing1), float(rows.Bearing2), float(rows.Bearing3), float(rows.Bearing4)]
            self.total_rows = self.total_rows + 1
            # append the list to the final list
            self.Row_list.append(record_list)

    def get_next_row(self, current_row):
        self.current_row = current_row
        print("current row number :", self.current_row)
        return self.Row_list[self.current_row]

    def init_count(self):
        return self.total_rows
