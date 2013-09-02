# -*- coding: utf-8 -*-
import imp, sys, os
from os.path import abspath, dirname, join as pathjoin
from setuptools import setup

version = imp.load_source('_mod', abspath('elaphe/__version__.py')).VERSION
version = '.'.join(map(str, version))
install_requires = ['setuptools', 'Pillow']
test_requires = []
extra_requires = {}
long_description = '\n'.join([
    open(pathjoin(dirname(abspath(__file__)), 'README')).read(),
    ])

setup_params = dict(
    name="elaphe",
    version=version,
    packages=['elaphe'],
    exclude_package_data={
        'elaphe': ['postscriptbarcode']},
    package_data={
        'elaphe': ['postscriptbarcode/barcode.ps',
                   'postscriptbarcode/LICENSE']},
    zip_safe=False,
    install_requires = install_requires,
    tests_require=test_requires,
    extras_require=extra_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    author = "Yasushi Masuda",
    author_email = "whosaysni at gmail dot com",
    description = "Generates various barcodes using barcode.ps and PIL.",
    long_description=long_description,
    license = "New BSD",
    keywords = "barcode convert postscript image graphics",
    url = "http://bitbucket.org/whosaysni/elaphe/",
    test_suite = 'runner',
)

sys.path.insert(0, abspath('./tests'))
setup(**setup_params)
