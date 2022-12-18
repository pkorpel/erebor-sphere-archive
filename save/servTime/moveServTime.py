import argparse
import itertools
import re
from os.path import exists


# Settings has a format of:
#     Section: { ID: { default: [], regex: [] } }
# where:
#     Section: is the name of the save block, such as WorldChar or WorldItem.
#     ID: is the identifier of the section, such as c_woman or i_pitcher_glass.
#         If the section doesn't have an ID then it matches to a special id "None" - useful for global variables at the beginning of the save
#         If a rule may appear under any ID then it can be written in a special id "ANY"
#     defaults: exact match values. Evaluation of values in this section is computationally cheaper.
#     regex:
settings = {
    'None': {
        'None': {
            'default': {'Time'}
        }
    },
    'VarNames': {
        'None': {
            'default': {'LastAuctionUpdate',
                        'treasureLastOpened',
                        'AuctionServTime',
                        'LastAuctionUpdate'
                        },
            'regex': {
                re.compile('treasureMapTime_\d+_\d+')
            }
        }
    },
    'WorldItem': {
        'i_memory_weekly_quest': {'default': {
            'Tag.KillStreak_time',
            'Tag.expiracyTime',
            'Tag.receptionTime'
        }},
        'i_pitcher_glass': {'default': {'Tag.lastMilking'}},
        'i_poisonManager': {'default': {'Tag.immunityUntil'}},
        'i_ring_power': {'default': {'Tag.basetime'}},
        'i_stealthbonus': {'default': {'Tag.hidetime'}},
        'i_frozenpad': {'default': {
            'Tag.fpDeactivatedTill',
            'Tag.removeTrap_DeactivatedTill'}},
        'i_pad_wallBuilding': {'default': {'Tag.removeTrap_DeactivatedTill'}},
        'i_poisonpad': {'default': {'Tag.tm'}},
        'i_relating_crystal': {'default': {'Tag.lastcheck'}},
        'i_spawnpad': {'default': {
            'Tag.removeTrap_DeactivatedTill',
            'Tag.spDeactivatedTill'}},
        'i_stealthbonus': {'default': {'Tag.hidetime'}},
        'i_switch_R': {'default': {'Tag.switchedTill'}},
        'i_switch_paralel': {'default': {'Tag.switchedTill'}},
        'i_switch_torch_R': {'default': {'Tag.switchedTill'}},
        'i_torch_paralel': {'default': {'Tag.switchedTill'}},
        'i_townstone': {'default': {'Tag.cas_dani'}},
        'i_treasureChest': {'default': {'Tag.vytvoreno'}},
        'i_varGate': {'default': {'Tag.vg_timeSeal_1'}},
        'i_worldgem_bit': {'default': {'Tag.paiduntil'}}
    },
    'WorldChar': {
        'ANY': {
            'default': {
                'Tag.GM_step_resist',
                'Tag.LastStepTime',
                'Tag.firststeptime',
                'Tag.lastlogoutedAt',
                'Tag.nextloot',
                'Tag.nextpotion',
                'Tag.nextress',
                'Tag.nextroundattack'
            }
        },
        'c_woman': {
            'default': {
                'Tag.HPsight_timer',
                'Tag.LastTamingAttemp',
                'Tag.isHealedUntil',
                'Tag.kudlyimmune',
                'Tag.nextSplitShot',
                'Tag.nextStrike',
                'Tag.nextTaunt_single',
                'Tag.nextcry',
                'Tag.nextdetect',
                'Tag.nextleap',
                'Tag.nextmask',
                'Tag.nextpact',
                'Tag.nextrangearrow',
                'Tag.nextroundattack',
                'Tag.nextthrow',
                'Tag.nextwoodoo',
                'Tag.omraceni_next',
                'Tag.podriznuti_next',
                'Tag.priest_next_selfres',
                'Tag.uderstitem_next'
            }
        },
        'C_A_MUSTANG_WIMMIMATE': {'default': {'Tag.jezdec_chcip'}},
        'C_BIRD_MAGPIE': {'default': {'Tag.jezdec_chcip'}},
        'c_bear_polar': {'default': {'Tag.npc_stun_nextHitTime'}},
        'c_bug_drone': {'default': {'Tag.npc_port_nextport'}},
        'c_bug_guard': {'default': {'Tag.npc_port_nextport'}},
        'c_bug_shadow': {'default': {'Tag.npc_port_nextport'}},
        'c_bug_warrior': {'default': {'Tag.npc_port_nextport'}},
        'c_cajun_child3': {'default': {'Tag.nextcry'}},
        'c_cyclops': {'default': {'Tag.jezdec_chcip'}},
        'c_cyclops_king': {'default': {'Tag.nextroundattack'}},
        'c_drapac': {'default': {'Tag.jezdec_chcip'}},
        'c_elem_earth': {'default': {'Tag.npc_stun_nextHitTime'}},
        'c_elem_earth_elder': {'default': {'Tag.npc_stun_nextHitTime'}},
        'c_elem_earth_terror': {'default': {'Tag.npc_stun_nextHitTime'}},
        'c_elem_ice': {'default': {
            'Tag.jezdec_chcip',
            'Tag.npc_stun_nextHitTime'}},
        'c_elem_snow': {'default': {
            'Tag.jezdec_chcip',
            'Tag.npc_stun_nextHitTime'}},
        'c_elem_snow_elder': {'default': {'Tag.nextroundattack'}},
        'c_ettin': {'default': {'Tag.jezdec_chcip'}},
        'c_ettin_lord': {'default': {'Tag.nextroundattack'}},
        'c_ettin_nb': {'default': {'Tag.multishot_time'}},
        'c_fireant_warrior': {'default': {'Tag.npc_port_nextport'}},
        'c_goblin_labyrint': {'default': {'Tag.jezdec_chcip'}},
        'c_harpy_stone': {'default': {'Tag.npc_stun_nextHitTime'}},
        'c_lizardman_chief': {'default': {'Tag.npc_port_nextport'}},
        'c_m_phoenix': {'default': {'Tag.npc_port_nextport'}},
        'c_minotaur': {'default': {'Tag.nextroundattack'}},
        'c_ogre_lord': {'default': {'Tag.nextroundattack'}},
        'c_ogre_mage': {'default': {'Tag.npc_curse_time'}},
        'c_ogre_suicider': {'default': {'Tag.nextroundattack'}},
        'c_pirat_mage_chief': {'default': {'Tag.npc_curse_time'}},
        'c_ratman_chief': {'default': {
            'Tag.npc_port_nextport',
            'Tag.npc_stun_nextHitTime'}},
        'c_skeleton_axe_lvl_4': {'default': {'Tag.nextroundattack'}},
        'c_skeleton_axe_lvl_5': {'default': {'Tag.nextroundattack'}},
        'c_skeleton_knight_lvl_4': {'default': {'Tag.nextroundattack'}},
        'c_spirit_obsidian': {'default': {'Tag.npc_curse_time'}},
        'c_spirit_verite': {'default': {'Tag.npc_curse_time'}},
        'c_terathan_drone': {'default': {'Tag.npc_port_nextport'}},
        'c_titan_lord': {'default': {'Tag.npc_stun_nextHitTime'}},
        'c_titan_overlord': {'default': {'Tag.npc_port_nextport'}},
        'c_treasureKeeper': {'default': {'Tag.lastOpened'}},
        'c_troll_snow': {'default': {'Tag.jezdec_chcip'}},
        'c_vguard_harad_mec_jezdec': {'default': {'Tag.jezdec_chcip'}},
        'c_vguard_rohan_hala_jezdec': {'default': {'Tag.npc_stun_nextHitTime'}},
        'c_worm_samec': {'default': {'Tag.npc_port_nextport'}},
        'c_zm_balrogh': {'default': {'Tag.nextroundattack'}},
        'c_zm_guard_archer': {'default': {
            'Tag.jezdec_chcip',
            'Tag.nextcry'}},
        'c_zm_minotaur': {'default': {'Tag.nextroundattack'}},
        'c_zm_strazce': {'default': {'Tag.nextroundattack'}}
    }
}


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
    c_print(CYAN, " S P H E R E S A V E   S E R V . T I M E   F I X E R")
    print()
    c_print(GREEN, f"Argumenty: {args.__dict__}")
    separator()


