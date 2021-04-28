import csv

def stream_csv(csv_filename = "./dataset/sensors.csv"):
    with open(csv_filename, "r", encoding="latin-1") as dataset:
        for data in csv.reader(dataset):
            yield data
def main():
    #filename = "./dataset/sensors.csv"
    iter_data = iter(stream_csv(filename))
    print(next(iter_data))

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted!")
        exit(0)