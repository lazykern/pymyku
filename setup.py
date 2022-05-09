from setuptools import setup
from .pymyku import __version__

extra_requires = {
    'docs': [
        'sphinx==4.4.0',
        'sphinxcontrib_trio==1.1.2',
        'sphinxcontrib-websupport',
        'typing-extensions',
    ],
}

setup(
    name='pymyku',
    version=__version__,
    description='Python MyKU API Wrapper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='phusitsom',
    author_email='phusitsom@gmail.com',
    packages=['pymyku'],
    extras_require=extra_requires,
    url='https://github.com/phusitsom/pymyku',
    install_requires=['requests'],
    license='GNU General Public License v3.0',
    python_requires='>=3.6',
    classifiers=[
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
