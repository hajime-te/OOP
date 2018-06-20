from datetime import datetime


class AtCoder:

    def __init__(self, contest_name, problem_char):
        """
        :param str contest_name:
        :param str problem_char:
        """
        self.__contest_name = contest_name
        self.__problem_char = problem_char

    def build_record(self):
        return {'Contest': self.__contest_name, 'Problem': self.__problem_char}


class Problem:

    def __init__(self, atcoder, tag):
        """

        :param AtCoder atcoder:
        :param str tag:
        """
        self.__atcoder = atcoder
        self.__tag = tag

    def build_record(self):
        problem_record = {'Tag': self.__tag}
        problem_record.update(self.__atcoder.build_record())
        return problem_record


class Date:

    def __init__(self):
        self.__date = datetime.today()

    def build_record(self):
        return {'Date': self.__date.strftime("%m-%d")}


class Progress:

    def __init__(self, problem, date):
        """

        :param Problem problem:
        :param Date date:
        """
        self.__problem = problem
        self.__date = date

    def to_data_record(self):
        progress_record = self.__date.build_record()
        progress_record.update(self.__problem.build_record())
        return progress_record


class ProgressList:

    def __init__(self):
        self.__progress_list = []

    def add_progress(self, progress):
        self.__progress_list.append(progress)


class Training:

    def __init__(self):
        pass

    def report_training(self):
        pass

    def create_atcoder(self):
        is_valid_input_contest = True
        while is_valid_input_contest:
            contest = input('Please enter the contest that you participated in: ')
            if contest in ["ABC", "ARC", "AGC"]:
                is_valid_input_contest = False

        




