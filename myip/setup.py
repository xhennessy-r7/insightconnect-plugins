# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='myip-rapid7-plugin',
      version='1.0.0',
      description='MyIP is a free service which returns your public routable IP address',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_myip']
      )