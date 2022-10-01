import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        situation = request.form["animal"]
        response = openai.Completion.create(
            model="curie:ft-personal-2022-10-01-19-15-56",
            prompt=generate_prompt(situation),
            max_tokens= 60,
            temperature=0.6,
            stop="."
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = str(request.args.get("result")) + "."
    return render_template("index.html", result=result)


def generate_prompt(situation):
    return """{}. Give me really funny advice.""".format(
        situation.capitalize()
    )
