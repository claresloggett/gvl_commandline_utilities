#!/usr/bin/env python

"""[License: GNU General Public License v3 (GPLv3)]
 
 This file is part of galaxyfs.
 
 galaxyfs is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 galaxyfs is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import galaxyfs

from distutils.core import setup
from setuptools import setup, find_packages

setup(name='galaxyfs',
		version=galaxyfs.__version__,
		description='Mount galaxy via fuse',
		author=galaxyfs.__author__,
		maintainer=galaxyfs.__author__,
		license=galaxyfs.__license__,
		url=galaxyfs.__homepage__,
		scripts=["bin/galaxyfs"],
		packages=['galaxyfs'],
		install_requires=['fusepy','bioblend'],
		classifiers=[
			'Environment :: Console',
			'Intended Audience :: Science/Research',
			'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
			'Operating System :: OS Independent'
			'Topic :: Scientific/Engineering',
			'Topic :: Scientific/Engineering :: Bio-Informatics',
			],
	)
