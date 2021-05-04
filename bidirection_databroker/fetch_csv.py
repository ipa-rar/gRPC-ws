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


""" import csv
import time

def stream_messages():
    csv_filename = "./dataset/sensors.csv"
    with open(csv_filename, "r", encoding="latin-1") as dataset:
        for data in csv.reader(dataset):
            msg = dict(id=data[0],
            sensor1=data[1],
            sensor2=data[2],
            sensor3=data[3],
            sensor4=data[4])
            yield msg
            time.sleep(.01)

if __name__ =='__main__':
    ans = stream_messages()
    for data in ans:
        print(data) """
