from setuptools import setup
from os import path
setup(
    name='imageserve',
    version='1.1.1',
    description='Serves jpg images to localhost:5000',
    author='David van der Pol',
    install_requires=[
        'flask',
        'Pillow',
    ],
    packages=['imageserve'],
    package_dir={'imageserve': 'imageserve'},
    package_data={'imageserve': ['templates/*.html']},
)
