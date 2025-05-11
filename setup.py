'''
Setup.py file is an essential part of packaging and distributing python projects. it is used by setuptools
(or distutils in older python versions) to define the configuration of your project, such as its metadata,
dependencies and more.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This Function will return the list of requirements
    '''
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not found")
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Vaibhav Kale",
    author_email="kalevaibhav2903@gmail.com",
    packages=find_packages(),
    install_requirements = get_requirements()
)