"""
Module:
orbitals_class.py

This module implements the MolcasOrbitals class. The constructor requires a single parameter, namely the *.RasOrb
orbital file produced by a Molcas RASSCF calculation supplied in a list-of-strings format.
"""

import math


class MolcasOrbitals:
    def __init__(self, output) -> None:
        self.irreps = list(range(1, int(output[3].split()[1]) + 1))
        self.orbs_per_irrep = output[4].split()
        self.output_header = output[:output.index('* ORBITAL    1    1\n')]
        self.output_footer = output[output.index('#OCC\n'):]
        self.orbitals = {}

        # let's fill the object instance with MOs
        mo_indexes = [idx for idx, item in enumerate(output) if "ORBITAL" in item or "#OCC" in item]
        for idx in range(len(mo_indexes) - 1):
            myorb = "".join(output[mo_indexes[idx]+1:mo_indexes[idx+1]]).split()
            mo_tag = tuple(output[mo_indexes[idx]].split()[2:])
            self.orbitals[mo_tag] = myorb

    # method to print out an orbital
    def print_orbital(self, irrep, mo_nr):
        return self.orbitals[(str(irrep), str(mo_nr))]

    # method to rotate two orbitals orbitals
    def rotate(self, mo_a, mo_b, angle):
        orb_a = self.orbitals[mo_a]
        orb_b = self.orbitals[mo_b]
        angle = math.radians(angle)
        # let's get the rotated orbitals
        rot_orb_a, rot_orb_b = [], []
        for idx in range(len(orb_a)):
            rot_orb_a.append('{:.14E}'.format(float(orb_a[idx])*math.cos(angle) + \
                float(orb_b[idx])*math.sin(angle)))
            rot_orb_b.append('{:.14E}'.format(float(orb_b[idx])*math.cos(angle) - \
                float(orb_a[idx])*math.sin(angle)))
        self.orbitals[mo_a] = rot_orb_a
        self.orbitals[mo_b] = rot_orb_b
    
    # method to write MO data of the object instance to a file
    def write_orbitals(self, file):
        with open(file, mode='a') as afile:
            afile.write("".join(self.output_header))
            # the following code needs to be fixed 
            for orb in self.orbitals.keys():
                line = "* ORBITAL    " + orb[0] + orb[1].rjust(5) + '\n' + "\n".join(self.orbitals[orb])
                afile.write(line)

    # a dunder to get readable representation of the object instance
    def __str__(self) -> str:
        return "class OrbRot with " + "#irreps=" + str(len(self.irreps)) + \
         ' and #mos in total=' + str(len(self.orbitals))
    
    # a dunder to get the #MOs present in the RasOrb file
    def __len__(self) -> int:
        return len(self.orbitals)
