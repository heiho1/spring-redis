from setuptools import setup, find_packages

setup(
    name = "spring-redis",
    version = "1.0",
    url = 'http://github.com/heiho1/spring-redis',
    license = 'BSD',
    description = "A Spring-Python wrapper for Redis",
    author = 'James Richards',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
