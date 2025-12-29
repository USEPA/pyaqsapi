.. index:: Install pyaqsapi;
.. sectionauthor:: Clinton Mccrowey \<mccrowey \<DOT\>\ clinton \<AT\>\ epa.gov\>

Install pyaqsapi
================
The user has the choice of installing pyaqspi as a precompiled binary or from either
pypi or conda-forge or installing from source.

Packaged Binary install options (preferred method)
--------------------------------------------------
Most users should install pyaqsapi using one of the packaged binary install options below.

Packaged binary install of pyaqsapi from pypi.org using pip or (uv)[https://github.com/astral-sh/uv]
----------------------------------------------------------------------------------------------------
.. code-block:: console

   pip install pyaqsapi

   # List `pyaqsapi` metadata using pip:
   pip show pyaqsapi

   Alternatively, (uv)[https://github.com/astral-sh/uv] can be used as an alternative to pip by replacing the command
   `pip` with `uv pip` if `uv` is installed


Packaged binary install of pyaqsapi from conda-forge using conda or (mamba)[https://github.com/mamba-org/mamba}
----------------------------------------------------------------------------------
Installing pyaqsapi from the conda-forge channel can be achieved by adding conda-forge to your channels with:
.. code-block:: console

  conda config --add channels conda-forge
  conda config --set channel_priority strict

Once the conda-forge channel has been enabled, pyaqsapi can be installed with conda:
.. code-block:: console

  conda install pyaqsapi

mamba can be used as an alternative to conda:
.. code-block:: console

  mamba config --add channels conda-forge
  mamba --set channel_priority strict
  mamba install pyaqsapi

It is possible to list all of the versions of pyaqsapi available on your platform:
.. code-block:: console

  conda/mamba search pyaqsapi --channel conda-forge

Alternatively, conda/mamba repoquery may provide more information:
.. code-block:: console

  # Search all versions available on your platform:
  {conda/mamba} repoquery search pyaqsapi --channel conda-forge

  # List dependencies of `pyaqsapi`:
  {conda/mamba} repoquery depends pyaqsapi --channel conda-forge


Install pyaqsapi from source (manual install from github)
---------------------------------------------------------
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
