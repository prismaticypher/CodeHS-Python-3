# fill in this function to return the total of the three judges' scores!
def calculate_score(judge_scores):
    valid_scores = all(0 <= score <= 10 for score in judge_scores)

    if not valid_scores:
        return "Invalid scores. Scores should be between 0 and 10."

    total_score = sum(judge_scores)

    return total_score