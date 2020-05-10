from distutils.core import setup

setup(
    name='splunkconnector',
    version='1.0.0',
    include_package_data=True,
    packages=['splunkconnector', 'splunkconnector.src', 'splunkconnector.utils',
              'splunkconnector.errors', 'splunkconnector.test'],
    package_data={
        'errors': ['*.json'],
        'test': ['*.json']
    })
