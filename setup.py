from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-abw",  # the name that you will install via pip
    version="3.2",
    author="Aaron Watkins Jr",
    author_email="aaron.watkinsjr@gmail.com",
    description="Helper functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    # license="MIT",
    url="https://github.com/ekselan/lambdata-abw",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
