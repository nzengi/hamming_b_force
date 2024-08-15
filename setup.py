from setuptools import setup, find_packages

setup(
    name="hamming_brute_force",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'numba'
    ],
    entry_points={
        'console_scripts': [
            'hamming_brute_force = main:main',
        ],
    },
)
