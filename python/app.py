import sqlite3
from sqlite3 import Error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import jinja2
plt.style.use('ggplot')

from flask import Flask
from flask import abort
from flask import request
from flask import redirect
from flask import render_template
from flask import send_file

app = Flask(__name__)

#import requests

#retrieve all national parks and pipe them into our local DB
#def fetch_parks_from_api():
    #api_url = 'https://developer.nps.gov/api/v1/parks?api_key=pP814qNL44jE9aIH9tXlbgNS3Ddn428wmokwPT4a'
    #response = requests.get(api_url)
    #if response.status_code == 200:
        #return response.json()
    #else:
        #return None

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

@app.route("/ageweight/")
def ageweightViz():
    ages =[]
    weights = []
    conn = None

    try:
        conn = sqlite3.connect("../dbs/birthweight.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            SELECT birthwt.age, birthwt.lwt
            FROM birthwt
            ORDER BY birthwt.ID
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            age = row["age"]
            weight = row["lwt"]
            ages.append(age)
            weights.append(weight)

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()
    fig, ax = plt.subplots()
    plt.scatter(ages, weights)
    plt.xlabel("Ages")
    plt.ylabel("Weights")
    plt.title("Mother's Age vs Last Menstural Weight") 
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype = "image/png")

@app.route("/home")
def index():
    return render_template("index.html")
if __name__ == '__main__':
   app.run()