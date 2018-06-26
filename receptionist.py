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
