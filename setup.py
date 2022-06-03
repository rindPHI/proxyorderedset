from setuptools import setup

setup(
    name='proxyorderedset',
    version='0.3',
    packages=['orderedset'],
    url='https://projects.cispa.saarland/c01dost/islearn',
    license='GNU GPLv3',
    author='Dominic Steinhoefel',
    author_email='dominic.steinhoefel@cispa.de',
    description='OrderedSet/FrozenOrderedSet implementation as a proxy to dict/frozendict',
    install_requires=[
        "frozendict>=2.3.2",
        "pytest-cov>=3.0.0",
        "pytest-forked>=1.3.0",
        "pytest-html>=3.1.1",
        "pytest-profiling>=1.7.0",
        "pytest-pycharm>=0.7.0",
        "pytest-rerunfailures>=10.2",
        "pytest-xdist>=2.4.0",
        "pytest>=6.2.5",
        "pytest>=7.1.2"
     ],
)
