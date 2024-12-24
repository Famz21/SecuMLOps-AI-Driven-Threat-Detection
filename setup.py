from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    this function will return list of requirements
    
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            #Read lines from the file
            lines = file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
                ## Ignore the empty line and -e .
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

#print(get_requirements())

setup(
    name="SecuMLOps - AI Driven Threat Detection",
    version="0.0.1",
    author="Vira Rithy",
    author_email="rithyvira021@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)