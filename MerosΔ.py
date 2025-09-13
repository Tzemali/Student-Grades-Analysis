import math

def calculate_averages(students_scores):
    """
    Υπολογίζουμε τον μέσο όρο για κάθε μάθημα.
    students_scores: Λίστα πλειάδων (όνομα ,μαθηματικά, φυσική, αγγλικά)
    return: Λεξικό με τους μέσους όρους για κάθε μάθημα
    """
    math_scores = [score[1] for score in students_scores]
    physics_scores = [score[2] for score in students_scores]
    english_scores = [score[3] for score in students_scores]

    averages = {
        "Math": sum(math_scores) / len(math_scores),
        "Physics": sum(physics_scores) / len(physics_scores),
        "English": sum(english_scores) / len(english_scores)
    }

    return averages

def top_students(students_scores):
    """
    Βρίσκουμε τον καλύτερο μαθητή σε κάθε μάθημα.
    students_scores: Λίστα πλειάδων (όνομα ,μαθηματικά, φυσική, αγγλικά)
    return: Λεξικό με τον καλύτερο μαθητή για κάθε μάθημα
    """
    top_math = max(students_scores, key=lambda x: x[1])[0]
    top_physics = max(students_scores, key=lambda x: x[2])[0]
    top_english = max(students_scores, key=lambda x: x[3])[0]

    top_students_dict = {
        "Math": top_math,
        "Physics": top_physics,
        "English": top_english
    }

    return top_students_dict

def students_above_threshold(students_scores, threshold):
    """
    Υπολογίζειζουμε τον αριθμό των μαθητών που έχουν βαθμό πάνω από το όριο σε όλα τα μαθήματα.
    students_scores: Λίστα πλειάδων (όνομα, μαθηματικά, φυσική, αγγλικά)
    threshold: Όριο βαθμολογίας
    return: Αριθμός μαθητών
    """
    count = sum(
        all(score > threshold for score in student[1:]) for student in students_scores
    )

    return count

def unique_scores(students_scores):
    """
    Επιστρέφει ένα σύνολο με όλους τους μοναδικούς βαθμούς στα μαθήματα.
    students_scores: Λίστα πλειάδων (όνομα, μαθηματικά, φυσική, αγγλικά)
    return: Σύνολο μοναδικών βαθμών
    """
    scores = {score for student in students_scores for score in student[1:]}

    return scores

def calculate_std_deviation(students_scores):
    """
    Υπολογίζει την τυπική απόκλιση των βαθμών για κάθε μάθημα.
    Λίστα πλειάδων (όνομα, μαθηματικά, φυσική, αγγλικά)
    return: Λεξικό με τις τυπικές αποκλίσεις για κάθε μάθημα
    """
    def std_dev(scores):
        mean = sum(scores) / len(scores)
        variance = sum((x - mean) ** 2 for x in scores) / len(scores)
        return math.sqrt(variance)

    math_scores = [score[1] for score in students_scores]
    physics_scores = [score[2] for score in students_scores]
    english_scores = [score[3] for score in students_scores]

    std_deviation = {
        "Math": std_dev(math_scores),
        "Physics": std_dev(physics_scores),
        "English": std_dev(english_scores)
    }

    return std_deviation

# Παράδειγμα λειτουργίας
if __name__ == "__main__":
    students_scores = [
        ("Alice", 85, 90, 82),
        ("Bob", 78, 76, 88),
        ("Charlie", 92, 89, 95),
        ("David", 70, 72, 68),
        ("Eve", 88, 92, 91)
    ]

    print(calculate_averages(students_scores))
    print(top_students(students_scores))
    print(students_above_threshold(students_scores, 80))
    print(unique_scores(students_scores))
    print(calculate_std_deviation(students_scores))
