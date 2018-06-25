import csv
from collections import OrderedDict


class CsvFile:

    def __init__(self, file_name):
        self.__file_name = file_name

    def read_record(self, record_container):
        with open(self.__file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            self.append_record_to_container(reader, record_container)

    def write_record(self, record_container):
        with open(self.__file_name, 'w', newline='\n') as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            self.write_record_to_csv(writer, record_container)

    @staticmethod
    def write_record_to_csv(writer, record_container):
        def extract_values_from_dict(one_record):
            return [one_record.values()]

        for record in record_container:
            writer.writerows(extract_values_from_dict(record))

    @staticmethod
    def append_record_to_container(reader, record_container):
        for row in reader:
            record_container.append(dict(row))

