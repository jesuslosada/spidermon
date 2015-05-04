from setuptools import setup, find_packages

setup(
    name         = 'spidermon',
    version      = '0.1',
    packages     = find_packages(),
    install_requires=[
        'six==1.9.0',
    ],
    tests_require=[
        'six==1.9.0',
        "pytest>=2.7.0",
    ]

)