from flask import Flask, render_template

app = Flask("__main__")


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>/")
def api(word):
    definition = word.upper()
    translator_output = {"word": word,
                         "definition": definition}
    return translator_output


app.run(debug=True)