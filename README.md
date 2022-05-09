<a href="">
    <img src="https://raw.githubusercontent.com/phusitsom/pymyku/main/docs/assets/pymyku_logo.png" alt="pymyku" title="pymyku" align="left" height="157" />
</a>

# PyMyKU

[![Language: Python](https://img.shields.io/badge/python-3.6+-white?style=flat-square&logo=python&logoColor=white&labelColor=376F9E&color=FDD043)](https://www.python.org/)
[![Request](https://img.shields.io/badge/-requests-376F9E?style=flat-square&logo=)](https://docs.python-requests.org/)

An unofficial [MyKU](https://my.ku.th/) API wrapper for python.
<br>

## Table of Contents

- [PyMyKU](#pymyku)
  - [Table of Contents](#table-of-contents)
  - [Notices](#notices)
  - [Documentation](#documentation)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [From PyPI](#from-pypi)
    - [From source](#from-source)
  - [Usage](#usage)
    - [Methods](#methods)
      - [Client](#client)
      - [Requests](#requests)
    - [Output](#output)
  - [Notes](#notes)

## Notices

This project was developed by KU students and is not affiliated with the university.
Please **respect** the API when using this project.

## Documentation

All the documentation is available on [the repository wiki](https://github.com/phusitsom/pymyku/wiki).

You can also use `help()` to see the docstrings of any modules in pymyku.

## Installation

### Prerequisites

- [Python](https://www.python.org/) 3.6+

### From PyPI

```bash
python -m pip install pymyku
```

### From source

```bash
git clone https://github.com/phusitsom/pymyku.git
cd pymyku
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Usage

You can use this library by importing the `pymyku` module to your script.

### Methods

Assume that `USERNAME` is the username of your Nontri account and `PASSWORD` is the password of your Nontri account.

#### Client

```python
import pymyku

ku_client = pymyku.Client('USERNAME', 'PASSWORD')

response = ku_client.fetch_gpax()

print(response)
```

#### Requests

```python
from pymyku import requests, TokenAttr
from pymyku.utils import extract

login_res = requests.request_login('USERNAME', 'PASSWORD')

access_token = extract(login_res, TokenAttr.ACCESS_TOKEN)

response = requests.get_gpax(access_token).json()

print(response)
```

### Output

```txt
{
    'code': 'success',
    'results': [
            {
                'std_id': '######',
                'std_code': '##########',
                'gpax': #.##,
                'total_credit': ##
            }
    ]
}
```

## Notes

The only goal of this project is to make it simpler to send API requests to MyKU.
There's no need to be concerned about the user's personal data being saved or shared.
