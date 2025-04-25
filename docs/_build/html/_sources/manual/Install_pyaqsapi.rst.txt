.. index:: Install pyaqsapi;
.. sectionauthor:: Clinton Mccrowey \<mccrowey \<DOT\>\ clinton \<AT\>\ epa.gov\>

Packaged binary install of pyaqsapi(preferred method)
=====================================================
Packaged binary install of pyaqsapi from pypi.org
-------------------------------------------------
.. code-block:: console

   pip install pyaqsapi

Install pyaqsapi from source (manual install from github)
=========================================================
To install pyaqsapi first clone the pyaqsapi repository.

.. code-block:: console

   git clone https://github.com/USEPA/pyaqsapi.git

Next, in the project's root directory use pip to install the proper
dependencies that are required to build
and install pyaqsapi.

.. code-block:: console

    pip install -r requirements.txt

While still in the project's root directory use setuptools to build and pip
to install the package.

.. code-block:: console

    python -m build .
    python -m pip install .