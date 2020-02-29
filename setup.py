"""
Imgur-python
-----------
A Python client for the Imgur API.
The original imgurpython project is no longer supported, so,
I decided to create my own python client for the Imgur API.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
version = '0.1.0'
requirements = [
    'requests>=2.0',
    'fleep>=1.0'
]
long_description = open('README.md').read()
    
config = {
    'name': 'imgur_python',
    'description': 'A Python client for the Imgur API',
    'long_description': long_description,
    'license': 'GPLv3+',
    'author': 'Fausto Carrera',
    'author_email': 'fausto.carrera.f@gmail.com',
    'url': 'https://github.com/faustocarrera/imgur-python/wiki',
    'download_url': 'https://github.com/faustocarrera/imgur-python',
    'version': version,
    'install_requires': requirements,
    'packages': ['imgur_python'],
    'include_package_data': True,
    'platforms': 'any',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)'
    ]
}

setup(**config)