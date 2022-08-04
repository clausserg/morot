"""
Module:
functions.py

This module implements functions that are used in the implementation of the main module
"""

import os.path


def get_rasorb_file():
    rasorb_file = ''
    while True:
        rasorb_file = input("Provide the full path + the name if the RasOrb file\n[e.g. /home/dumitruc/myorbitals.RasOrb]:")
        if os.path.exists(rasorb_file):
            return rasorb_file
        else:
            print("File not found! Please enter a valid path + file name.")

def get_mo_pairs(available_mos):
    while True:
        try:
            nr_of_pairs = int(input("\nHow many MO pairs would you like to rotate?[e.g. 2]: "))
            break
        except ValueError:
            print("That is not a number, please try again!")
    mo_pairs = {}
    print("\nProvide with MO pair(s) to be rotated and corresponding angle(s)!")

    for idx in range(nr_of_pairs):
        while True:
            pair = tuple(input("Pair number {} [#irrep_nr, #orb1_index, #orb2_index, angle]: ".format(idx+1)).replace(" ", "").split(","))
            mo_a = (pair[:2])
            mo_b = (pair[0], pair[2])
            if mo_a in available_mos.orbitals.keys() and mo_b in available_mos.orbitals.keys():
                mo_pairs[(mo_a, mo_b)] = pair[3]
                print("In irrep {}, MO {} will rotate with MO {} by {} radians!".format(pair[0], pair[1], pair[2] , pair[3]))
                break
            else:
                print("One or both MOs specified in this pair is not present in the RasOrb file, check the MO indexes/irreps and try again!")
    return mo_pairs

    