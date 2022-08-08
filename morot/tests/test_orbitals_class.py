"""
Unit and regression test for the morot package.
"""

# Import package, test suite, and other packages as needed
from morot.orbitals_class import MolcasOrbitals


def test_instance_attributes_sym_d2h():
    """
    Testing some instance variables with orbitals obtained for berkelocene, symmetry D2h
    """
    input_mos = "../data/orbitals.RasOrb"
    MOs = MolcasOrbitals(input_mos)
    assert MOs.in_orb_file == input_mos and MOs.out_orb_file == "orbitals.RotOrb" and \
        len(MOs.irreps) == 8 and len(MOs.orbs_per_irrep) == 8 and \
            len(MOs.orbitals) == 710 and len(MOs.header) == 11 and \
                len(MOs.footer) == 388

def test_instance_attributes_sym_c1():
    """
    Testing some instance variables with orbitals obtained for molecular oxygen, symmetry=nosym
    """
    input_mos = "../data/dioxygen.RasOrb"
    MOs = MolcasOrbitals(input_mos)
    assert MOs.in_orb_file == input_mos and MOs.out_orb_file == "dioxygen.RotOrb" and \
        len(MOs.irreps) == 1 and len(MOs.orbs_per_irrep) == 1 and \
            len(MOs.orbitals) == 46 and len(MOs.header) == 11 and \
                len(MOs.footer) == 33