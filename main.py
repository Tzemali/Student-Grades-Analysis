from MerosA import calculate_statistics
from MerosB import matrix_prod
from MerosΓ import list_operations
from MerosΔ import (calculate_averages, top_students, students_above_threshold, unique_scores, calculate_std_deviation)

if __name__ == "__main__":
    # MerosA
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 6, 8, 10]
    print(calculate_statistics(X, Y))

    # MerosB
    A = [[2, 1, 3], [3, 9, 4], [5, 10, 7]]
    B = [[3, 4], [2, 1], [5, 6]]
    print(matrix_prod(A, B))

    # MerosΓ
    A1 = [2, 2, 2, 2, 2, 2]
    B1 = [3, 3, 3, 3, 3, 3]
    print(list_operations(A1, B1))

    # MerosΔ
    students_scores = [
        ("Alice", 85, 90, 82),
        ("Bob", 78, 76, 88),
        ("Charlie", 92, 89, 95),
        ("David", 70, 72, 68),
        ("Eve", 88, 92, 91),
    ]
    print(calculate_averages(students_scores))
    print(top_students(students_scores))
    print(students_above_threshold(students_scores, 80))
    print(unique_scores(students_scores))
    print(calculate_std_deviation(students_scores))
