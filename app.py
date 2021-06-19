import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient


def create_app():
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://user_1:Krishna778@microblog-application.hitm7.mongodb.net/test")
    app.db = client.microblog
    entries = []

    @app.route("/", methods=["GET", "POST"])
    def home():
        print([e for e in app.db.entry.find({})])
        if request.method == "POST":
            entry_form = request.form.get("content")
            formatted_data = datetime.datetime.today().strftime("%Y-%m-%d")
            entries.append((entry_form, formatted_data))
            app.db.entry.insert({"content": entry_form, "date": formatted_data})
        return render_template("home.html", entries=entries)

    return app
