from progress import Progress, ProgressList


class Receptionist:

    def __init__(self):
        # data processor
        pass

    def listen_command(self):
        is_quit = False
        while not is_quit:
            is_quit, command = self.present_prompt()

    @staticmethod
    def present_prompt():
        command = input('>>> ')
        is_quit = True if command == 'q' else False
        return is_quit, command


class BulletinBoard:

    def __init__(self, record_container):
        self.__target_record = record_container

    def view_records(self):
        for record in self.__target_record:
            self.view_one_record(record.build_record())

    @staticmethod
    def view_one_record(record):
        for key, value in record.items():
            print(value, end=" ")
        print("")


class NewProgress:

    def __init__(self, record_container):
        self.__target_record = record_container

    def add_new_progress(self):
        if self.__target_record.add_progress(Progress()):
            return True
        print("not unique progress")
        return False


class SortedProgress:

    def __init__(self, record_container):
        self.__target_record = record_container

    def process_record(self):
        record_keys = list(self.__target_record[0].build_record().keys())
        for index, key in enumerate(record_keys):
            print("{0}:{1}".format(index, key), end=" ")
        sort_key = record_keys[int(input())]
        return sorted(self.__target_record, key=lambda key: key.build_record()[sort_key])
