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
from amity import Amity


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
            room_type = input(
                'Type(O/L): "O" -> Office or "L" -> Living Space\n %s :' % elem)
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
        """Usage: add_person <person_name> (FELLOW|STAFF) [<wants_accommodation>] """

        person_name = arg["<person_name>"]
        stf = arg['STAFF']
        flw = arg['FELLOW']

        if stf is None:
            type_person = flw
        else:
            type_person = stf

        need = 'n'
        if arg['<wants_accommodation>'] is not None:
            need = arg['<wants_accommodation>']

        print (Person().add_person(
            person_name, type_person.lower(), need.lower()))
        print('=' * 75)

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_name> <room_name>"""

        person_name = arg['<person_name>']
        room_name = arg['<room_name>']

        print(Room().reallocate_room(person_name, room_name))
        print('=' * 75)

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""

        room_name = arg['<room_name>']

        print(Person().get_room_members(room_name))
        print('=' * 75)

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [<filename>]"""

        filename = arg['<filename>']
        list_return = Amity().get_allocations(filename)
        if type(list_return[0]) is list:
            print (list_return[0])
        else:
            for key, value in list_return[0].items():
                print('\tRoom Name:  ' + key)
                print('\t' + '-' * 50)
                print('\tOccupants: ' + str(value))
                print('\n')

        print('Office: ' + list_return[1])
        print('Living Space: ' + list_return[2])
        print('=' * 75)

    @docopt_cmd
    def do_print_empty_rooms(self, arg):
        """Usage: print_empty_rooms [<filename>]"""

        filename = arg['<filename>']
        list_return = Amity().get_unallocated(filename)
        if type(list_return[0]) is list:
            print (list_return[0])
        else:
            for key, value in list_return[0].items():
                print('\tRoom Name:  ' + key)
                print('\t' + '-' * 50)
                print('\tOccupants: ' + str(value))
                print('\n')

        print('Office: ' + list_return[1])
        print('Living Space: ' + list_return[2])
        print('=' * 75)

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """"Usage: print_unallocated [<filename>]"""

        filename = arg['<filename>']
        list_return = Amity().get_all_unallocated_people(filename)
        print('Unallocated Fellows : ' + str(list_return[0]))
        print (list_return[1])
        print ('Unallocated Staffs: ' + str(list_return[2]))
        print (list_return[3])
        print('=' * 75)

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people"""

        Amity().load_people()

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state """
        db = None

        Amity().save_state(db)

    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: load_state """

        # print(arg)
        Amity().load_state()

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('\t\t\tGood Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        MyInteractive().cmdloop()
    except SystemExit:
        pass
    except KeyboardInterrupt:
        pass
