from datetime import datetime
import re
from abc import ABCMeta, abstractmethod
from fileio import CsvFile
from collections import OrderedDict


class Record(metaclass=ABCMeta):

    @abstractmethod
    def build_record(self):
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
        self.__contest_name = self.input_loop(r'(ABC|ARC|AGC)([0-9]{3})', 'input contest name that you participated :')
        self.__problem_char = self.input_loop(r'(A|B|C|D|E|F)$', 'input problem ID [A-F]: ')

    def build_record(self):
        atcoder_record = OrderedDict({'Contest': self.__contest_name})
        atcoder_record.update(OrderedDict({'Problem': self.__problem_char}))
        return atcoder_record


class Problem(Record):

    def __init__(self):
        """

        :param AtCoder atcoder:
        :param str tag:
        """
        self.__atcoder = AtCoder()
        self.__tag = self.input_loop(r'[a-z]+', 'input problem tag: ')

    def build_record(self):
        problem_record = self.__atcoder.build_record()
        problem_record.update(OrderedDict({'Tag': self.__tag}))
        return problem_record


class Date(Record):

    def __init__(self):
        self.__date = datetime.today()

    def build_record(self):
        return OrderedDict({'Date': self.__date.strftime("%m-%d")})


class Progress(Record):

    def __init__(self):
        """

        :param Problem problem:
        :param Date date:
        """
        self.__problem = Problem()
        self.__date = Date()

    def build_record(self):
        progress_record = self.__problem.build_record()
        progress_record.update(self.__date.build_record())
        return progress_record


class ProgressList:

    def __init__(self):
        self.__progress_list = []

    def add_progress(self, progress):
        self.__progress_list.append(progress)

    def read_record_from_resource(self, resource):
        resource.read_record(self.__progress_list)

    def is_unique_record(self, progress):
        atcoder, value_list = [self.extract_atcoder(progress)], []
        for record in self.__progress_list:
            value_list.append(self.extract_atcoder(record))
        return len(set(atcoder) & set(value_list)) == 0

    @staticmethod
    def extract_atcoder(progress):
        atcoder_record = progress.build_record()
        return atcoder_record['Contest'] + atcoder_record['Problem']
