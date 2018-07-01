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

    def add_new_record(self):
        self.__target_record.add_progress(Progress())

