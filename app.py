# -*- coding: utf-8 -*-

from flask import render_template, request, Flask, flash, redirect, url_for, session
import sys
import db_connect as db

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		new_word = request.form["word"].encode('utf-8')
		words = [new_word]
		for word in db.get_words(4):
			words.append(word[0])
		db.add_words(new_word)
	else:
		words = []
		for word in db.get_words(5):
			words.append(word[0])
	return render_template("index.html", words=words)

if __name__ == "__main__":
	app.run()
