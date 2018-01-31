import os
from setuptools import find_packages, setup

import remake_music

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(
    os.path.normpath(
        os.path.join(
            os.path.abspath(__file__), os.pardir)))

with open(os.path.join(os.path.dirname(__file__),
                       'requirements.txt')) as req_fd:
    install_requires = req_fd.read().split('\n')

setup(
    name='remake_music',
    version=remake_music.__version__,
    packages=find_packages(),
    include_package_data=True,
    description='Remake music website',
    long_description=README,
    author='Alexey Tolkun',
    author_email='niree.xd@gmail.com',
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'app = remake_music.manage:main',
        ],
    },
)
