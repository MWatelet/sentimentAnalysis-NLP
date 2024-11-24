from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def hello_world():
    sentiment = "haha"
    if request.method == 'POST':
        review = request.form['review']
    return render_template("index.html", sentiment=sentiment)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
