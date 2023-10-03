import sqlite3
from sqlite3 import Error
import pandas as pd
import matplotlib.pyplot as plt
import math

from flask import Flask
from flask import abort
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route("/age")
def getAges():
    ages = []
    conn = None
    try:
        conn = sqlite3.connect("../dbs/birthweight.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            SELECT birthwt.ID, birthwt.age
            FROM birthwt
            ORDER BY birthwt.ID
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            age = {"id": row["id"], "age": row["age"]}
            ages.append(age)

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()

    return {"Ages": ages} 

@app.route("/age/average")
def getAvgAge():
    ages = []
    conn = None
    try:
        conn = sqlite3.connect("../dbs/birthweight.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            SELECT birthwt.age
            FROM birthwt
            ORDER BY birthwt.ID
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            age = row["age"]
            ages.append(age)

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()
    average = sum(ages)/len(ages)
    return {"Average Age": average} 