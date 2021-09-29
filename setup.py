from setuptools import setup, find_packages
import version

setup(
    name = 'pyextractor',
    packages = find_packages(),
    version = version.__version__,
    description = 'Extractor tool written in Python',
    author='Warkdev',
    url='',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Build Tools'
    ],
    zip_safe = False,
    install_requires = [],
    test_suite="tests"
)