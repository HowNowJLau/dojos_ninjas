from flask import Flask, render_template, request, redirect
from flask_app.models.dojo_model import Dojo
from flask_app import app

@app.route('/')
def index():
    return redirect('dojos')

@app.route('/dojos')
def dojo_home():
    all_dojos = Dojo.get_all()
    return render_template("all_dojos.html", all_dojos=all_dojos)

@app.route('/dojos/<int:id>')
def view_dojo(id):
    one_dojo = Dojo.get_one({'id':id})
    print(one_dojo)
    return render_template("one_dojo.html", one_dojo=one_dojo)
    
@app.route('/dojos/create', methods=["POST"])
def create_dojo():
    id = Dojo.create(request.form)
    return redirect(f'/dojos/{id}')