from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."
# To create your own package, you need to create a setup.py file.
"""The setup script is the center of all activity in building, distributing, and installing modules using the Distutils. 
The main purpose of the setup script is to describe your module distribution to the Distutils, so that the various commands 
that operate on your modules do the right thing."""


def get_requirement(file: str) -> List[str]:
    with open(file) as f:
        requirements = []
        with open(file) as f:
            requirements = f.read().splitlines()
            
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
                
            return requirements


setup(
    name='Diamond_Price_Prediction',
    version='0.1',
    author='Shreyash Singh',
    author_email="shreyashsingh865@gmail.com",
    install_requires=get_requirement("requirements.txt"),
    packages=find_packages(),
)

