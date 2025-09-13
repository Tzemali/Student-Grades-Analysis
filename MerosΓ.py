def list_operations(A, B):
    """
    Υπολογίζουμε το άθροισμα και το γινόμενο δύο λιστών στοιχείο προς στοιχείο, μαζί με τα μεγέθη τους.
    A: Λίστα αριθμών
    B: Λίστα αριθμών
    return: Λεξικό με το αποτέλεσμα των πράξεων
    """
    # Έλεγχουμε για ίσο μέγεθος λιστών
    if len(A) != len(B):
        return {
            "sum_of_lists": False,
            "prod_of_lists": False,
            "length_of_list_A": len(A),
            "length_of_list_B": len(B)
        }

    # Υπολογιζουμε Λίστα Χ και Λίστα Υ
    sum_of_lists = [A[i] + B[i] for i in range(len(A))]
    prod_of_lists = [(A[i] * B[i]) ** 2 for i in range(len(A))]

    # Δημιουργούμε λεξικού αποτελεσμάτων
    results = {
        "sum_of_lists": sum_of_lists,
        "prod_of_lists": prod_of_lists,
        "length_of_list_A": len(A),
        "length_of_list_B": len(B)
    }

    return results

# Παράδειγμα λειτουργίας
if __name__ == "__main__":
    # Περίπτωση 1
    A1 = [2, 2, 2, 2, 2, 2]
    B1 = [3, 3, 3, 3, 3, 3]
    print("Result of case 1", list_operations(A1, B1))

    # Περίπτωση 2
    A2 = [2, 2, 2, 2, 2, 2]
    B2 = [3, 3]
    print("Result of case 2", list_operations(A2, B2))
