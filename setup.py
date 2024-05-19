__doc__ = """
Manipulate audio with an simple and easy high level interface.

See the README file for details, usage info, and a list of gotchas.
"""

from setuptools import setup, find_packages

setup(
    name         = 'pydaab',
    version      = '0.25.2',
    author       = 'James Robert, Lam Nguyen',
    author_email = 'lamnguyenx@gmail.com',
    description  = 'Manipulate audio with an simple and easy high level interface',
    license      = 'MIT',
    keywords     = 'audio sound high-level',
    url          = 'http://pydaab.com',
    packages     = find_packages(where='src'),
    package_dir={'': 'src'},
    long_description=__doc__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Multimedia :: Sound/Audio :: Conversion",
        "Topic :: Multimedia :: Sound/Audio :: Editors",
        "Topic :: Multimedia :: Sound/Audio :: Mixers",
        "Topic :: Software Development :: Libraries",
        'Topic :: Utilities',
    ],
)
