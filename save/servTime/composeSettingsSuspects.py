import argparse
import itertools
import pprint
from os.path import exists

results = {}

# C O L O R   P R I N T
NoColor = False

BLACK = 30
RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
PURPLE = 35
CYAN = 36
WHITE = 37


def with_color(c, s):
    return "%s" % s if NoColor else "\x1b[%dm%s\x1b[0m" % (c, s)


def t_print(message, tab_num=1):
    tabs = ""
    for _ in itertools.repeat(None, tab_num):
        tabs += "\t"

    print(tabs + message, flush=True)


def c_print(c, message):
    print(with_color(c, message), flush=True)


def succ_print(message):
    c_print(GREEN, message)


def err_print(message):
    c_print(RED, message)


def separator():
    print()
    print("--------------------------------------------------------------------------------\n", flush=True)


def print_header():
    print()
    c_print(CYAN, " S P H E R E S A V E   S E R V . T I M E   V A L U E S   F I N D E R")
    print()
    c_print(GREEN, f"Argumenty: {args.__dict__}")
    separator()


# H E L P E R S

def load_min_servtime(time):
    if not time:
        err_print(f"Na vstupu chybi povinny parametr -t")
        exit()

    try:
        return int(time)
    except ValueError:
        err_print(f"Vstup pro parametr -t musi byt cele cislo! ({time})")
        exit()


def load_files(path):
    if not path:
        err_print(f"Na vstupu chybi povinny parametr -f")
        exit()

    if not exists(path):
        err_print(f"Zadany soubor nebyl nalezen: '{path}'")
        exit()

    save_file = open(path, 'r')
    line = save_file.readline()
    if (line != 'Title="Sphere World Script"\n'):
        save_file.close()
        err_print(f"Zadany soubor neni Sphere save, {line}")
        exit()

    output_file = open(path + '-servtimes.txt', 'w')

    return save_file, output_file

# D A T A


class Scope:
    """
    Defines definition scope of the current processor. The scope is defined by the lines
    in brackets, e.g.
    ```
    [WorldItem i_box_brass]
    ```
    The `WorldItem` defines the scope name.
    The `i_box_brass` is the scope ID.
    """

    name: str
    id: str

    def __init__(self, name: str, id: str) -> None:
        self.name = name
        self.id = str(id)


# A L G O R I T H M
def process_scope(line: str):
    elements = line[1:].split(']')[0].split(' ')
    name = elements[0]
    id = None
    if len(elements) > 1:
        id = elements[1]

    return Scope(name, id)


def process_line(line: str, scope: Scope, min_servtime: int):
    parts = line.split('=', 1)
    if (len(parts) == 2 and matches_servtime(parts[1], min_servtime)):
        if not scope.name in results:
            results[scope.name] = {scope.id: {'default': {parts[0]}}}
        elif not scope.id in results[scope.name]:
            results[scope.name][scope.id] = {'default': {parts[0]}}
        else:
            results[scope.name][scope.id]['default'].add(parts[0])


def matches_servtime(value: str, min_servtime: int):
    try:
        int_val = int(value)
        return int_val > min_servtime
    except:
        return False


def process_save(save_file, min_servtime: int):
    scope = Scope("None", "None")
    for line in save_file:
        line = line.rstrip()
        if (len(line) > 0):
            if line[0] == '[':
                scope = process_scope(line)
            else:
                process_line(line, scope, min_servtime)


if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser(
        description="Script prochazi save a identifikuje klice, jejichz hodnota napadne vypada jako serv.time.")
    parser.add_argument(
        "-t", help="Minimalni ciselna hodnota, ktera ma identifikovat potencialni hodnotu representujici serv.time.")
    parser.add_argument("-f", help="Cesta k save, ktery se ma transformovat.")
    parser.add_argument(
        "--no-color", help="Vypne barevny vystup.", action="store_true")

    args = parser.parse_args()
    NoColor = args.no_color

    print_header()

    min_servtime = load_min_servtime(args.t)
    save_file, output_file = load_files(args.f)
    process_save(save_file, min_servtime)

    pp = pprint.PrettyPrinter(depth=4)
    output_file.write(pp.pformat(results))
