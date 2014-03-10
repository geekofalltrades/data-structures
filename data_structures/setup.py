from setuptools import setup

long_description = """
Implementations of classic data structures in Python.
"""

setup(
    name="data-structures",
    version="0.1-dev",
    description="Classic Data Structures",
    long_description=long_description,
    # The project URL.
    url='http://github.com/geekofalltrades/data-structures',
    # Author details
    author='William Dougherty',
    author_email='thegeekofalltrades@gmail.com',
    # Choose your license
    #   and remember to include the license text in a 'docs' directory.
    # license='MIT',
    packages=['data_structures'],
    install_requires=['setuptools', ]
)
