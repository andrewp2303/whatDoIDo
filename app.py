import os
import openai
from flask import Flask, redirect, render_template, request, url_for
from better_profanity import profanity

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():

    # function error checks for deleted posts
    def gen_response():
        situation = request.form["situation"]
        response = openai.Completion.create(
            model="curie:ft-personal-2022-10-01-20-47-19",
            prompt=generate_prompt(situation),
            max_tokens= 60,
            temperature=0.6,
            stop=[".", " END"]
        )
        if "[deleted]" in response.choices[0].text:
            gen_response()
        return redirect(url_for("index", result=response.choices[0].text))
    
    if request.method == "POST":
        return gen_response()


    end = '' if (str(request.args.get("result")))[-1] in ['?', '!'] else "."
    result = (str(request.args.get("result")))[6:] + end
    return render_template("index.html", result=result)


def generate_prompt(situation):
    return """{}. Give me really funny advice.""".format(
        situation.capitalize()
    )
