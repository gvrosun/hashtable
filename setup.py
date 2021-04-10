import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hashtable-python",
    version="1.0.3",
    author="Rosun GV",
    author_email="gvrosun@gmail.com",
    description="HashTable implementation in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gvrosun/hashtable",
    project_urls={
        "Bug Tracker": "https://github.com/gvrosun/hashtable/issues",
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='HashTable, Data Stuctures, development',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires='>=3.6, <4',
)