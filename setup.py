# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in ahr/__init__.py
from ahr import __version__ as version

setup(
	name='ahr',
	version=version,
	description='AFS',
	author='AFS',
	author_email='afsbpo@afs.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
