import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="philter_mod",
    version="1.0.0",
    author="Beau Norgeot (modified by Mark Krass)",
    author_email="beaunorgeot@gmail.com",
    description="An open-source PHI-filtering software",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/markskrass/philter_mod",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
