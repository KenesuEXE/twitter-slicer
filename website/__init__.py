from flask import Flask, render_template, request
from . import twitter_slicer as ts

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["POST", "GET"])
    def home():
        if request.method == "POST":
            text = request.form.get("text")
            slice_mode = request.form.get("slice_mode")
            with_counter = True if request.form.get("with_counter") else False
            separator = request.form.get("separator")
    
            text_list = ts.SliceMode.indicated(text, separator)
            if slice_mode == "limit":
                tweets = ts.SliceMode(text_list, with_counter).limit()
            if slice_mode == "space":
                tweets = ts.SliceMode(text_list, with_counter).space()
            if slice_mode == "punct":
                tweets = ts.SliceMode(text_list, with_counter).punct()
        else:
            tweets = None

        return render_template("index.html", tweets=tweets)

    return app

