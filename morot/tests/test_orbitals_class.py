"""
Unit and regression test for the morot package.
"""

# Import package, test suite, and other packages as needed
from morot.orbitals_class import MolcasOrbitals
import pytest


@pytest.fixture
def get_file() -> str:
    return "./dioxygen.RasOrb"

def test_len_dunder_c1(get_file) :
    """
    Testing the __len__() dunder method with orbitals w/o symmetry
    """
    input_mos = get_file
    print(input_mos)
    MOs = MolcasOrbitals(input_mos) 
    assert MOs.__len__() == 46