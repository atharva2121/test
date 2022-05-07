from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fortest/__init__.py
from fortest import __version__ as version

setup(
	name="fortest",
	version=version,
	description="this is for testing purpose",
	author="Atharva Deshpande",
	author_email="adeshpande@dexciss.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
