# -*- coding: utf-8 -*-

from flask import render_template, request, Flask, flash, redirect, url_for, session

import db_connect as db

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		new_word = request.form["id"]
		db.add_words(new_word)
		words = [new_word]
		words += db.get_words(4)
	else:
		words = db.get_words(5)
	return render_template("index.html", words=words)

if __name__ == "__main__":
	app.run()
