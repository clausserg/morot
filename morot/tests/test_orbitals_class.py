"""
Unit and regression test for the morot package.
"""

# Import package, test suite, and other packages as needed
from morot.orbitals_class import MolcasOrbitals


def test_instance_attributes():
    """
    Testing some instance variables
    """
    input_mos = "../data/orbitals.RasOrb"
    MOs = MolcasOrbitals(input_mos)
    assert MOs.in_orb_file == input_mos and MOs.out_orb_file == "orbitals.RotOrb" and \
        len(MOs.irreps) == 8 and len(MOs.orbs_per_irrep) == 8 and \
            len(MOs.orbitals) == 710 and len(MOs.header) == 11 and \
                len(MOs.footer) == 388


