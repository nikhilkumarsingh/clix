# -*- coding: utf-8 -*-
from setuptools import setup

def readme():
	try:
		with open('README.rst') as f:
			return f.read()
	except:
		pass

setup(name = 'clix',
	  version = '1.0.8',
	  classifiers = [
	  	'Development Status :: 4 - Beta',
	  	'License :: OSI Approved :: MIT License',
	  	'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
	  ],
	  keywords = 'clipboard manager tkinter gui desktop',
	  description = 'an easy to use clipboard manager made using tkinter.',
	  long_description = readme(),
	  url = 'https://github.com/nikhilkumarsingh/clix',
	  author = 'Nikhil Kumar Singh',
	  author_email = 'nikhilksingh97@gmail.com',
	  license = 'MIT',
	  packages = ['clix'],
	  install_requires = ['xerox'],
	  include_package_data = True,
	  entry_points="""
	  [console_scripts]
	  clix = clix.clix:main
	  """,
	  zip_safe = False)
