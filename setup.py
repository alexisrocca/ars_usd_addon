from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ars_usd_addon/__init__.py
from ars_usd_addon import __version__ as version

setup(
	name="ars_usd_addon",
	version=version,
	description="Conversor connected to DolarSi API (https://www.dolarsi.com/api/api.php?type=dolar)",
	author="IT-IEA",
	author_email="it@iea.com.ar",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
