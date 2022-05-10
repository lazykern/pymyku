:orphan:

.. currentmodule:: pymyku

Examples
========

This page is a collection of examples that demonstrate the use of pymyku.

Using Client
------------

Importing :class:`Client` from pymyku and initializing it with your credentials:

.. code-block:: python

    from pymyku import Client
    
    client = Client("USERNAME", "PASSWORD")

The initialization method of the :class:`Client` will automatically call 
:meth:`Client.login` and :meth:`Client.initialize` methods to get the data required to work with the API.

Fetching
^^^^^^^^
The word :code:`fetch` for this module means getting a response from the API by sending a GET or POST request to the API.

The following examples show all methods of pymyku that fetch data from the APIs.

:meth:`Client.fetch_schedule`

.. code-block:: python

    print(client.fetch_schedule())

Output the response from :ref:`:attr:`url.schedule``.