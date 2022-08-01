"""Main module.

Python code to rotate by user-defined angles, two-by-two, molecular orbitals produced by
the RASSCF module of the OpenMOlcas quantum chemistry code.
"""


from orbitals_class import MolcasOrbitals
from functions import get_rasorb_file


if __name__ == "__main__":
    molcas_rasorb_file = get_rasorb_file()

    myorbitals = []
    with open(molcas_rasorb_file, 'r') as rfile:
        myorbitals = rfile.readlines()
    
    berk = MolcasOrbitals(myorbitals)
    print(berk)
    print(len(berk))

