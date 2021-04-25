# Strata-Odata

## About
*Implemented in Django framework.
*In-memory sqlite db

### Use Cases
1. Accepts Entity Parameters from User and Call Create Entity API
 
  >Method:POST    
  >url:http://localhost:8000/People/
  
  >Request Body:
  ```
  {
      "UserName":"People20",
      "FirstName":"Lewis",
      "LastName":"Black",
      "Emails":[
          "lewisblack@example.com"
      ],
      "Age":23,
      "AddressInfo": [
      {
        "Address": "187 Suffolk Ln.",
        "City": {
          "Name": "Boise",
          "CountryRegion": "United States",
          "Region": "ID"
        }
      }
      ]
  }
  ```
  >Sample Response:
  ```
  {
    "Success": "True",
    "Message": "User created successfully",
    "id": 11,
    "name": "People9"
  }
  ```
2. Accepts a Search Parameter (ID) and display entities returned by search API:

  >Method:GET    
  >url: http://localhost:8000/People/id=People8/
  
  >Sample Response:
  
  ```
    {
  "UserName": "People8",
  "FirstName": "Lewis",
  "LastName": "Black",
  "MiddleName": "",
  "Gender": "",
  "Age": 23,
  "Emails": [
  "lewisblack@example.com"
  ],
  "AddressInfo": [
  {
  "Address": "187 Suffolk Ln.",
  "City": {
  "Name": "Boise",
  "CountryRegion": "United States",
  "Region": "ID"
  }
  }
  ]
  }
  ```
3. Get Filter Parameters from User and use the filter endpoint to fetch the results:
     
     >Method:GET
     >Url:http://localhost:8000/People/filter/?FirstName=Lewis&Age=23
     
     >Sample Response:
     
     ```
     [
    {
        "UserName": "People5",
        "FirstName": "Lewis",
        "LastName": "Black",
        "MiddleName": "",
        "Gender": "",
        "Age": 23,
        "Emails": [
            "lewisblack@example.com"
        ],
        "AddressInfo": [
            {
                "Address": "187 Suffolk Ln.",
                "City": {
                    "Name": "Boise",
                    "CountryRegion": "United States",
                    "Region": "ID"
                }
            }
        ]
    },
    {
        "UserName": "People6",
        "FirstName": "Lewis",
        "LastName": "Black",
        "MiddleName": "",
        "Gender": "",
        "Age": 23,
        "Emails": [
            "lewisblack@example.com"
        ],
        "AddressInfo": [
            {
                "Address": "187 Suffolk Ln.",
                "City": {
                    "Name": "Boise",
                    "CountryRegion": "United States",
                    "Region": "ID"
                }
            }
        ]
    },
    {
        "UserName": "People7",
        "FirstName": "Lewis",
        "LastName": "Black",
        "MiddleName": "",
        "Gender": "",
        "Age": 23,
        "Emails": [
            "lewisblack@example.com"
        ],
        "AddressInfo": [
            {
                "Address": "187 Suffolk Ln.",
                "City": {
                    "Name": "Boise",
                    "CountryRegion": "United States",
                    "Region": "ID"
                }
            }
        ]
    },
    {
        "UserName": "People8",
        "FirstName": "Lewis",
        "LastName": "Black",
        "MiddleName": "",
        "Gender": "",
        "Age": 23,
        "Emails": [
            "lewisblack@example.com"
        ],
        "AddressInfo": [
            {
                "Address": "187 Suffolk Ln.",
                "City": {
                    "Name": "Boise",
                    "CountryRegion": "United States",
                    "Region": "ID"
                }
            }
        ]
    },
    {
        "UserName": "People9",
        "FirstName": "Lewis",
        "LastName": "Black",
        "MiddleName": "",
        "Gender": "",
        "Age": 23,
        "Emails": [
            "lewisblack@example.com"
        ],
        "AddressInfo": [
            {
                "Address": "187 Suffolk Ln.",
                "City": {
                    "Name": "Boise",
                    "CountryRegion": "United States",
                    "Region": "ID"
                }
            }
        ]
    }
    ]    
     ```



## Installation and setup
***

```
$ git clone https://github.com/mayank-95/odata
$ cd odata
$ python manage.py migrate
$ python manage.py runserver (runs on port 8000 by default)
