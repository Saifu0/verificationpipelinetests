from setuptools import setup

setup(
    name='gitcopy',
    version='0.0.1',
    py_modules=['cli'],
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'gitcopy = cli:main',
        ],
    },
)
