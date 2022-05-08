from setuptools import setup

setup(
    name='pymyku',
    version='0.1.0',
    description='Python MyKU API Wrapper',
    long_description=open('README.md').read(),
    author='phusitsom',
    author_email='phusitsom@gmail.com',
    packages=['pymyku'],
    url='https://github.com/phusitsom/pymyku',
    install_requires=['requests'],
    license='GNU General Public License v3.0',
    python_requires='>=3.6',
    classifiers=[
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
