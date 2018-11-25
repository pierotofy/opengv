#!/usr/bin/env python

from __future__ import print_function

import setuptools
import os.path


readme = os.path.join(os.path.dirname(__file__), "README.txt")

setuptools.setup(
    name='opengv',
    version='0.0.0a0',
    description='A collection of computer vision methods for solving '
                'geometric vision problems',
    long_description=open(readme).read(),
    url='https://github.com/laurentkneip/opengv',
    project_urls={
        "Documentation": "http://laurentkneip.github.io/opengv/",
    },
    author='Laurent Kneip',
    license='BSD',
    packages=['pyopengv'],
    package_data={
        'pyopengv': [
            'pyopengv.*',
        ]
    },
    ext_modules=[setuptools.Extension(name='pyopengv.pyopengv', sources=[])],
    zip_safe=False,
)
