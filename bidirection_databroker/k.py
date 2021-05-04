import csv
import time

def stream_messages():
    csv_filename = "./dataset/sensors.csv"
    with open(csv_filename, "r") as dataset:
        row = csv.reader(dataset, delimiter=",")
        for i, data in enumerate(row):
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
        print(data)

