"""
Module:
functions.py

This module implements functions that are used in the implementation of the main module
"""

import os.path


def get_rasorb_file():
    rasorb_file = ''
    while True:
        rasorb_file = input("Provide the full path + the name if the RasOrb file [e.g. /home/dumitruc/myorbitals.RasOrb]:")
        if os.path.exists(rasorb_file):
            return rasorb_file
        else:
            print("File not found! Please enter a valid path + file name.")


