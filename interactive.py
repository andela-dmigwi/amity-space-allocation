#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    amity tcp <host> <port> [--timeout=<seconds>]
    amity serial <port> [--baud=<n>] [--timeout=<seconds>]
    amity (-i | --interactive)
    amity (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from app.room import Room
from app.person import Person


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    print()
    intro = '=' * 75 + '\nWelcome to AMITY ROOM ALLOCATION SYSTEM!' \
        + ' (type help for a list of commands.)' \
        + "\n click on the screen to be able to type\n" + '=' * 75

    prompt = '(Amity) '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_name>"""

        data = {}
        elements = arg['<room_name>'].replace(',', ' ').split(' ')
        for elem in elements:
            room_type = input('Type "O" for Office else it will be Living Space\n %s :' % elem)
            if 'o' in room_type.lower():
                data[elem] = 'office'
            else:
                data[elem] = 'livingspace'

        # Save each at a go and  display messages
        for key, value in data.items():
            print(Room().create_room(room_name=key, room_type=value))
        print('=' * 75)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <room_name> (FELLOW|STAFF) [<wants_accommodation>] """

        person_name = arg["<room_name>"]
        if arg['FELLOW'] is None:
            type_person = arg['STAFF']
        else:
            type_person = arg['FELLOW']

        need = arg['<wants_accommodation>'].lower()

        print (Person().add_person(person_name, type_person.lower(), need))
        print('=' * 75)

    @docopt_cmd
    def reallocate_person(self, arg):
        """reallocate_person <person_identifier> <room_name>"""

        person_name = arg['<person_identifier>']
        room_name = arg['<room_name>']

        print(Person().reallocate_person(person_name, room_name))
        print('=' * 75)

    @docopt_cmd
    def do_print_allocations(self, arg):
        """print_allocations [-o=filename]"""

        filename = arg['[-o=filename]']
        print(Room().get_allocations(filename))
        print('=' * 75)

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """print_unallocated [-o=filename]"""

        filename = arg['[-o=filename]']
        print(Room().get_unallocated(filename))
        print('=' * 75)

    @docopt_cmd
    def do_print_room(self, arg):
        """print_room <room_name>"""

        room_name = arg['<room_name>']

        print(Person().get_room_members(room_name))
        print('=' * 75)

    @docopt_cmd
    def do_save_state(self, arg):
        """save_state [--db=sqlite_database]"""

        print(arg)

    @docopt_cmd
    def do_load_state(self, arg):
        """load_state <sqlite_database>"""

        print(arg)

    @docopt_cmd
    def do_load_people(self, arg):
        """load_people <path to text file>"""

        print(arg)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        MyInteractive().cmdloop()
    except SystemExit:
        pass
    except KeyboardInterrupt:
        pass
