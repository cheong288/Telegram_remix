from flask import Flask, request, render_template
import os
import sqlite3
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    return (render_template("main.html"))

@app.route("/index", methods=["GET", "POST"])
def index():
    return (render_template("index.html"))

@app.route("/paynow", methods=["GET", "POST"])
def paynow():
    return (render_template("paynow.html"))

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    q = request.form.get("q")
    if not q:
      return render_template("add_user.html", error="Name cannot be empty.")

    t = datetime.datetime.now()
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("insert into users(name,timestamp) values(?,?)",(q,t))
    conn.commit()
    c.close()
    conn.close()
    return render_template("add_user.html", error=None)

@app.route("/user_log", methods=["GET", "POST"])
def user_log():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("select * from users")
    rows = c.fetchall()
    c.close()
    conn.close()
    return (render_template("user_log.html",rows=rows))

@app.route("/delete_log", methods=["GET", "POST"])
def delete_log():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("delete from users")
    conn.commit()
    c.close()
    conn.close()
    return (render_template("delete_log.html"))

if __name__ == '__main__':
    app.run()