from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def first_flask():
    return "This is my first webpage ! "

app.run()

@app.route("/page_2")
def second_flask():
    return "Python is fun !"

app.run(debug=True)






