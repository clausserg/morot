"""Main module.

Python code to rotate by user-defined angles, two-by-two, molecular orbitals produced by
the RASSCF module of the OpenMOlcas quantum chemistry code.
"""


from orbitals_class import MolcasOrbitals
from functions import get_rasorb_file
from functions import get_mo_pairs


if __name__ == "__main__":
    molcas_rasorb_file = get_rasorb_file()
    MOs = MolcasOrbitals(molcas_rasorb_file)
    rotate_me = get_mo_pairs(MOs)
    for orbs, angle in rotate_me.items():
        MOs.rotate(orbs[0], orbs[1], float(angle))
    MOs.write_orbitals()
