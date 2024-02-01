import setuptools

# import logging
with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="veri-rag",  # This is the name of the package
    version="0.0.0",  # The initial release version
    author="Veriserve Vietnam",  # Full name of the author
    description="Veriserve library for LLM RAG application ",
    long_description=long_description,  # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(
        where="src"
    ),  # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Information to filter the project on PyPi website
    python_requires=">=3.9",  # Minimum version requirement of the package
    py_modules=["VeriRAG"],  # Name of the python package
    package_dir={"": "src"},  # Directory of the source code of the package
    install_requires=[],  # Install other dependencies if any
)
