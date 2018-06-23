import csv

class CsvFile:

    def __init__(self, file_name):
        self.__file_name = file_name

    def read_record(self, record_container):

        with open(self.__file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                record_container.append(dict(row))



