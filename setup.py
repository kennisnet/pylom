import os
from setuptools import setup, find_packages
import pylom

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = pylom.__name__,
    version = pylom.__version__,
    author = "Wim Muskee",
    author_email = "w.muskee@kennisnet.nl",
    description = ("Library for parsing IMS-LOM xml records."),
    license = "MIT",
    keywords = "lom parsing xml",
    packages=find_packages(),
    long_description=read('README.md'),
    install_requires = [
         'lxml'
         ]
)
