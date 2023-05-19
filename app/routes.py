from app import app
from flask import render_template, request
from app.models import User, CPU

@app.route('/', methods =["GET", "POST"])
def index():

    if request.method == "POST":
        name = request.form['fname']
        info = CPU.query.filter(CPU.name == name)
        return render_template('cpu_info.html', title=f"CPU {name}", info=info)

    cpus = CPU.query.all()
    return render_template('index.html', title='CPU', cpus=cpus)