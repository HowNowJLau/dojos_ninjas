from flask import Flask, render_template, request, redirect
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo
from flask_app import app

@app.route('/ninjas')
def new_ninja():
    all_dojos = Dojo.get_all()
    return render_template('new_ninja.html', all_dojos=all_dojos)

@app.route('/ninjas/create', methods=["POST"])
def create_ninja():
    Ninja.create(request.form)
    return redirect('/')
