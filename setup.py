import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="PyRexoma",
    version="1.0.0",
    description="A Secure and Powerful Python-Pyrogram Based Library For Rexoma Bots",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MrAbhiX/PyRexoma",
    author="ABHISHEK THAKUR",
    author_email="mrabhixd03@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["PyRexoma"],
    include_package_data=True,
    install_requires=["requests"],#soon update
)
