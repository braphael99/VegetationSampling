import requests
import statistics
import sqlite3
from sqlite3 import Error
from scipy import stats
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
from flask import send_from_directory

app = Flask(__name__)
testMean = 0.0

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
def circumheightViz():
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

@app.route("/diamHeight/")
def diamheightViz():
    diameters =[]
    heights = []
    conn = None

    try:
        conn = sqlite3.connect("../dbs/vegetationSampling.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            SELECT vegetation_sampling.DBH, vegetation_sampling.height
            FROM vegetation_sampling
            ORDER BY vegetation_sampling.id
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            diameter = row["DBH"]
            height = row["height"]
            diameters.append(diameter)
            heights.append(height)

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()
    fig, ax = plt.subplots()
    plt.scatter(diameters, heights)
    plt.xlabel("Diameters (in CM)")
    plt.ylabel("Heights (in Meters)")
    plt.title("Diameters vs. Heights") 
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype = "image/png")

@app.route("/basiHeight/")
def basiheightViz():
    basiAreas =[]
    heights = []
    conn = None

    try:
        conn = sqlite3.connect("../dbs/vegetationSampling.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            SELECT vegetation_sampling.BA, vegetation_sampling.height
            FROM vegetation_sampling
            ORDER BY vegetation_sampling.id
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            basiArea = row["BA"]
            height = row["height"]
            basiAreas.append(basiArea)
            heights.append(height)

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()
    fig, ax = plt.subplots()
    plt.scatter(basiAreas, heights)
    plt.xlabel("Basal Areas (in Sq. Meter by Hectare)")
    plt.ylabel("Heights (in Meters)")
    plt.title("Basal Areas vs. Heights") 
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype = "image/png")

@app.route("/circumCorrel")
def circumCorrel():
    circumferences = []
    heights = []
    correlation = 0.0

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
    
    r = np.corrcoef(heights, circumferences)
    correlation = r[0][1]
    return {"correlation" : correlation}

@app.route("/diamCorrel")
def diamCorrel():
    diameters = []
    heights = []
    correlation = 0.0

    try:
        conn = sqlite3.connect("../dbs/vegetationSampling.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            SELECT vegetation_sampling.DBH, vegetation_sampling.height
            FROM vegetation_sampling
            ORDER BY vegetation_sampling.id
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            diameter = row["DBH"]
            height = row["height"]
            diameters.append(diameter)
            heights.append(height)

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()
    
    r = np.corrcoef(heights, diameters)
    correlation = r[0][1]
    return {"correlation" : correlation}

@app.route("/basiCorrel")
def basiCorrel():
    basiAreas = []
    heights = []
    correlation = 0.0

    try:
        conn = sqlite3.connect("../dbs/vegetationSampling.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            SELECT vegetation_sampling.BA, vegetation_sampling.height
            FROM vegetation_sampling
            ORDER BY vegetation_sampling.id
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            basiArea = row["BA"]
            height = row["height"]
            basiAreas.append(basiArea)
            heights.append(height)

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()
    
    r = np.corrcoef(heights, basiAreas)
    correlation = r[0][1]
    return {"correlation" : correlation}

@app.route("/newObservations/new", methods = ["POST"])
def insertObservations():
    newObservation= {}
    conn = None
    try:
        jsonPostData = request.get_json()
        CBH = int(jsonPostData["CBH"])
        height = float(jsonPostData["height"])
        DBH = float(jsonPostData["DBH"])
        BA = float(jsonPostData["BA"])
        dead = jsonPostData["dead"]

        if DBH > 10: 
            DBHclass = "1 cm < DBH <= 10 cm"
        
        else: 
            DBHclass = "DBH > 10 cm"
        
        
        conn = sqlite3.connect("../dbs/vegetationSampling.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            INSERT INTO vegetation_sampling (CBH, height, DBH, BA, dead, DBHclass) VALUES (?,?,?,?,?,?)    
        """
        cursor = conn.cursor()
        cursor.execute(sql, (CBH, height, DBH, BA, dead, DBHclass, ))
        conn.commit()
        conn.close()
        return redirect(f"/newObservations")
    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()

@app.route('/hypTest/new', methods = ["POST"])
def hypothTest():
    jsonPostData = request.get_json()
    testMean = float(jsonPostData["testMean"])
    heights = []
    conn = None
    try:
        conn = sqlite3.connect("../dbs/vegetationSampling.db")
        conn.row_factory = sqlite3.Row
        sql = """ 
            SELECT vegetation_sampling.height
            FROM vegetation_sampling
            ORDER BY vegetation_sampling.id
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            height = row["height"]
            heights.append(height)

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()

    heightSampStdDev = statistics.stdev(heights)
    heightSampMean = statistics.mean(heights)
    nObs = len(heights)

    tScore = (heightSampMean - testMean)/(heightSampStdDev/math.sqrt(nObs))
    degF = nObs - 1

    twoTailP = stats.t.sf(np.abs(tScore), degF) * 2
    leftTailP = stats.t.sf(np.abs(tScore), degF)
    rightTailP = 1 - stats.t.sf(np.abs(tScore), degF)
    ninetyCI = stats.t.interval(confidence = 0.90, df = degF, loc = heightSampMean, scale = heightSampStdDev)
    ninetyFiveCI = stats.t.interval(confidence = 0.95, df = degF, loc = heightSampMean, scale = heightSampStdDev)
    ninetyNineCI = stats.t.interval(confidence = 0.99, df = degF, loc = heightSampMean, scale = heightSampStdDev)

    return {"twoTailP": twoTailP,
            "leftTailP": leftTailP,
            "rightTailP": rightTailP,
            "ninetyCI": ninetyCI,
            "ninetyFiveCI": ninetyFiveCI,
            "ninetyNineCI": ninetyNineCI}

@app.route('/linearRegress')
def linearRegress():
    linearRegression = ""
    return {"linear regression": linearRegression}

@app.route('/images/<image_filename>')
def get_image(image_filename):
    image_directory = './resources/img/'
    return send_from_directory(image_directory, image_filename)

@app.route('/js/<js_filename>')
def get_js(js_filename):
    js_directory = './resources/js/'
    return send_from_directory(js_directory, js_filename)

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

@app.route("/newObservations")
def newObservations():
    return render_template("newObservations.html")

@app.route("/hypothesisTest")
def hypTestRen():
    return render_template("hypothesisTest.html")

#@app.route("/favicon.ico")
#def favIcon():
    #return send_from_directory('./resources/img/', "favicon.ico")

if __name__ == '__main__':
   app.run()