from flask import Flask, render_template, request, jsonify
import json
import analyzer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        analysis = analyzer.analyze_text(text)
        return jsonify(analysis)
    return render_template("index.html")

@app.route("/correct", methods=["POST"])
def correct():
    modified_json = request.json
    corrected_json = analyzer.correct(modified_json)
    return jsonify(corrected_json)

if __name__ == "__main__":
    app.run(debug=True)