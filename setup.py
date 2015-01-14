from setuptools import setup, find_packages
setup(
    name = "avgrabber",
    version = "0.1",
    packages = find_packages(),
    install_requires = [
        'click',
        'requests',
        'sqlalchemy',
        'dateutils',
        'lxml'
    ]
)