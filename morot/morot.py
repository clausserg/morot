"""Main module.

Python code to rotate by user-defined angles, two-by-two, molecular orbitals produced by
the RASSCF module of the OpenMOlcas quantum chemistry code.
"""

from orbitals_class import MolcasOrbitals


if __name__ == "__main__":
    mo_output_file = "./data/orbitals.RasOrb"
    myorbitals = []
    with open(mo_output_file, 'r') as rfile:
        myorbitals = rfile.readlines()

