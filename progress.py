from datetime import datetime
import re
from abc import ABCMeta, abstractmethod


class Record(metaclass=ABCMeta):

    @abstractmethod
    def init_record(self):
        pass

    @staticmethod
    def substitute_correct_data(correct_pattern, input_message):
        input_data = input(input_message)
        if re.match(correct_pattern, input_data):
            return True, input_data
        print("valid input data, retry input")
        return False, None

    def input_loop(self, pattern, input_message):
        is_correct_input, correct_data = False, None
        while not is_correct_input:
            is_correct_input, correct_data = self.substitute_correct_data(pattern, input_message)
        return correct_data


class AtCoder(Record):

    def __init__(self):
        """
        :param str contest_name:
        :param str problem_char:
        """
        self.__contest_name = str()
        self.__problem_char = str()
        self.init_record()

    def init_record(self):
        self.__contest_name = self.input_loop(r'(ABC|ARC|AGC)([0-9]{3})', 'input contest name that you participated :')
        self.__problem_char = self.input_loop(r'A|B|C|D|E|F','input problem ID [A-F]: ')

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



a=AtCoder()

