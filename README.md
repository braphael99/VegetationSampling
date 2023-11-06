# VegetationSampling

Welcome to Vegetation Sampling!   
This is a Flask App that serves a simple web site focused on Data Science applications.  
Using a SQLite database, we access a small vegetation dataset and use its data to do some fun simple statistics.  
Here you can find data visualizations, hypothesis testing, confidence intervals, and even simple linear regressions.  
Users can also add in their own observations to manipulate the data themselves.  

### Getting Started  

I chose to serve my app through a virtual environment (venv), so thats how I recommend you go about it. These are instructions for running the app locally on Windows.  
First and foremost, make sure you have python installed, this can be found in the app store on Windows.  
Open PowerShell and navigate to the directory that VegetationSampling is in.  
In the python folder, install venv (`py -3 -m venv venv`).  
Next, activate the virtual environment by running the following in the python directory: `venv\Scripts\activate`. You only need to run the activation script from now on.   
Now you may need to install some of the packages we are using like Pandas, NumPy, and SciPy in your virtual environment.  
This can be done with `pip` (`pip install Pandas` for example). I recommend just going down the line with the packages I used, as I had some installed and others not.  
Now, we need to set up our environment. We need to set up our Flask app with the following commands: `$env:FLASK_APP = "app.py"` and `$env:FLASK_ENV = "development"`.  
Finally we are ready to start our Flask app with the following command: `flask run`.  
Now visit `127.0.0.1:5000` and the app should be running.  
Have fun!  

### Future Considerations  

-Implementing a delete observation feature  
-More rigorous and thorough interpretations  
-Website Icon  

### Licensing Information  
The Vegetation Sampling dataset was pulled from Kaggle, posted by user Miguel Rojas. This dataset is being used under the [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) licensing rights. Here is the [Original Dataset](https://www.kaggle.com/datasets/itsmiguelrojas/humid-forest-sampling/).  
