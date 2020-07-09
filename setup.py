
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="hello",
    version="0.0.7",
    description="This is a test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atregubova/yadroTask"
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'gui_scripts': ['yadroTest=yadroTest.yadroTest:MainPage',],
    },
)
