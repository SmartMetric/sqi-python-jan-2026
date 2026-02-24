def read_scores(filename):
    cleaned_scores = []

    with open(filename, "r") as f:
        scores = f.readlines()
    for score in scores:
        cleaned_score = score.strip()
        cleaned_scores.append(score.strip())
        name, age = cleaned_score.split(",")
    return cleaned_scores
