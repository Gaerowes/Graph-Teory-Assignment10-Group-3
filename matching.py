
def hungarian_algorithm(cost_matrix):
    """
    Hungarian Algorithm for minimum-cost assignment.
    Supports rectangular matrices by padding them
    into square matrices.
    """

    rows = len(cost_matrix)

    if rows == 0:
        raise ValueError("Matrix cannot be empty.")

    cols = len(cost_matrix[0])

    if cols == 0:
        raise ValueError("Matrix cannot have empty rows.")

    if any(len(row) != cols for row in cost_matrix):
        raise ValueError("All rows must have the same length.")

    if any(not isinstance(value, (int, float)) or isinstance(value, bool)
           for row in cost_matrix for value in row):
        raise ValueError("Matrix must contain numeric costs.")

    if any(value < 0 for row in cost_matrix for value in row):
        raise ValueError("Costs must be non-negative.")

    # Pad rectangular matrix to square matrix
    size = max(rows, cols)
    max_cost = max(max(row) for row in cost_matrix)
    padding_cost = (max_cost + 1) * (size + 1)

    cost = [
        [padding_cost] * size for _ in range(size)
    ]

    for i in range(rows):
        for j in range(cols):
            cost[i][j] = cost_matrix[i][j]

    # Hungarian Algorithm (minimum cost)
    u = [0] * (size + 1)
    v = [0] * (size + 1)
    p = [0] * (size + 1)
    way = [0] * (size + 1)

    for i in range(1, size + 1):
        p[0] = i
        j0 = 0
        minv = [float("inf")] * (size + 1)
        used = [False] * (size + 1)

        while True:
            used[j0] = True
            i0 = p[j0]
            delta = float("inf")
            j1 = 0

            for j in range(1, size + 1):
                if not used[j]:
                    current = cost[i0 - 1][j - 1] - u[i0] - v[j]

                    if current < minv[j]:
                        minv[j] = current
                        way[j] = j0

                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j

            for j in range(size + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta

            j0 = j1

            if p[j0] == 0:
                break

        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1

            if j0 == 0:
                break

    # Extract assignments, excluding dummy rows/columns
    assignments = []

    for j in range(1, size + 1):
        i = p[j]

        if 1 <= i <= rows and j <= cols:
            assignments.append((i, j, cost_matrix[i - 1][j - 1]))

    assignments.sort(key=lambda x: x[0])

    total_cost = sum(item[2] for item in assignments)

    return assignments, total_cost


def display_result(matrix, case_number):
    print(f"\nTEST CASE {case_number}")
    print("=" * 40)

    print("Cost Matrix:")

    for row in matrix:
        print(row)

    assignments, total_cost = hungarian_algorithm(matrix)

    print("\nOptimal Assignments:")

    for worker, task, cost in assignments:
        print(f"Worker {worker} -> Task {task} | Cost: {cost}")

    print(f"\nTotal Minimum Cost: {total_cost}")

    print(f"Number of Assignments: {len(assignments)}")


def main():
    test_cases = [
        # Test Case 1: 3 x 3
        [
            [10, 20, 30],
            [20, 10, 15],
            [15, 25, 10]
        ],

        # Test Case 2: 4 x 4
        [
            [90, 75, 75, 80],
            [35, 85, 55, 65],
            [125, 95, 90, 105],
            [45, 110, 95, 115]
        ],

        # Test Case 3: 3 x 4
        [
            [8, 6, 10, 9],
            [9, 12, 7, 11],
            [14, 9, 16, 5]
        ],

        # Test Case 4: 5 x 3
        [
            [12, 7, 9],
            [8, 11, 6],
            [10, 5, 13],
            [9, 8, 7],
            [6, 10, 11]
        ]
    ]

    for i, matrix in enumerate(test_cases, start=1):
        display_result(matrix, i)


if __name__ == "__main__":
    main()
