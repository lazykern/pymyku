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
"""""""""""""""""""""""""""""

    .. code-block:: python

        print(client.fetch_schedule())

    .. code-block:: bash


API Responses
-------------

POST
^^^^

:attr:`url.LOGIN`
"""""""""""""""""
.. code-block:: json

    {
    "accesstoken": "x",
    "renewtoken": "x",
    "user": {
        "loginName": "x",
        "userType": "x",
        "idCode": "x",
        "titleTh": "x",
        "titleEn": "x",
        "firstNameTh": "x",
        "firstNameEn": "x",
        "middleNameTh": "x",
        "middleNameEn": "x",
        "lastNameTh": "x",
        "lastNameEn": "x",
        "avatar": "x",
        "gender": "x",
        "student": {
            "loginName": "x",
            "stdId": "x",
            "stdCode": "x",
            "titleTh": "x",
            "titleEn": "x",
            "firstNameTh": "x",
            "middleNameTh": "x",
            "lastNameTh": "x",
            "firstNameEn": "x",
            "middleNameEn": "x",
            "lastNameEn": "x",
            "copenId": "x",
            "copenNameTh": "x",
            "copenNameEn": "x",
            "campusCode": "x",
            "campusNameTh": "x",
            "campusNameEn": "x",
            "facultyCode": "x",
            "facultyNameTh": "x",
            "facultyNameEn": "x",
            "departmentCode": "x",
            "departmentNameTh": "x",
            "departmentNameEn": "x",
            "majorCode": "x",
            "majorNameTh": "x",
            "majorNameEn": "x",
            "nationCode": "x",
            "nationalityNameTh": "x",
            "nationalityNameEn": "x",
            "studentStatusCode": "x",
            "studentStatusNameTh": "x",
            "studentStatusNameEn": "x",
            "studentTypeCode": "x",
            "studentTypeNameTh": "x",
            "studentTypeNameEn": "x",
            "edulevelCode": "x",
            "edulevelNameTh": "x",
            "edulevelNameEn": "x",
            "studentYear": "x",
            "advisorId": "x",
            "advisorNameTh": "x",
            "advisorNameEn": "x",
            "positionTh": "x",
            "email": "x",
            "mobileNo": "x"
        },
        "roleMenus": [{ "...": "..." }]
    },
    "cache": false
    }

