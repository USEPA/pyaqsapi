# -*- coding: utf-8 -*-
from setuptools import find_packages, setup


def readme():
    with open(file="README.md", encoding="utf8") as f:
        return f.read()


setup(
    name="pyaqsapi",
    version="1.0-beta",
    author="Clinton Mccrowey",
    author_email="mccrowey<DOT>clinton<at>epa<DOT>gov",
    description="Retrieve ambient air monitoring data from the United States \
                 Environmental Protection Agency’s (US EPA) Air Quality \
                 System (AQS) Data Mart API v2 interface.",
    install_requires=["wheel", "sphinx", "setuptools", "sphinx-rtd-theme"],
    zip_safe=False,
    project_urls={
        "Homepage": "https://github.com/USEPA/pyaqsapi",
        "AQS": "https://www.epa.gov/aqs",
        "AQS DataMart": "https://aqs.epa.gov/aqsweb/documents/data_mart_welcome.html",
        "RAQSAPI": "https://github.com/USEPA/RAQSAPI",
        "Issue Tracker": "https://github.com/USEPA/pyaqsapi/issues",
        "Source": "https://github.com/USEPA/pyaqsapi.git",
        "AQS Data Mart API": "https://aqs.epa.gov/aqsweb/documents/data_api.html",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
    ],
    packages=find_packages(exclude=["*.egg-info", "build", "dev"]),
    python_requires=">=3.8",
)
