from setuptools import setup

setup(
    name='proxyorderedset',
    version='0.2',
    packages=['orderedset'],
    url='https://projects.cispa.saarland/c01dost/islearn',
    license='GNU GPLv3',
    author='Dominic Steinhoefel',
    author_email='dominic.steinhoefel@cispa.de',
    description='OrderedSet/FrozenOrderedSet implementation as a proxy to dict/frozendict',
    install_requires=[
        "attrs>=21.2.0",
        "iniconfig>=1.1.1",
        "frozendict>=2.3.1",
        "packaging>=21.0",
        "pluggy>=0.12.0",
        "py>=1.11.0",
        "pyparsing>=2.4.7",
        "pytest>=6.2.5",
        "pytest-html>=3.1.1",
        "pytest-metadata>=1.11.0",
        "toml>=0.10.2",
     ],
)
