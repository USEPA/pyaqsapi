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
   (reffer to the aqs_sign_up function, this only need to be done once).
2) Every time this library is reloaded aqs_credentials function
   must be called before continuing.

reffer to the `package documentation` <https://usepa.github.io/pyaqsapi/>
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
from .helperfunctions import *
from .setupfunctions import *
from .metadatafunctions import *
from .listfunctions import *
import pyaqsapi.bysite.bysite as bysite
import pyaqsapi.bycounty.bycounty as bycounty
import pyaqsapi.bystate.bystate as bystate
import pyaqsapi.bybox.bybox as bybox
import pyaqsapi.byma.byma as byma
import pyaqsapi.bypqao.bypqao as bypqao
import pyaqsapi.bycbsa.bycbsa as bycbsa


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
    # 'bysite/',
    # 'bycounty/',
    # 'bystate/',
    # 'byma/',
    # 'bypqao/',
    # 'bycbsa/',
    # 'bybox/',
    "listfunctions",
]