# H E L P E R S

def load_time(time):
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
    line = save_file.readline().rstrip()
    if (line != 'Title="Sphere World Script"'):
        save_file.close()
        err_print(f"Zadany soubor neni Sphere save, {line}")
        exit()

    output_file = open(path + '.out', 'w')
    output_file.write(line + '\r\n')

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
    The `match` property indicates if the current scope has any records in the `settings`,
    and may therefore contain a key-value pair for update
    """

    name: str
    id: str
    match: bool

    def __init__(self, name: str, id: str, match: bool) -> None:
        self.name = name
        self.id = str(id)
        self.match = match


# A L G O R I T H M
def process_scope(line: str):
    elements = line[1:].split(']')[0].split(' ')
    name = elements[0]
    id = None
    if len(elements) > 1:
        id = elements[1]

    if (name in settings and
            (str(id) in settings[name] or 'ANY' in settings[name])):
        match = True
    else:
        match = False

    return Scope(name, id, match)


def process_line(line: str, scope: Scope, reduction_time: int):
    parts = line.split('=', 1)
    if len(parts) < 2:
        return line

    context = settings[scope.name]
    if (scope.id in context):
        if ('default') in context[scope.id] and parts[0] in context[scope.id]['default']:
            return recompute_pair(parts, reduction_time)
        if ('regex') in context[scope.id]:
            for regex in context[scope.id]['regex']:
                if regex.fullmatch(parts[0]):
                    return recompute_pair(parts, reduction_time)

    if ('ANY' in context and parts[0] in context['ANY']):
        line = recompute_pair(parts, reduction_time)

    return line


def recompute_value(time_orig: str, reduction_time: int):
    time_new = int(time_orig) - reduction_time
    return str(time_new) if time_new > 0 else "0"


def recompute_pair(parts: list[str], reduction_time: int):
    return parts[0] + '=' + recompute_value(parts[1], reduction_time)


def process_save(save_file, output_file, reduction_time: int):
    scope = Scope("None", "None", True)
    for line in save_file:
        line = line.rstrip()
        if (len(line) > 0):
            if line[0] == '[':
                scope = process_scope(line)
            elif (scope.match):
                line = process_line(line, scope, reduction_time)

        output_file.write(line + '\r\n')


if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser(
        description="Script migrujici serv.time cas pro sphere save.")
    parser.add_argument(
        "-t", help="Cas o ktery se ma serv.time posunout zpet.")
    parser.add_argument("-f", help="Cesta k save, ktery se ma transformovat.")
    parser.add_argument(
        "--no-color", help="Vypne barevny vystup.", action="store_true")

    args = parser.parse_args()
    NoColor = args.no_color

    print_header()

    reduction_time = load_time(args.t)
    save_file, output_file = load_files(args.f)
    process_save(save_file, output_file, int(reduction_time))
