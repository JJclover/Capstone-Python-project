# README (API)

## **REST API with Flask and Flask-RESTx**

This repository contains the source code for a REST API built using Flask and Flask-RESTx. The API is designed to manage articles, transactions, and customers in a retail setting.

### **Overview**

The REST API provides access to the following resources:

- Articles
- Transactions
- Customers

It includes operations for fetching and filtering these resources. The API uses a simple token-based authentication system.

### **Installation**

To install the required packages, run:

```

pip install -r requirements.txt

```

### **Running the API**

To start the API server, simply run:

```

python main.py

```

**The API will be available at** 

[The famous REST API with FLASK!](https://api-dot-directed-racer-376415.oa.r.appspot.com/)

## **Required Modules**

Before using the REST API, the following Python modules must be installed:

```
SQLAlchemy
Flask
gunicorn== 20.1.0
flask-restx
pandas
numpy
streamlit
pymysql
PyYAML
config
```

### **API Endpoints**

### Authentication

- **`POST /api/v1/auth`**
    - Authenticate a user and return an access token.
    - Request body:
        - **`token`**: A valid token (string)
    - Response: JSON object containing an access token if authentication is successful.

### Articles

- **`GET /api/v1/articles`**
    - Fetch all articles, filtered by product group name and color group name.
    - Request headers:
        - **`Authorization`**: A valid access token.
    - Request query parameters:
        - **`product_group_name`**: List of product group names to filter by (strings, optional).
        - **`colour_group_name`**: List of color group names to filter by (strings, optional).
    - Response: JSON array of articles.

### Transactions

- **`GET /api/v1/transactions`**
    - Fetch all transactions, filtered by sales channel ID, minimum price, and maximum price.
    - Request headers:
        - **`Authorization`**: A valid access token.
    - Request query parameters:
        - **`sales_channel_id`**: List of sales channel IDs to filter by (strings, optional).
        - **`min_price`**: Minimum price to filter by (float, optional, default: 0.0).
        - **`max_price`**: Maximum price to filter by (float, optional, default: 1.0).
    - Response: JSON array of transactions.

### Customers

- **`GET /api/v1/customers`**
    - Fetch all customers, filtered by minimum age, maximum age, and club member status.
    - Request headers:
        - **`Authorization`**: A valid access token.
    - Request query parameters:
        - **`min_age`**: Minimum age to filter by (integer, optional, default: 1).
        - **`max_age`**: Maximum age to filter by (integer, optional, default: 100).
        - **`club_member_status`**: List of club member statuses to filter by (strings, optional).
    - Response: JSON array of customers.

### **Error Handling**

In case of errors, the API will return a JSON object containing an error message and an appropriate HTTP status code.

### **Authentication**

The API uses a simple token-based authentication system. Users must provide a valid token in the **`Authorization`** header of their requests to access protected endpoints.