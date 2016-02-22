from flask import render_template, flash, redirect, url_for
from app import app
from .forms import InputForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    download_form = InputForm()
    return render_template('home.html',
                           form=download_form)
