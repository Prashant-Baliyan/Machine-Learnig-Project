from pytz import VERSION
from setuptools import setup
from typing import List



def get_requirements_list()-> List[str]:
    
    """
    Description: This function is going to return list of requirement mention in requirement.txt file.

    Retuen this function is going to return a list which contain name of libraries mention inrequirement.txt file.
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_file.readlines()

#Declaring variable for setup function
PROJECTNAME = "Housing-Predictor"
VERSION = "0.0.1"
AUTHOR = "Prashant Baliyan"
DESCRIPTION = "First Project on Housing Prediction"
PACKAGES = "housing"
REQUIREMENTS_FILE_NAME = 'requirements.txt'

setup(
name = PROJECTNAME,
version= VERSION,
author= AUTHOR,
description= DESCRIPTION,
packages= PACKAGES,
install_requires = get_requirements_list()
)
