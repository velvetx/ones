import argparse
import colorama
import pyfiglet
from src import requester
from src import data_parser
from src import writer

colorama.init(autoreset=True)


class Program:
    def __init__(self):
        self.greeting()
        self.args = self.creating_parser()
        self.results_of_requests = None
        self.list_with_data = None
        self.get_requests()
        self.get_parsed_data()
        self.get_result()

    @staticmethod
    def greeting():
        pyfiglet.print_figlet('ONES', font='isometric1')
        print(f'{colorama.Fore.MAGENTA}Processing...')

    @staticmethod
    def creating_parser():
        parser = argparse.ArgumentParser(description='A simple program that collects Russian names and surnames.')
        parser.add_argument('-c', '--count', type=int, help='Number of first and last names.', required=True)
        parser.add_argument('-p', '--path', default='logs', help='Path to save the result .')
        return parser.parse_args()

    def get_requests(self):
        return requester.Requester().starting_processing(self.args.count)

    def get_parsed_data(self):
        self.list_with_data = data_parser.DataParser().get_html_parser(self.get_requests())

    def get_result(self):
        writer.Writer().writing_to_file(self.args.path if self.args.path else None,
                                        self.list_with_data, self.args.count)


if __name__ == '__main__':
    try:
        Program()
    except KeyboardInterrupt:
        print(f'{colorama.Fore.RED}Exiting!')
    except EOFError:
        print(f'{colorama.Fore.RED}Exiting!')