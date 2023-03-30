




from flask import Flask, jsonify
from sqlalchemy import create_engine
from datetime import datetime
from flask_restx import Api, Namespace, Resource, reqparse, inputs, fields 

import os
import sqlalchemy
SQLALCHEMY_SILENCE_UBER_WARNING = 1
SQLALCHEMY_WARN_20 = 0
import datetime
from sqlalchemy import create_engine, engine, text
import pandas as pd
import numpy as np
import streamlit as st


user = "root"
passw = "Capstone_Python"
host = "34.175.84.247"
database = "main"
db_port = 3306  


# need to instantiate a flask and a flask app 
app = Flask(__name__)

#is to say to the app that the host is here (not mandatory)
app.config["SQLALCHEMY_DATABASE_URI"] = host

#for the documentation page
#endpoint used for example customers and another one for sales
api = Api(app, version = '1.0',
    title = 'The famous REST API with FLASK!',
    description = """
        This RESTS API is an API to built with FLASK
        and FLASK-RESTX libraries
        """,
    contact = "jean-jacob.klat@student.ie.edu",
    endpoint = "/api/v1"
)

def connect_tcp_socket(
    db_host, db_user, db_pass, db_name, db_port = 3306
    ) -> sqlalchemy.engine.base.Engine:
    """ Initializes a TCP connection pool for a Cloud SQL instance of MySQL. """

    engine = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL.create(
            drivername="mysql+pymysql",
            username=user,
            password=passw,
            host=host,
            port=db_port,
            database=database,
        ),
    )
    return engine


engine = connect_tcp_socket(host, user, passw, database, db_port)
conn = engine.connect()

print(conn)



def disconnect(conn):
    conn.close()


def connect():
    db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(user, passw, host, database), \
    connect_args = {'connect_timeout': 10})
    conn = db.connect()
    return conn

def disconnect(conn):
    conn.close()


#This part of the code is how i would upload it to the database

# result = conn.execute("SHOW TABLES;").fetchall()
# for r in result:
#     print(r)
# if not result:
#   print("No tables in the DATABASE")

# articels_df = pd.read_csv("articles.csv")
# articels_df.to_sql(
#     con = conn, name = "H_M_articels", if_exists = "replace")

# customers_df = pd.read_csv("customers.csv")
# customers_df.to_sql(
#     con = conn, name = "H_M_customer", if_exists = "replace")


# transactions_df = pd.read_csv("transactions_sample.csv")
# transactions_df.to_sql(
#     con = conn, name = "H_M_transactions", if_exists = "replace")





#now we will begin with the code needed to make streamlit website



def load_data(query):
    try:
        data = pd.read_sql(query, conn)
    except Exception as e:
        print(e)
    return data 


auth_db={
    "ilovecapstone"

}






#names space customers has a drscription and a path, thss path will overwrite the endpoint given at the start.
#the endpoint at the starts will be the default namespace.
#have different name space for order: to seperate customers and workers
customers = Namespace('H_M_customer',
    description = 'All operations related to customers',
    path='/api/v1')
#here you add a new namespace, you woud overwrite it 
api.add_namespace(customers)
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
import sqlalchemy
import pandas as pd
from flask_restx import Api, Namespace, Resource

# ... (keep the rest of the imports and configurations as in your original code)

# Remove Streamlit code and change the filtering to use request arguments

@customers.route("/customers")
class get_all_customers(Resource):
    def get(self):
        if "Authorization" not in request.headers:
            return jsonify({"error": "unauthorized"})
        else:
            header = request.headers["Authorization"]
            token= header.split()[1]

            if token in auth_db:
                min_age = int(request.args.get('min_age', 1))
                max_age = int(request.args.get('max_age', 100))
                club_member_status = request.args.getlist('club_member_status')

                club_member_status_filtered_str = ', '.join(
                    "'{0}'".format(status) for status in club_member_status)

                if len(club_member_status) == 0:
                    club_member_status_filtered_str = "LIKE '%%'"
                else:
                    club_member_status_filtered_str = "IN (" + club_member_status_filtered_str + ")"

                conn = connect()
                select = """
                SELECT *
                FROM H_M_customer
                WHERE AGE BETWEEN {0} AND {1}
                AND club_member_status {2}
                LIMIT 7000;""".format(
                    min_age,
                    max_age,
                    club_member_status_filtered_str)
                result = conn.execute(select).fetchall()
                disconnect(conn)
                return jsonify({'result': [dict(row) for row in result]})
            
            else:
                return jsonify({"error": "unauthorized"})









articles = Namespace('H_M_articels',
    description = 'All operations related to articels',
    path='/api/v1')
#here you add a new namespace, you woud overwrite it 
api.add_namespace(articles)
@articles.route("/articles")
class get_all_articles(Resource):
    def get(self):
        if "Authorization" not in request.headers:
            return jsonify({"error": "unauthorized"})
        else:
            header = request.headers["Authorization"]
            token= header.split()[1]

            if token in auth_db:
                product_groups = request.args.getlist('product_group_name')
                colors = request.args.getlist('colour_group_name')

                product_group_filtered_str = ', '.join(
                    "'{0}'".format(product_group) for product_group in product_groups)

                if len(product_groups) == 0:
                    product_group_filtered_str = "LIKE '%%'"
                else:
                    product_group_filtered_str = "IN (" + product_group_filtered_str + ")"

                color_filtered_str = ', '.join(
                    "'{0}'".format(color) for color in colors)

                if len(colors) == 0:
                    color_filtered_str = "LIKE '%%'"
                else:
                    color_filtered_str = "IN (" + color_filtered_str + ")"

                conn = connect()
                select = """
                SELECT *
                FROM H_M_articels
                WHERE product_group_name {0}
                AND colour_group_name {1}
                LIMIT 7000;""".format(
                    product_group_filtered_str,
                    color_filtered_str)
                result = conn.execute(select).fetchall()
                disconnect(conn)
                return jsonify({'result': [dict(row) for row in result]})
            else:
                return jsonify({"error": "unauthorized"})






transactions = Namespace('H_M_transactions',
    description = 'All operations related to transactions',
    path='/api/v1')
#here you add a new namespace, you woud overwrite it 
api.add_namespace(transactions)
@transactions.route("/transactions")
class get_all_transactions(Resource):
    def get(self):
        if "Authorization" not in request.headers:
            return jsonify({"error": "unauthorized"})
        else:
            header = request.headers["Authorization"]
            token= header.split()[1]

            if token in auth_db:
                sales_channels = request.args.getlist('sales_channel_id')
                min_price = float(request.args.get('min_price', 0.0))
                max_price = float(request.args.get('max_price', 1.0))

                channel_filtered_str = ', '.join(
                    "'{0}'".format(sales_channel) for sales_channel in sales_channels)

                if len(sales_channels) == 0:
                    channel_filtered_str = "LIKE '%%'"
                else:
                    channel_filtered_str = "IN (" + channel_filtered_str + ")"

                conn = connect()
                select = """
                    SELECT *
                    FROM H_M_transactions
                    WHERE sales_channel_id {0}
                    AND price BETWEEN {1} AND {2}
                    LIMIT 7000;""".format(
                    channel_filtered_str,
                    min_price,
                    max_price)
                result = conn.execute(select).fetchall()
                disconnect(conn)
                return jsonify({'result': [dict(row) for row in result]})
            else:
                return jsonify({"error": "unauthorized"})




if __name__ == '__main__':
    app.run(debug = True)





