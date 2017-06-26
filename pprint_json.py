import json
import sys
from pprint import pprint
import argparse

version = "1.0.0"

def create_parser (params):

    if not params:
        params = ['-h']

    parser = argparse.ArgumentParser(
            prog='Pretty print',
            description = '''
            This program demonstrates pretty print of json''',
            epilog='''(c) Moscow 2017''',
            add_help=False
            )

    parent_group = parser.add_argument_group (title='Paramaters')

    parent_group.add_argument('--help', '-h', action='help', help='Help')



    parent_group.add_argument ('--version',
            action='version',
            help = 'Version number',
            version='%(prog)s {}'.format (version))

    parser.add_argument('-f', '--file', type=argparse.FileType())

    return parser.parse_args(params)


def load_data(filepath):
    js_obj = open(filepath, "r")
    p_obj = json.load(js_obj)
    return p_obj


def pretty_print_json(data):
    pprint(data)


if __name__ == '__main__':
    parser_command_line = create_parser(sys.argv[1:])
    
    if parser_command_line.file:
        p_obj = load_data(parser_command_line.file.name)
        pretty_print_json(p_obj)



