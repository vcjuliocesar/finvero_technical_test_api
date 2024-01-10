# finvero technical test api
Welcome to the **finvero technical test api** repository! This is a simple guide to help you get started with settings up and running the project.
___

## Requirements
 
 * Python:3 :snake:

 * PIP:3 :snake:
 
 * Mysql

 ## Getting Started


Follow these steps to set up and run the project on your local machine:

### Clone the repository

```git
git clone git@github.com:vcjuliocesar/finvero_technical_test_api.git
```
### In the path where you cloned the project:

**Create enviroment file:** rename .env.example by .env

add your [belvo](https://sandbox.belvo.com) enviroment variables

**Example**
```
SECRETID=fdab73a3-fccc1-4a10-847b-5bb9c8b56fe2
SECRETPASSWORD=5_YiAQuiN@ixxxxXtXboyjSMWPIoyxFTiHAISozbkkcirH7T_AbFyO0yz9u1QarXX
LINKID=3eefa5b0-7af0-4632-a431-58c8ee401199
```
add your database enviroment variables

**Example**
```
DATABASE_NAME=finvero
DATABASE_USER=finvero
DATABASE_PASSWORD=Finvero_123
DATABASE_HOST=localhost
DATABASE_PORT=3306
```


It is important that you have python,pip and mysql installed on your computer

**Create a Virtual Environment**

```sh
python3 -m venv env
```

**Activate the Virtual Environment: On macOS/Linux**

```sh
source env/bin/activate
```

**On Windows**

```sh
.\env\Scripts\activate
```

**Install dependencies**

```sh
pip3 install --no-cache-dir requirements.txt
```

**Run the project**

```
uvicorn src.application.main:app --reload
```
Once the project is up and running, you can access it through your browser or API client.

**Default: [http://127.0.0.1:8000](http://127.0.0.1:8000/docs)**

### API Endpoint: [http://127.0.0.1:8000/api/v1/users](http://127.0.0.1:8000/api/v1/users)

### Description

This endpoint allows you to create users

#### Method
- **Method:** POST

#### Params
- **name** (required): User name
- **email** (required,unique): Email
- **password** (required): password

### Headers
- **Authorization:** Bearer {token} (autentication)

### Responses
- **code 200 OK**
```
{
  "message": "User created"
}
```

### API Endpoint: [http://127.0.0.1:8000/api/v1/users](http://127.0.0.1:8000/api/v1/login)

### Description

This endpoint allows you to log in

#### Method
- **Method:** POST

#### Params
- **email** (required): User name
- **password** (required): Password

### Responses
- **code 200 OK**
```
"TOKEN"
```

### API Endpoint: [http://127.0.0.1:8000/api/v1/users](http://127.0.0.1:8000/api/v1/transactions)

### Description

This endpoint return all payment transactions

#### Method
- **Method:** GET

### Headers
- **Authorization:** Bearer {token} (autentication)

### Responses
- **code 200 OK**
```
{
"results":[
    {
        "transaction_id": "0644634a-696e-42df-95e1-c05772d9a6ab",
        "category": "Income & Payments",
        "subcategory": "null",
        "type": "INFLOW",
        "amount": 380.03,
        "status": "PROCESSED",
        "balance": 25645.5,
        "currency": "MXN",
        "reference": "1128",
        "description": "DISPERSION",
        "collected_at": "2024-01-07T21:55:58.681926Z",
        "observations": "null",
        "accounting_date": "2023-12-28T07:36:31",
        "internal_identification": "51d312e3",
        "created_at": "2024-01-07T21:58:47.336358Z",
        "account_id": 1,
        "id": 1
    }
 ]
}
```

### API Endpoint: [http://127.0.0.1:8000/api/v1/users](http://127.0.0.1:8000/api/v1/accounts)

### Description

This endpoint return all accounts

#### Method
- **Method:** GET

### Headers
- **Authorization:** Bearer {token} (autentication)

### Responses
- **code 200 OK**
```
{
  "results": [
    {
      "link": "3eefa5b0-7af0-4632-a431-58c8ee401144",
      "currency": "MXN",
      "account_id": "b956d760-277a-4ef2-b551-d50f92b2aa44",
      "type": "Créditos",
      "agency": "5760218",
      "public_identification_name": "ACCOUNT_NUMBER",
      "name": "Cuenta perfiles",
      "balance_type": "LIABILITY",
      "created_at": "2024-01-09T15:03:52",
      "id": 31,
      "category": "LOAN_ACCOUNT",
      "number": "15946701",
      "internal_identification": "6379741",
      "public_identification_value": "5333643",
      "last_accessed_at": "2024-01-06T14:39:47",
      "bank_product_id": "4022243",
      "collected_at": "2024-01-09T15:03:52"
    }
  ]
}
```

### API Endpoint: [http://127.0.0.1:8000/api/v1/users](http://127.0.0.1:8000/api/v1/amounts_by_category)

### Description

This endpoint return all amounts by category

#### Method
- **Method:** GET

### Headers
- **Authorization:** Bearer {token} (autentication)

### Responses
- **code 200 OK**
```
{
  "results": [
    {
      "category": "bills_&_utilities",
      "transactions": [
        {
          "transaction_id": "00444d62-c1b6-4f1f-bd3f-7bce8903f669",
          "category": "Bills & Utilities",
          "type": "OUTFLOW",
          "status": "PROCESSED",
          "currency": "MXN",
          "description": "POR DOMICILIACION",
          "observations": null,
          "internal_identification": "27c7efdf",
          "account_id": 40,
          "id": 501,
          "subcategory": null,
          "amount": 695.98,
          "balance": 50010.21,
          "reference": "5272",
          "collected_at": null,
          "accounting_date": "2023-12-26T19:53:37",
          "created_at": null
        }
        ]
    }
    ]
}
```

### API Endpoint: [http://127.0.0.1:8000/api/v1/users](http://127.0.0.1:8000/api/v1/income_and_expense_analysis)

### Description

This endpoint return an income and expense analysis(financial distress,good financial health)

#### Method
- **Method:** GET

#### Params
- **account_id** (required): account id (UUI)

### Headers
- **Authorization:** Bearer {token} (autentication)

### Responses
- **code 200 OK**
```
{
  "message": "financial analysis"
}

```

### API Endpoint: [http://127.0.0.1:8000/api/v1/users](http://127.0.0.1:8000/api/v1/balance)

### Description

This endpoint return a total sum of income and expenses of the user's different accounts

#### Method
- **Method:** GET

#### Params
- **account_id** (required): account id (UUI)

### Headers
- **Authorization:** Bearer {token} (autentication)

### Responses
- **code 200 OK**
```
{
  "message": "balance $9255.56"
}

```

#### Happy Code! :smiley: