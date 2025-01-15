"""
pyaqsapi
--------
A python Interface to The United States Environmental Protection
Agency\'s Air Quality System Data Mart RESTful API server. pyaqsapi is a python
port of RAQSAPI
         
pyaqsapi is a package for python that connects the python programming
environment to the United States Environmental protection agency\'s
Air Quality System (AQS) Data Mart API for retrieval of air
monitoring data.

There are two things that you must do before using this package.
1) If you have not done so yet register your username with Data Mart,
   (refer to the aqs_sign_up function, this only need to be done once).
2) Every time this library is reloaded aqs_credentials function
   must be called before continuing.

refer to the `package documentation` <https://usepa.github.io/pyaqsapi/>
for more details about this package.

EPA Disclaimer
--------------
This software/application was developed by the U.S. Environmental Protection
Agency (USEPA). No warranty expressed or implied is made regarding the
accuracy or utility of the system, nor shall the act of distribution
constitute any such warranty. The USEPA has relinquished control of the
information and no longer has responsibility to protect the integrity,
confidentiality or availability of the information. Any reference to specific
commercial products, processes, or services by service mark, trademark,
manufacturer, or otherwise, does not constitute or imply their endorsement,
recommendation or favoring by the USEPA. The USEPA seal and logo shall not
be used in any manner to imply endorsement of any commercial product or
activity by the USEPA or the United States Government.
"""

from pyaqsapi import helperfunctions
from pyaqsapi import setupfunctions
from pyaqsapi import metadatafunctions
import pyaqsapi.bybox as bybox
import pyaqsapi.bycbsa as bycbsa
import pyaqsapi.bycounty as bycounty
import pyaqsapi.byma as byma
import pyaqsapi.bypqao as bypqao
import pyaqsapi.bysite as bysite
import pyaqsapi.bystate as bystate

from pyaqsapi.helperfunctions import *
from pyaqsapi.listfunctions import *
from pyaqsapi.metadatafunctions import *
from pyaqsapi.setupfunctions import *

# from pyaqsapi.bysite import bysite as bysite
# from pyaqsapi.bycounty import bycounty as bycounty
# from pyaqsapi.bystate import bystate as bystate
# from pyaqsapi.byma import byma as byma
# from pyaqsapi.bypqao import bypqao as bypqao
# from pyaqsapi.bycbsa import bycbsa as bycbsa
# from pyaqsapi.bybox import bybox as bybox


__all__ = [
    "helperfunctions",
    "metadatafunctions",
    "setupfunctions",
    "bysite",
    "bycounty",
    "bystate",
    "byma",
    "bypqao",
    "bycbsa",
    "bybox",
    "listfunctions",
]
