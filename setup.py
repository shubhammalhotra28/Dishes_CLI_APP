from setuptools import setup
setup(
    name = 'Dishes-Application-CLI',
    version = '0.1.0',
    packages = ['cli'],
    entry_points = {
        'console_scripts': [
            'cli = cli.__main__:main'
        ]
    })