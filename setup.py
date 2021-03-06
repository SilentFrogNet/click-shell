
from setuptools import setup, find_packages

# Set version
with open('VERSION', 'r') as f:
    __version__ = f.read().strip()

SHORT_DESCRIPTION = 'An extension to click that easily turns your click app into a shell utility'

# Use the README.md as the long description
with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

requirements = [
    'click>=6.0',
]

testing_requirements = [
    'coveralls',
    'pep8',
    'pylint>=1.5,<1.6',
    'pytest>=2.8,<2.9',
    'pytest-cov>=2.2,<2.3',
]


setup(
    name='click-shell',
    version=__version__,
    url='https://github.com/SilentFrogNet/click-shell',
    author='Ilario Dal Grande',
    author_email='info@silentfrog.net',
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license='BSD',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=requirements,
    dependency_links=[],
    extras_require={
        'testing': testing_requirements,
        'readline': ['gnureadline'],
        'windows': ['pyreadline'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: System :: Shells',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
