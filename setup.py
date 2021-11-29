from os import read
from setuptools import setup, find_packages

setup(
    name= 'mypackage',
    version= '0.1',
    packages = find_packages(exclude=['test']),
    license= 'Tech reyal',
    description= 'This is a test function',
    long_description= open('ReadMe.md').read(),
    install_requires = 'numpy',
    url = 'https://github.com/David-gbenga/function_top_items.git',
    author= 'Kolawole david',
    author_email= 'kpeksorg@gmail.com'

)