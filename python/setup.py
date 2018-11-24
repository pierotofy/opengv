#!/usr/bin/env python

from __future__ import print_function

import setuptools
import os.path
from wheel.bdist_wheel import bdist_wheel


class platform_bdist_wheel(bdist_wheel):
    """Patched bdist_well to make sure wheels include platform tag."""
    def finalize_options(self):
        bdist_wheel.finalize_options(self)
        self.root_is_pure = False


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
    cmdclass={'bdist_wheel': platform_bdist_wheel},
)
