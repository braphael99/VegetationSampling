import requests
import sqlite3
from sqlite3 import Error
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import math
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import jinja2
plt.style.use('ggplot')
matplotlib.use('agg')

from flask import Flask
from flask import abort
from flask import request
from flask import redirect
from flask import render_template
from flask import send_file
from flask import jsonify

app = Flask(__name__)

@app.route("/CBH")
def getCBH():
    circumferences = []
    conn = None
    try:
        conn = sqlite3.connect("../dbs/vegetationSampling.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            SELECT vegetation_sampling.id, vegetation_sampling.CBH
            FROM vegetation_sampling
            ORDER BY vegetation_sampling.id
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            circumference = {"id": row["id"], "circumference": row["CBH"]}
            circumferences.append(circumference)

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()

    return {"Circumferences": circumferences} 

@app.route("/height")
def getHeight():
    heights = []
    conn = None
    try:
        conn = sqlite3.connect("../dbs/vegetationSampling.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            SELECT vegetation_sampling.id, vegetation_sampling.height
            FROM vegetation_sampling
            ORDER BY vegetation_sampling.id
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            height = {"id": row["id"], "height": row["height"]}
            heights.append(height)

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()

    return {"Heights": heights} 

@app.route("/DBH")
def getDBH():
    diameters = []
    conn = None
    try:
        conn = sqlite3.connect("../dbs/vegetationSampling.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            SELECT vegetation_sampling.id, vegetation_sampling.DBH
            FROM vegetation_sampling
            ORDER BY vegetation_sampling.id
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            diameter = {"id": row["id"], "diameter": row["DBH"]}
            diameters.append(diameter)

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()

    return {"Diameters": diameters} 

@app.route("/BA")
def getBA():
    basiAreas = []
    conn = None
    try:
        conn = sqlite3.connect("../dbs/vegetationSampling.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            SELECT vegetation_sampling.id, vegetation_sampling.BA
            FROM vegetation_sampling
            ORDER BY vegetation_sampling.id
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            basiArea = {"id": row["id"], "basiArea": row["BA"]}
            basiAreas.append(basiArea)

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()

    return {"Basimetric Areas": basiAreas} 

@app.route("/dead")
def getDead():
    deaths = []
    conn = None
    try:
        conn = sqlite3.connect("../dbs/vegetationSampling.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            SELECT vegetation_sampling.id, vegetation_sampling.dead
            FROM vegetation_sampling
            ORDER BY vegetation_sampling.id
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            dead = {"id": row["id"], "dead": row["dead"]}
            deaths.append(dead)

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()

    return {"Dead": deaths} 


@app.route("/DBHClass")
def getDBHClass():
    classes = []
    conn = None
    try:
        conn = sqlite3.connect("../dbs/vegetationSampling.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            SELECT vegetation_sampling.id, vegetation_sampling.DBHclass
            FROM vegetation_sampling
            ORDER BY vegetation_sampling.id
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            dClass = {"id": row["id"], "DBH Class": row["DBHclass"]}
            classes.append(dClass)

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()

    return {"Classes": classes} 

@app.route("/circumHeight/")
def ageweightViz():
    circumferences =[]
    heights = []
    conn = None

    try:
        conn = sqlite3.connect("../dbs/vegetationSampling.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            SELECT vegetation_sampling.CBH, vegetation_sampling.height
            FROM vegetation_sampling
            ORDER BY vegetation_sampling.id
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            circumference = row["CBH"]
            height = row["height"]
            circumferences.append(circumference)
            heights.append(height)

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()
    fig, ax = plt.subplots()
    plt.scatter(circumferences, heights)
    plt.xlabel("Circumferences (in CM)")
    plt.ylabel("Heights (in Meters)")
    plt.title("Circumferences vs. Heights") 
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype = "image/png")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/circumferencePage")
def circumferencePage():
    return render_template("circumferencePage.html")

@app.route("/diameterPage")
def diameterPage():
    return render_template("diameterPage.html")

@app.route("/basiPage")
def basiPage():
    return render_template("basiPage.html")

@app.route("/predictiveStats")
def predictiveStats():
    return render_template("predictiveStats.html")

if __name__ == '__main__':
   app.run()