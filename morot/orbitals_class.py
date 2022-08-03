"""
Module:
orbitals_class.py

This module implements the MolcasOrbitals class. The constructor requires a single parameter, namely the *.RasOrb
orbital file produced by a Molcas RASSCF calculation.
"""

import math
import os


class MolcasOrbitals:
    def __init__(self, in_orb_file) -> None:
        self.in_orb_file = in_orb_file
        self.out_orb_file = in_orb_file.split('/')[-1].split('.')[0] + ".RotOrb"

        self.output = []
        with open(self.in_orb_file, mode='r') as ifile:
            self.output = ifile.readlines()

        self.irreps = list(range(1, int(self.output[3].split()[1]) + 1))
        self.orbs_per_irrep = self.output[4].split()
        self.header = self.output[:self.output.index('* ORBITAL    1    1\n')]
        self.footer = self.output[self.output.index('#OCC\n'):]
        self.orbitals = self._get_orbitals()

    def _get_orbitals(self):
        mo_indexes = [idx for idx, item in enumerate(self.output) if "ORBITAL" in item or "#OCC" in item]
        orbitals = {}
        for idx in range(len(mo_indexes) - 1):
            myorb = "".join(self.output[mo_indexes[idx]+1:mo_indexes[idx+1]]).split()
            mo_tag = tuple(self.output[mo_indexes[idx]].split()[2:])
            orbitals[mo_tag] = myorb
        return orbitals

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
    def write_orbitals(self):
        try:
            os.unlink(self.out_orb_file)
        except FileNotFoundError:
            pass
        with open(self.out_orb_file, mode='a') as afile:
            afile.write("".join(self.header))
            for orb in self.orbitals.keys():
                line = "* ORBITAL    " + orb[0] + orb[1].rjust(5) + '\n'
                afile.write(line)
                for idx, coeff in enumerate(self.orbitals[orb]):
                    if (idx+1) % 5 == 0 and idx == len(self.orbitals[orb])-1:
                        afile.write(coeff.rjust(22))
                    elif (idx+1) % 5 == 0:
                        afile.write(coeff.rjust(22) + "\n")
                    else:
                        afile.write(coeff.rjust(22))
                afile.write("\n")
            afile.write("".join(self.footer))

    # a dunder to get readable representation of the object instance
    def __str__(self) -> str:
        return "class OrbRot with " + "#irreps=" + str(len(self.irreps)) + \
         ' and #mos in total=' + str(len(self.orbitals))
    
    # a dunder to get the #MOs present in the RasOrb file
    def __len__(self) -> int:
        return len(self.orbitals)
