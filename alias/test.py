import sys
import os
from subprocess import call


if not os.path.exists(os.path.expanduser('~/.alias')):
    os.mkdir(os.path.expanduser('~/.alias'))
HOME = os.path.expanduser('~/.alias')
print (HOME)
ALIAS_FILE = HOME + '/.aliases'  # File to store commands
ALIASN_FILE = HOME + '/.aliases_info'  # File to store number of commands


def print_error_message():
    print("Usages :\n1. als [options]")
    print("Options: list | reset ")
    print("2. als <command_name> \n <brief_description_of_the_command>")

def load():
    file = open(ALIAS_FILE)
    while 1:
        line = file.readline()
        line = line.strip('\n')
        call(line)
        if not line:
            break
        pass # do something
    file.close()


def main():
    command = sys.argv[1:]
    if not command:
        print_error_message()
        sys.exit(2)
    elif command[0] == 'load':
        load()
    elif command[0] == 'list':
        try:
            f = open(ALIAS_FILE, 'r')
        except IOError:
            print("You have no saved commands.")
            sys.exit(2)
        cmdno = 0
        for line in f.readlines():
            cmdno += 1
            print(str(cmdno) + "." + line[1:], end="")
        f.close()
    elif command[0] == 'reset':
        prompt = input("This will erase all of your stored commands. "
                       "Proceed ? (y/N)")
        if prompt.strip() in ('y', 'Y'):
            try:
                os.remove(ALIAS_FILE)
            except FileNotFoundError:
                pass
            try:
                os.remove(ALIASN_FILE)
            except FileNotFoundError:
                pass
        else:
            print("Aborted.")
    else:
        if not os.path.exists(ALIASN_FILE):
            f = open(ALIASN_FILE, 'w')
            f.write('0\n')
            f.close()

        f = open(ALIAS_FILE, 'a')
        new = ' '.join(command)
        desc = input("Alias Name : ")
        f.write("alias "+ desc + '=')
        f.write("'" + new + "'")
        #f.write('\n')
        f.close()

        f = open(ALIASN_FILE, 'r')
        n = int(f.readline())
        f.close()
        f = open(ALIASN_FILE, 'w')
        f.write(str(n+1) + '\n')
        f.close()
