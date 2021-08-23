

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name= "pebm",
    version="0.0.9",
    author="Example Author",
    author_email="sheina@campus.technion.ac.il",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "pebm"},
    packages=setuptools.find_packages(where="pebm"),
    package_data = {
        'c_files': ['*'],
        'wavedet_exe': ['*']
    },
    include_package_data=True,
    python_requires=">=3.6",
)