import os
from setuptools import setup, find_packages
import pylom

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

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
    long_description_content_type="text/markdown",
    url="https://github.com/kennisnet/pylom",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries"
    ],
    install_requires = [
         'lxml'
         ]
)
