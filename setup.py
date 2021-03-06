#!/usr/bin/env python

from setuptools import setup

setup(name="DetectorMorse",
      version="0.2",
      description="DetectorMorse, a sentence splitter",
      author="Kyle Gorman",
      author_email="gormanky@ohsu.edu",
      packages=["detectormorse"],
      install_requires=["nlup >= 0.3.0"],
      dependency_links=["http://github.com/cslu-nlp/nlup/archive/master.zip#egg=nlup-0.3.0"])
