from flask import Flask, render_template, request
from app.model.textblobmodel import TextBlobModel

app = Flask(__name__)

models = {
    "textblob": TextBlobModel(),
    # "vader" : VaderModel(),
    # "flair" : FlairModel(),
    # "transformer" : TransformerModel()
}


def analyze_sentiment_with_models(review: str):
    results = []
    for key, model in models.items():
        sentiment = model.analyze_sentiment(review)
        results.append((key, sentiment))
    return results


@app.route("/", methods=['POST', 'GET'])
def review_page():
    sentiments = []
    if request.method == 'POST':
        review = request.form['review']
        sentiments = analyze_sentiment_with_models(review)
    return render_template("index.html", sentiments=sentiments)


@app.route("get_sentiment", methods=['GET'])
def get_sentiment():
    review = request.json['review']
    sentiments = analyze_sentiment_with_models(review)
    return {"sentiments": sentiments}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
