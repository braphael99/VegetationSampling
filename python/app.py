#Author: Blake Raphael
#App Name: Vegetation Testing

#Importing all of our necessary python libraries
#**Could use some pruning, maybe in later releases we will sift through this**
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

#Naming our app for flask
app = Flask(__name__)

#Our first 6 routes are incredibly boring (created as a part of the proof of concept phase), as they are just basic
#routes that send raw JSON out. Could be useful in implmenting things down the road.

#Circumferences route (accesses database and sends raw JSON)
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

#Height route (access database and send raw JSON)
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

#Diameter route (accesses database and sends raw JSON)
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

#Basal Area route (accesses database and sends raw JSON)
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

#Dead route (accesses database and sends raw JSON)
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

#DBHClass route (accesses database and sends raw JSON)
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

#Our first interesting routes, sending graph data out

#Circumference and Height Graph route
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
            circumferences.append(float(circumference))
            heights.append(float(height))

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()

    #performing a linear regression to get our line of best fit
    res = stats.linregress(circumferences, heights)
    fig, ax = plt.subplots()

    #plotting both our scatter plot and line of best fit along with labeling our graph
    plt.plot(circumferences, heights, 'o', label = "original data")
    ax.axline((0,res.intercept), slope = res.slope, label = "fitted line", color = "blue")
    plt.xlabel("Circumferences (in CM)")
    plt.ylabel("Heights (in Meters)")
    plt.title("Circumferences vs. Heights")
    plt.legend()

    #converting our plot to an image to send to our webpage
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype = "image/png")

#Diameter and Height graph route
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
            diameters.append(float(diameter))
            heights.append(float(height))

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()

    #performing a linear regression to get our line of best fit
    res = stats.linregress(diameters, heights)     
    fig, ax = plt.subplots()

    #plotting both our scatter plot and line of best fit along with labeling our graph
    plt.plot(diameters, heights, 'o', label = "original data")
    ax.axline((0,res.intercept), slope = res.slope, label = "fitted line", color = "blue")
    plt.xlabel("Diameters (in CM)")
    plt.ylabel("Heights (in Meters)")
    plt.title("Diameters vs. Heights") 
    plt.legend()

    #converting our plot to an image to send to our webpage
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype = "image/png")

#Basal Area and Height graph route
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
            basiAreas.append(float(basiArea))
            heights.append(float(height))

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()
    

    #performing a linear regression to get our line of best fit
    res = stats.linregress(basiAreas, heights)     
    fig, ax = plt.subplots()

    #plotting both our scatter plot and line of best fit along with labeling our graph
    plt.plot(basiAreas, heights, 'o', label = "original data")
    ax.axline((0,res.intercept), slope = res.slope, label = "fitted line", color = "blue")
    plt.xlabel("Basal Areas (in Sq. Meter by Hectare)")
    plt.ylabel("Heights (in Meters)")
    plt.title("Basal Areas vs. Heights") 
    plt.legend()

    #converting our plot to an image to send to our webpage
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype = "image/png")

#Circumference and Height correlation coefficient route
#This route also handles our linear regression equation and r-squared value
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
    
    res = stats.linregress(circumferences, heights)
    r = np.corrcoef(heights, circumferences)
    correlation = r[0][1]
    return {"correlation" : correlation,
            "rSquared": res.rvalue**2,
            "slope": res.slope,
            "intercept": res.intercept}


#Diameter and Height correlation coefficient route
#This route also handles our linear regression equation and r-squared value
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
    
    res = stats.linregress(diameters, heights)
    r = np.corrcoef(heights, diameters)
    correlation = r[0][1]
    return {"correlation" : correlation,
            "rSquared" : res.rvalue**2,
            "slope" : res.slope,
            "intercept" : res.intercept}


#Basal Area and Height correlation coefficient route
#This route also handles our linear regression equation and r-squared value
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
    
    res = stats.linregress(basiAreas, heights)
    r = np.corrcoef(heights, basiAreas)
    correlation = r[0][1]
    return {"correlation" : correlation,
            "rSquared": res.rvalue**2,
            "slope": res.slope,
            "intercept": res.intercept}

#A new observations post route, taking user input from an HTML form and inserting it into our database
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

#our new hypothesis testing route, taking a user hypothetical mean and testing it
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

    #Setting up our variables for the t-tests and confidence intervals
    heightSampStdDev = statistics.stdev(heights)
    heightSampMean = statistics.mean(heights)
    nObs = len(heights)

    #calculating our t-scores and degrees of freedom
    tScore = (heightSampMean - testMean)/(heightSampStdDev/math.sqrt(nObs))
    degF = nObs - 1

    #calculating our p-values and confidence intervals
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

#our image accessing route
@app.route('/images/<image_filename>')
def get_image(image_filename):
    image_directory = './resources/img/'
    return send_from_directory(image_directory, image_filename)

#our javascript accessing route
@app.route('/js/<js_filename>')
def get_js(js_filename):
    js_directory = './resources/js/'
    return send_from_directory(js_directory, js_filename)

#our home page (index) route
@app.route("/")
def index():
    return render_template("index.html")

#circumference page route
@app.route("/circumferencePage")
def circumferencePage():
    return render_template("circumferencePage.html")

#diameter page route
@app.route("/diameterPage")
def diameterPage():
    return render_template("diameterPage.html")

#basal area page route
@app.route("/basiPage")
def basiPage():
    return render_template("basiPage.html")

#hypothesis test page route
@app.route("/hypothesisTest")
def hypTestRen():
    return render_template("hypothesisTesting.html")

#new observations page route
@app.route("/newObservations")
def newObservations():
    return render_template("newObservations.html")


if __name__ == '__main__':
   app.run()