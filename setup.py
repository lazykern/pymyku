import re
from pathlib import Path

from setuptools import setup

version = ""
with Path("pymyku/__init__.py").open() as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE,
    )
    if version:
        version = version.group(1)
    else:
        msg = "Unable to find version string."
        raise RuntimeError(msg)

setup(
    name="pymyku",
    version=version,
    description="Python MyKU API Wrapper",
    long_description=Path("README.md").open().read(),
    long_description_content_type="text/markdown",
    project_urls={
        "Documentation": "https://pymyku.readthedocs.io",
    },

    author="lazykern",
    author_email="lazykern@gmail.com",
    packages=["pymyku"],
    license_file="LICENSE.md",
    url="https://github.com/lazykern/pymyku",
    install_requires=["requests", "PyCryptodome"],
    python_requires=">=3.8",
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
