from flask import Flask, render_template, request

from app.model.flairmodel import FlairModel
from app.model.textblobmodel import TextBlobModel
from app.model.transformermodel import TransformerModel
from app.model.vadermodel import VaderModel
from app.enum.model import Model

app = Flask(__name__)

models = {
    Model.TB.value: TextBlobModel(),
    Model.V.value: VaderModel(),
    Model.F.value: FlairModel(),
    Model.T.value: TransformerModel()
}


class ModelResult:

    def __init__(self, model, sentiment):
        self.model = model
        self.sentiment = sentiment

    def to_json(self):
        return {
            "model": self.model,
            "sentiment": self.sentiment
        }


def analyze_sentiment_of_review_with_models(review: str):
    results = []
    for model_name, model in models.items():
        try:
            sentiment = model.analyze_sentiment_of_text(review)
            results.append(ModelResult(model_name, sentiment))
        except Exception as e:
            print(f"Error analyzing sentiment with model {model_name}: {e}")
            results.append(ModelResult(model_name, "Error"))
    return results


@app.route("/", methods=['POST', 'GET'])
def review_page():
    sentiments = []
    if request.method == 'POST':
        review = request.form['review']
        sentiments = analyze_sentiment_of_review_with_models(review)
    return render_template("index.html", sentiments=sentiments)


@app.route("/get_sentiment", methods=['GET'])
def get_sentiment():
    review = request.json['review']
    assert type(review) == str
    sentiments = analyze_sentiment_of_review_with_models(review)
    return list(map(lambda x: x.to_json(), sentiments))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
