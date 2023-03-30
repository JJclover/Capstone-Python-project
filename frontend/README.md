# README (Frontend)

# **H&M Transaction Dashboard**

This is a README file for the H&M Transaction Dashboard application. The application utilizes Streamlit to create a web-based dashboard that allows users to view and analyze transaction, customer, and article data of the H&M store.

**Important to note, I already created two users with which you can login:**

1) username: jsmith     password: abc

2) username: rbriggs     password: def

**The Frontend will be available at:**

[Streamlit](https://frontend-dot-directed-racer-376415.oa.r.appspot.com/)

## **Table of Contents**

1. **[Installation](https://chat.openai.com/chat?model=gpt-4#installation)**
2. **[Usage](https://chat.openai.com/chat?model=gpt-4#usage)**
3. **[Features](https://chat.openai.com/chat?model=gpt-4#features)**
4. **[Code Structure](https://chat.openai.com/chat?model=gpt-4#code-structure)**

## **Installation**

### **Requirements**

- Python 3.6 or higher
- Streamlit
- pandas
- numpy
- sqlalchemy
- PyYAML
- requests
- streamlit-authenticator (optional)

### **Installing Dependencies**

To install the required dependencies, run the following command:

```

pip install -r requirements.txt

```

## **Usage**

To run the application, use the following command:

```

streamlit run main.py

```

## **Features**

The H&M Transaction Dashboard consists of the following features:

1. User authentication
2. Filters for transaction, customer, and article data
3. KPI cards displaying key metrics
4. Data visualizations (histograms) for various data attributes

## **Code Structure**

The **`main.py`** file contains the entire application code, which can be broadly divided into the following sections:

1. Importing required libraries
2. Loading configuration files
3. Setting up user authentication
4. Defining filter options and making API calls
5. Displaying transaction, customer, and article data
6. Calculating and displaying KPIs
7. Generating and displaying histograms for various data attributes

### **Configuration**

The application uses two configuration files:

- **`app.yaml`**: Contains the App Engine configuration.
- **`config.yaml`**: Contains custom configuration, such as user credentials, cookie settings, and preauthorized users.

### **Data Loading**

The application loads data from a REST API by making GET requests with the appropriate filters. The API calls are made using the **`requests`** library, and the response data is converted into pandas DataFrames for further processing.

### **Filters**

The dashboard allows users to apply various filters to transaction, customer, and article data. The filters include sales_channel_id, price range, age range, club_member_status, product_group_name, and color.

### **KPIs**

The application calculates and displays several key performance indicators (KPIs) based on the filtered data, such as the number of customers, number of articles, average age, number of transactions, average price, and number of active accounts.

### **Data Visualizations**

The dashboard includes several histograms that visualize the distribution of different data attributes, such as age, club_member_status, sales_channel_id, product_group_name, and section_name.