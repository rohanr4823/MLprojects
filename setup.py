from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements,
    excluding `-e .` for `install_requires`.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != HYPHEN_E_DOT]
    return requirements

setup(
    name='MLproject',
    version='0.0.1',
    author='Rohan',
    author_email='rohanr4823@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
