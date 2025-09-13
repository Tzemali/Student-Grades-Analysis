import math as MerosA

def calculate_statistics(X, Y):
    """
    Βασικά στατιστικά για δύο λίστες X και Y.
    X: Λίστα αριθμών για τη μεταβλητή Χ
    Y: Λίστα αριθμών για τη μεταβλητή Y
    return: Λεξικό με τα στατιστικά και τη συνδιακύμανση
    """
    # Έλεγχουμε το ίσο μέγεθος λιστών
    if len(X) != len(Y):
        raise ValueError("List X and Y must be the same size")
    n = len(X)

    # Υπολογίζουμε βασικών στατιστικών για X
    mean_X = sum(X) / n
    variance_X = sum((x - mean_X) ** 2 for x in X) / (n - 1)
    std_X = MerosA.sqrt(variance_X)

    # Υπολογίζουμε βασικών στατιστικών για Y
    mean_Y = sum(Y) / n
    variance_Y = sum((y - mean_Y) ** 2 for y in Y) / (n - 1)
    std_Y = MerosA.sqrt(variance_Y)

    # Υπολογίζουμε δειγματικής συνδιακύμανσης
    covariance = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n)) / n

    # Δημιουργούμε λεξικού αποτελεσμάτων
    results = {
        "basic_statistics_X": {
            "mean": mean_X,
            "variance": variance_X,
            "std": std_X
        },
        "basic_statistics_Y": {
            "mean": mean_Y,
            "variance": variance_Y,
            "std": std_Y
        },
        "covariance_X_Y": covariance
    }

    return results

# Παράδειγμα λειτουργίας
if __name__ == "__main__":
    try:
        X = [1, 2, 3, 4, 5]
        Y = [2, 4, 6, 8, 10]
        print("Result:", calculate_statistics(X, Y))
    except ValueError as e:
        print("error:", e)
