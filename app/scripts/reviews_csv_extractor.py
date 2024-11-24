import pandas as pd

from app.main import analyze_sentiment_of_review_with_models
from app.enum.model import Model

DATA_PATH = "../data/IMDB-movie-reviews.csv"
OUTPUT_PATH = "../data/evaluated_reviews.csv"
MODEL_FIELDS = [e.value for e in Model]


def extract_reviews(path=DATA_PATH):
    extracted_reviews = pd.read_csv(path, encoding='ISO-8859-1', on_bad_lines='warn', sep=';')
    return extracted_reviews


def eval_reviews(reviews_df):
    """function that evaluates the sentiment of the reviews with all the models and returns a dataframe with this
    additional information"""
    evaluated_reviews_df = pd.DataFrame(columns=['review', 'sentiment'] + MODEL_FIELDS)
    for index, row in reviews_df.iterrows():
        # analyze the sentiment of the review with all the models
        model_analysis = analyze_sentiment_of_review_with_models(row['review'])
        to_write = {'review': row['review'], 'sentiment': row['sentiment']}
        for model in model_analysis:
            to_write[model.model] = model.sentiment
        to_write_df = pd.DataFrame([to_write])
        evaluated_reviews_df = pd.concat([evaluated_reviews_df, to_write_df], ignore_index=True)
    return evaluated_reviews_df


if __name__ == '__main__':
    reviews = extract_reviews()
    evaluated_reviews_dtf = eval_reviews(reviews)
    evaluated_reviews_dtf.to_csv(OUTPUT_PATH, index=False, sep=';')
