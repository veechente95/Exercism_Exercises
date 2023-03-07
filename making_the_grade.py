"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    """Round all provided student scores."""
    rounded_score = []
    while student_scores:
        rounded_score.append(round(student_scores.pop()))
    return rounded_score


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided."""
    failed = 0
    for score in student_scores:
        if score <= 40:
            failed += 1
    return failed


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold."""
    top_students = []
    for score in student_scores:
        if score >= threshold:
            top_students.append(score)
    return top_students

    
def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade."""
    grades = []
    increment = round((highest - 40)/4)
    for scores in range(41,highest,increment):
        grades.append(scores)
    return grades
    

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order."""
    ranking = []
    for i in range(len(student_scores)):
        ranking.append(f"{i + 1}. {student_names[i]}: {student_scores[i]}")
    return ranking
    

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    pass
