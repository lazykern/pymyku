:orphan:

.. currentmodule:: pymyku

Examples
========

This page is a collection of examples that demonstrate the use of pymyku.

Using client
------------

Import :class:`Client` from pymyku and initializing it with your credentials:

- :code:`USERNAME` -- Your nontri account username.
- :code:`PASSWORD` -- Your nontri account password.

.. code-block:: python

    from pymyku import Client
    
    client = Client('USERNAME', 'PASSWORD')

The initialization method of the :class:`Client` will automatically call :meth:`Client.initialize` methods to get the data required to work with the API.

Fetching
^^^^^^^^

The word :code:`fetch` for this class means getting a response from the API by sending a GET or POST request to the API.

The following examples show all methods of pymyku that fetch data from the APIs using the functions from :class:`requests`.

For example:

.. code-block:: python

    client.fetch_schedule()

Output: (the response from :ref:`:attr:`url.schedule``)

.. code-block:: python

    {
        "code": "success",
        "results": [{
            "std_id": -1,
            "std_code": "x",
            "gpax": -1.0,
            "total_credit": -1
        }]
    }

Geting
^^^^^^

The word :code:`get` for this class means getting a attribute from  the client or the result from the API (not response).

Arrtibutes
""""""""""

Attributes/Properties in the :class:`Client` object can be accessed directly by using the dot operator.

.. code-block:: python

    #: For getting the login response.
    client.login_response
    
    #: For getting the access token.
    client.access_token

    #: For getting your student code. Extracted from the login response.
    client.std_code

Or by using the :meth:`Client.get` method.

First, the enums from :mod:`pymyku.attribute` need to be imported to use with this method.

.. code-block:: python

    from pymyku.attribute import FetchedResponse, Token, Student

Next, you can use the :meth:`Client.get` method to get the attributes.

.. code-block:: python

    #: For getting the login response.
    client.get(FetchedResponse.LOGIN_RESPONSE)

    #: For getting the access token.
    client.get(Token.ACCESS_TOKEN)

    #: For getting your student code. Extracted from the login response.
    client.get(Student.STD_CODE)

Result from the API
"""""""""""""""""""

Methods that starts with :code:`get_` are methods that return the `result` from the API response.

For example:

.. code-block:: python

    client.get_enrolled_subjects(2565, 0)

This will return a :class:`list` of subjects that you enrolled in the summer term of 2565.

Searching
^^^^^^^^^

Methods that starts with :code:`search` will return the result from the API that is related to searching.

For example:

.. code-block:: python

    client.search_subject_id('013')

This will return a :class:`list` of subjects that start with the code "013".

Using requests
--------------

Import the :mod:`requests` module from pymyku and login.

.. code-block:: python

    from pymyku import requests, APP_KEY

    login_res = requests.login('USERNAME', 'PASSWORD')

Using the functions
^^^^^^^^^^^^^^^^^^^

You can use the predefined functions in :mod:`requests` to send requests to the MyKU API straightly.

Most functions have parameters that are required to send the request. e.g. `access_token`, `std_id`, etc.

But with :mod:`pymyku.requests`, you can pass the `login response` to the function.
The function will extract required parameters from the `login response` automatically.

.. code-block:: python

    requests.get_group_course(login_response = login_res)

You can also pass the :class:`Client` object to the function.

.. code-block:: python

    requests.get_group_course(client = client)

Otherwise, you pass the required parameters directly.

.. code-block:: python

    requests.get_group_course(access_token = 'ACCESS_TOKEN', std_id = 'STD_CODE')

Doing it directly
^^^^^^^^^^^^^^^^^

You can also use the :mod:`requests` module to send :func:`GET <requests.get>` or :func:`POST <requests.post>` request to the API you want.

.. code-block:: python

    requests.get(url = 'URL', headers = {'app-key':APP_KEY, 'x-access-token':'ACCESS_TOKEN'} params = {'THE_REQUIRED_PARAMETERS': 'THE_REQUIRED_PARAMETERS'})

To get the request headers easily, you can use the :func:`utils.gen_request_headers` function to generate the headers from the `login response` or your `access token`.

.. code-block:: python

    from pymyku import utils

    headers = utils.gen_request_headers('ACCESS_TOKEN')
    
    #headers = utils.gen_request_headers(login_res)

    requests.get(url = 'URL', headers = headers params = {'THE_REQUIRED_PARAMETERS': 'THE_REQUIRED_PARAMETERS'})

