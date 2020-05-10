from distutils.core import setup

setup(
    name='splunkconnector',
    version='1.0.0',
    include_package_data=True,
    packages=['splunkconnector'],
    package_data={
        'errors': ['*.json'],
        'test': ['*.json']
    },
    install_requires=['splunk-sdk'])
