#!/usr/bin/env python
import os
import os.path as op
from flask import Flask, render_template, request, redirect, url_for

import flask_admin as admin
from flask_admin.contrib import fileadmin

##################################################
# Create flask app
##################################################
app = Flask(__name__, template_folder='templates', static_folder='files')

# Create dummy secrey key so we can use flash
app.config['SECRET_KEY'] = '123456790'

##################################################
# HOME
##################################################
@app.route('/')
def index():
    # importing .jpg from files dir
    # =======================================================
    images = []    
    for file in os.listdir("files"):
        if file.endswith(".jpg"):
            images.append(os.path.join("files", file))
        else:
            continue         

    # image description
    # =======================================================
    txt_file = open("files/descriptions/description.txt").read().strip()
    t = txt_file.split()

    # company description
    # ========================================================
    company_txt_file = open("files/descriptions/company.txt").read().strip()

    # company slogan description
    # ========================================================
    company_slogan_txt_file = open("files/descriptions/company_slogan.txt").read().strip()

    return render_template('index_new.html', images=images, 
                                             txt_file=t,
                                             company_txt_file=company_txt_file,
                                             company_slogan_txt_file=company_slogan_txt_file)

##################################################
# ADD DESCRIPTION
##################################################
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        add = request.form['add']
        txt_file = open("files/descriptions/description.txt", "a")    
        txt_file.write(add + "\n")
        txt_file.close()
    return redirect(url_for('fileadmin.edit'))   

##################################################
# COMPAMY DESCRIPTION
##################################################
@app.route('/company', methods=['POST'])
def company():
    if request.method == 'POST':
        company = request.form['company']
        txt_file = open("files/descriptions/company.txt", "w")    
        txt_file.write(company + "\n")
        txt_file.close()
    return redirect(url_for('fileadmin.edit'))

##################################################
# COMPAMY SLOGAN DESCRIPTION
##################################################
@app.route('/company_slogan', methods=['POST'])
def company_slogan():
    if request.method == 'POST':
        company_slogan = request.form['company_slogan']
        txt_file = open("files/descriptions/company_slogan.txt", "w")    
        txt_file.write(company_slogan + "\n")
        txt_file.close()
    return redirect(url_for('fileadmin.edit'))            


if __name__ == '__main__':
    # Create directory
    path = op.join(op.dirname(__file__), 'files')
    try:
        os.mkdir(path)
    except OSError:
        pass

    # Create admin interface
    admin = admin.Admin(app, 'Files')
    admin.add_view(fileadmin.FileAdmin(path, '/files', name='Files'))

    # Start app
    app.run(debug=True)
