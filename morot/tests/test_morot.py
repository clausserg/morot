"""
Unit and regression test for the morot package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import morot


def test_morot_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "morot" in sys.modules
