from setuptools import setup

setup(
    name='bing-dict',
    version='0.1.0',
    packages=['bing-dict'],
    author='Wang Kai',
    author_email='kaiwkx@gmail.com',
    install_requires=['requests', 'beautifulsoup4'], # external packages as dependencies
    scripts=['bing-dict/bd'],
    license='MIT',
    long_description=open('README.txt').read()
)
