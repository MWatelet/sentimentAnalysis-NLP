import matplotlib.pyplot as plt

from app.enum.model import Model
from app.scripts.reviews_csv_extractor import extract_reviews, OUTPUT_PATH

MODEL_FIELDS = [e.value for e in Model]


def compile_models_scores(reviews_evaluated):
    """function that compiles the scores of the models and the misses of the models in a dictionary"""
    scores = {name: 0 for name in MODEL_FIELDS}
    misses = {name: 0 for name in MODEL_FIELDS}
    for index, row in reviews_evaluated.iterrows():
        for model in MODEL_FIELDS:
            if row[model] == row['sentiment']:
                scores[model] += 1
            else:
                misses[model] += 1
    return scores, misses


def bar_plot(data: dict, title: str, y_label: str, x_label='Models'):
    """function that creates a bar plot with the data provided and save it in the data/chart folder"""
    names = list(data.keys())
    values = list(data.values())
    plt.bar(names, values, color='blue', width=0.4)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(f'../static/{title}.png')


if __name__ == '__main__':
    reviews_evaluated_dataframe = extract_reviews(OUTPUT_PATH)
    models_scores, models_misses = compile_models_scores(reviews_evaluated_dataframe)
    bar_plot(models_scores, 'Models_successes', 'Successes')
    plt.clf()
    bar_plot(models_misses, 'Models_misses', 'Misses')
