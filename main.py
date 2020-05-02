import json
import time
from pynput.keyboard import Listener, Controller


def data_reading():
    with open("abilities.json") as file:
        data = json.load(file)
        return data


def checking(key):
    if key in ['<96>', '<97>', '<98>', '<99>', '<100>', '<101>', '<102>', '<103>', '<104>', '<105>']:
        print("Casting the spell")
        return 'spell'
    elif key in ['p']:
        print('Casting a combo.')
        return 'combo'
    else:
        return False


def cast_spell(spell_name, data):
    print('casting {}'.format(spell_name))
    keyboard = Controller()
    keyboard.type(data[spell_name]["sphere_1"])
    keyboard.type(data[spell_name]["sphere_2"])
    keyboard.type(data[spell_name]["sphere_3"])
    time.sleep(.05)
    keyboard.type('r')
    time.sleep(.05)
    keyboard.type('t')


def cast_combo(combo, data):
    for one_spell in combo:
        cast_spell(one_spell, data)
        time.sleep(1)
    pass


def cast(key):
    data = data_reading()
    convert_list_spells = {'<96>': 'ghost_walk', '<97>': 'cold_snap', '<98>': 'ice_wall', '<99>': 'emp',
                           '<100>': 'tornado', '<101>': 'alacrity', '<102>': 'sunstrike', '<103>': 'forged_spirit',
                           '<104>': 'chaos_meteor', '<105>': 'deafening_blast'}
    convert_list_combo = {'p': ['tornado', 'emp', 'chaos_meteor', 'sunstrike', 'deafening_blast']}
    letter = str(key)
    letter = letter.replace("'", "")
    if checking(letter) == 'spell':
        cast_spell(convert_list_spells[letter], data)
    elif checking(letter) == 'combo':
        cast_combo(convert_list_combo[letter], data)

    with open("log.txt", 'a') as f:
        f.write(letter)


def main():
    print("This program lets you cast several skills and combos clicking on one button in Dota2 playing on Invoker.\n"
          "You must have given bindings before running the program q-quas, e-wex, a-exort.\n"
          "Here are indicated the spells and combos with their corresponding keys:\n"
          "0-ghost walk\n"
          "1-cold snap\n"
          "2-ice wall\n"
          "3-emp\n"
          "4-tornado\n"
          "5-alacrity\n"
          "6-sunstrike\n"
          "7-forged spirit\n"
          "8-chaos meteor\n"
          "9-deafening blast\n"
          "p-tornado+emp+meteor+sunstrike+blast")
    while True:
        with Listener(on_press=cast) as l:
            l.join()


main()
