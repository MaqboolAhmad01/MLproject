from setuptools import setup,find_packages
from typing import List
HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    """this function will return list of requirements"""
    req=[]
    with open(file_path) as fp:
        req=fp.readlines()
        req=[i.replace('\n','') for i in req]
        if HYPHEN_E_DOT in req:
            req.remove(HYPHEN_E_DOT)
    return req
setup(
    name='MLProject',
    version='0.0.1',
    author='maqbool',
    author_email='maqbool.riazahmad@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)
