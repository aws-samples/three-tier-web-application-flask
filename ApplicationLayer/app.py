from flask import Flask, make_response, request, jsonify, after_this_request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from parameters import master_username, db_password, endpoint, db_instance_name
import requests, json
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{master_username}:{db_password}@{endpoint}/{db_instance_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class TodoTable(db.Model):
    __tablename__ = "todotable"
 
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))
 
    def __init__(self, task):
        self.task = task
 
    def __repr__(self):
        return f"{self.id}:{self.task}"

with app.app_context():
    db.create_all()

def create_object(results):
    return {result.id: result.task for result in results}

@app.route('/', methods=['GET'])
def display():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    todos = TodoTable.query.all()
    return jsonify(create_object(todos))

@app.route("/create", methods =['POST'])
def create():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    try:
        if request.method == "POST":
            todo = TodoTable(task=request.form.get("task"))
            db.session.add(todo)
            db.session.commit()

            return redirect("/", 302)
    except:
        return redirect("/", 404)

@app.route("/update", methods =['POST'])
def update():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    try:
        if request.method == "POST":
            todo = TodoTable.query.get(request.form.get("task_id"))
            todo.task = request.form.get("task")

            db.session.commit()
            return redirect("/", 302)
    except:
        return redirect("/", 404)

@app.route("/complete/<task_id>", methods=["POST"])
def complete(task_id):
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    try:
        todo = TodoTable.query.get(task_id)
        db.session.delete(todo)
        db.session.commit()
        
        return redirect("/", 302)
    except:
        return redirect("/", 404)
    

@app.route('/health')
def index():
    return make_response("Successful health check for ALB!", 200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=False)