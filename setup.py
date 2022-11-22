from setuptools import setup
import re

extra_requires = {
    "docs": [
        "sphinx==4.4.0",
        "sphinxcontrib_trio==1.1.2",
        "sphinxcontrib-websupport",
        "typing-extensions",
    ],
}
version = ""
with open("./pymyku/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    )
    if version:
        version = version.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name="pymyku",
    version=version,
    description="Python MyKU API Wrapper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    project_urls={
        "Documentation": "https://pymyku.readthedocs.io",
    },
    author="phusitsom",
    author_email="phusitsom@gmail.com",
    packages=["pymyku"],
    license_file="LICENSE.md",
    extras_require=extra_requires,
    url="https://github.com/phusitsom/pymyku",
    install_requires=["requests"],
    python_requires=">=3.6",
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
