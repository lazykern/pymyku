:orphan:

.. currentmodule:: pymyku

.. _intro:

Introduction
==============

This is the documentation for pymyku, a library for Python to aid
in creating applications that utilise the MyKU API.

Prerequisites
---------------

pymyku works with Python 3.6 or higher. Support for earlier versions of Python
is not provided.

Installing
----------

You can get the library directly from PyPI:

.. code-block:: bash

    python -m pip install pymyku

If you desire to install from a local source, you can do so:

.. code-block:: bash

    git clone https://github.com/pullinglazy/pymyku.git
    cd pymyku
    python -m pip install -r requirements.txt
    python -m pip install -e .

Basic Concepts
---------------

The goal of pymyku is to provide a simple and easy to use requestor for the MyKU API.
It provides a number of functions for interacting with the API, and provides a lot of useful utilities.

A quick example:

.. code-block:: python3

    import pymyku

    ku_client = pymyku.Client('USERNAME', 'PASSWORD')

    response = ku_client.fetch_gpax()

    print(response)

.. code-block:: text

    # Output:

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