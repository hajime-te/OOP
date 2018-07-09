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

    def process_record(self):
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

    def process_record(self):
        if self.__target_record.add_progress(Progress()):
            return True
        print("not unique progress")
        return False


class SortedProgress:

    def __init__(self, record_container):
        self.__target_record = record_container

    def process_record(self):
        record_keys = list(self.extract_one_record(self.__target_record).keys())
        sort_key = self.input_loop(record_keys, 'input target key index: ')
        return sorted(self.__target_record, key=lambda record_key: record_key.build_record()[sort_key])

    def input_loop(self, record_keys, message):
        is_correct, sort_key = False, None
        self.show_list_key(record_keys)
        while not is_correct:
            is_correct, sort_key = self.get_correct_key_index(record_keys, message)
        return sort_key

    @staticmethod
    def get_correct_key_index(record_keys, message):
        try:
            key_index = record_keys[int(input(message))]
        except (ValueError, IndexError):
            print('input data is valid')
            return False, None
        return True, key_index

    @staticmethod
    def extract_one_record(record_container):
        return record_container[0].build_record()

    @staticmethod
    def show_list_key(record_keys):
        for index, key in enumerate(record_keys):
            print("{0}:{1}".format(index, key), end=" ")
        print("\n")