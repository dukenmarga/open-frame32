from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

exec(open("openFrame32/_version.py").read())
setup(
    name="openFrame32",
    packages=find_packages(),
    version=__version__,
    license="New BSD",
    description="openFrame32 is open source software for modeling and perform structural analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Duken Marga",
    author_email="dukenmarga@gmail.com",
    url="https://github.com/dukenmarga/openFrame32",
    # download_url = 'https://github.com/dukenmarga/openFrame32/',
    keywords=[
        "structural",
        "analysis",
        "civil",
        "engineering",
        "frame",
        "fem",
        "finite element",
    ],
    install_requires=[
        "numpy>=1.16",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
