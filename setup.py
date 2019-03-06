#!/usr/bin/env python

import os
from setuptools import setup, find_packages

REQUIREMENTS = [line.strip() for line in
                open(os.path.join("requirements.txt")).readlines()]

setup(name='camerapose',
      version='0.1.0',
      url='https://github.com/brionmario/camera-pose-estimation-poc',
      description='Camera pose estimation using opencv',
      author='Brion Silva',
      author_email='brion@apareciumlabs.com',
      packages=find_packages(exclude=('tests', 'docs')),
      package_data={'camerapose': ['Readme.rst']},
      install_requires=REQUIREMENTS,
      include_package_data=True,
      license="The MIT License (MIT)"
      )
