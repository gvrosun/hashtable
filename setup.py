from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='hashtable',
    version='1.0.1',
    description='HashTable with fixed size (Hashtable is similar to dictionary)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gvrosun/hashtable',
    author='Rosun GV',
    author_email='gvrosun@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=find_packages(where='HashTable'),
    python_requires='>=3.6, <4',
    install_requires=[],
    project_urls={
        'Bug Reports': 'https://github.com/gvrosun/hashtable/issues',
        'Source': 'https://github.com/gvrosun/hashtable',
    },
)
