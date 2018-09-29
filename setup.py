from setuptools import setup, find_packages


setup(
    name='ccxt-rest',
    version='0.0.1',
    description='RESTful ccxt',
    author='Ryo Murakami',
    # url='',
    # license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)