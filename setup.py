from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='imageserve',
    version='1.0.0',
    description='Serves jpg images to localhost:5000',
    author='David van der Pol',
    install_requires=[
        'flask',
        'Pillow',
    ],
    packages=['imageserve'],
    package_dir={'imageserve': 'imageserve'},
    package_data={'imageServe': ['templates/*.html']},
)
