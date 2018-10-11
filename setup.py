
from setuptools import setup, find_packages
from myapp.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='myapp',
    version=VERSION,
    description='MyApp Does Amazing Things!',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Brian Blackstone',
    author_email='brianblackstone.email@gmail.com',
    url='https://github.com/obsian/myapp/',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'myapp': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        myapp = myapp.main:main
    """,
)
