from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = ['google-cloud-storage','tf-nightly-2.0-preview']

setup(
    name='text_classification',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='model for text classification'
)