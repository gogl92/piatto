import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "SaboresDeAsia",
    version = "0.0.1",
    author = "VRB",
    author_email = "luisarmando1234@gmail.com",
    description = ("Asian flavors."),
    license = "BSD",
    keywords = "restaurant asian",
    url = "https://gogl92.github.io/SaboresDeAsia/",
    install_requires=[
      'lxml',
      'html5lib',
      'beautifulsoup4',
    ],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
