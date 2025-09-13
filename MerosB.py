def matrix_prod(A, B):
    """
    Υπολογίζουμε το γινόμενο δύο πινάκων A και B.
    A: Δισδιάστατη λίστα αριθμών (πίνακας A)
    B: Δισδιάστατη λίστα αριθμών (πίνακας B)
    return: Δισδιάστατη λίστα αριθμών (πίνακας γινόμενο A * B)
    """
    # Έλεγχουμε διαστάσεων για τον πολλαπλασιασμό πινάκων
    try:
        if len(A[0]) != len(B):
            raise ValueError("The number of columns in A must be equal to the number of rows in B")

        # Υπολογίζουμε το γινόμενω πινάκων
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                element = sum(A[i][k] * B[k][j] for k in range(len(B)))
                row.append(element)
            result.append(row)
        return result
    except ValueError as e:
        print("error", e)
        return None

# Παράδειγμα λειτουργίας
if __name__ == "__main__":
    A = [
        [2, 1, 3],
        [3, 9, 4],
        [5, 10, 7]
    ]
    B = [
        [3, 4],
        [2, 1],
        [5, 6]
    ]

    result = matrix_prod(A, B)
    if result:
        print("The result of the product is")
        for row in result:
            print(row)
