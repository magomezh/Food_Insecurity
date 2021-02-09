"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask,render_template
from globalsuperstore import app
import time
import os



@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/visualizations')
def trends():
    """Renders the home page."""
    return render_template(
        'trends.html',
        title='Visualizations',
        year=datetime.now().year
    )


@app.route('/takeaways')
def sentiment():
    """Renders the contact page."""
    return render_template(
        'sentiment.html',
        title='Takeaways',
        year=datetime.now().year
        # message='Your contact page.'
    )

@app.route('/analysis')
def forecast():
    """Renders the contact page."""
    return render_template(
        'forecast.html',
        title='Analysis',
        year=datetime.now().year
        # message='Your Financial report page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        # message='Your application description page.'
    )
@app.route('/map')
def map_template():
    return render_template('map.html')

   
