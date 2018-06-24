import csv


class CsvFile:

    def __init__(self, file_name):
        self.__file_name = file_name

    def read_record(self, record_container):
        with open(self.__file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            self.append_record_to_container(reader, record_container)

    def write_record(self, record_container):
        with open(self.__file_name, 'a', newline='') as csv_file:
            field_name = list(record_container[0].keys())
            writer = csv.DictWriter(csv_file, fieldnames=field_name)
            writer.writeheader()
            writer.writerows(record_container)

    @staticmethod
    def append_record_to_container(reader, record_container):
        for row in reader:
            record_container.append(dict(row))


