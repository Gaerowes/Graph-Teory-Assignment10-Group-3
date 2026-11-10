
def hungarian_algorithm(cost_matrix):
    rows = len(cost_matrix)
    cols = len(cost_matrix[0])

    # Convert rectangular matrix into square matrix
    size = max(rows, cols)
    max_cost = max(max(row) for row in cost_matrix)
    padding_cost = (max_cost + 1) * (size + 1)

    cost = [[padding_cost] * size for _ in range(size)]

    for i in range(rows):
        for j in range(cols):
            cost[i][j] = cost_matrix[i][j]

    # Hungarian Algorithm
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
                    current = cost[i0-1][j-1] - u[i0] - v[j]

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

    assignments = []

    for j in range(1, size + 1):
        i = p[j]

        if 1 <= i <= rows and j <= cols:
            assignments.append(
                (i, j, cost_matrix[i-1][j-1])
            )

    assignments.sort(key=lambda x: x[0])

    total_cost = sum(item[2] for item in assignments)

    return assignments, total_cost


def get_matrix_input():
    print("=" * 45)
    print("       DYNAMIC MATRIX MATCHING")
    print("          HUNGARIAN ALGORITHM")
    print("=" * 45)

    while True:
        try:
            rows = int(input("\nEnter number of workers: "))
            cols = int(input("Enter number of tasks: "))

            if rows <= 0 or cols <= 0:
                print("Both dimensions must be positive.")
                continue

            break

        except ValueError:
            print("Please enter valid integers.")

    matrix = []

    print("\nEnter the cost matrix.")
    print(f"Input {cols} numbers for each of the {rows} rows.")
    print("Separate values using spaces.\n")

    for i in range(rows):
        while True:
            try:
                values = list(map(int, input(f"Worker {i+1}: ").split()))

                if len(values) != cols:
                    print(f"Please enter exactly {cols} values.")
                    continue

                if any(value < 0 for value in values):
                    print("Costs cannot be negative.")
                    continue

                matrix.append(values)
                break

            except ValueError:
                print("Please enter integers only.")

    return matrix


def display_result(matrix):
    assignments, total_cost = hungarian_algorithm(matrix)

    print("\n" + "=" * 45)
    print("             COST MATRIX")
    print("=" * 45)

    for row in matrix:
        print(" ".join(f"{value:6}" for value in row))

    print("\n" + "=" * 45)
    print("          OPTIMAL ASSIGNMENT")
    print("=" * 45)

    for worker, task, cost in assignments:
        print(
            f"Worker {worker} -> Task {task} "
            f"| Cost: {cost}"
        )

    print("-" * 45)
    print(f"Total Minimum Cost: {total_cost}")
    print(f"Total Assignments: {len(assignments)}")
    print("=" * 45)


def main():
    while True:
        matrix = get_matrix_input()
        display_result(matrix)

        again = input("\nRun another test case? (y/n): ").lower()

        if again != "y":
            print("\nProgram terminated.")
            break


if __name__ == "__main__":
    main()
