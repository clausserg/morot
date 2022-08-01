"""Python program for rotating two-by-two molecular orbitals produced by the RASSCF module of the OpenMOlcas quantum chemistry package"""

# Add imports here
from .morot import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
