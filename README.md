# Graph-Theory-Assignment11-Group-3

Implementation of Graph Coloring and Graph Matching Algorithms for the Graph Theory course at Institut Teknologi Sepuluh Nopember (ITS).

---

## 1. Identity

**Informatics ITS Graph Theory Class - Group 3**

| Name | Student ID |
|---|---|
| Padhang Abiyu Fikri | 5025251014 |
| Dzulfiqar Rafi'ussunnah | 5025251011 |
| Aditya Lingga Mardika | 5025251158 |
| Muhammad Faris Alfarrel | 5025251002 |

---

## 2. Short Explanation About Algorithms

This project implements two applications of graph theory: Graph Coloring and Graph Matching.

### 2.1 Graph Coloring - Sudoku Solver

Graph Coloring is the problem of assigning colors to the vertices of a graph so that no two adjacent vertices have the same color.

In this project, the Graph Coloring concept is applied to solve a Sudoku puzzle.

The Sudoku puzzle is represented as a graph with the following properties:

- Each cell in the Sudoku grid represents a vertex.
- Two vertices are adjacent if their corresponding cells belong to the same row, column, or 3×3 subgrid.
- The numbers from 1 to 9 represent the available colors.
- Adjacent vertices must have different colors.

The Sudoku Solver uses the **Backtracking Algorithm** to find a valid coloring of the graph.

The algorithm works by assigning a valid number to an empty cell and checking whether the assignment satisfies all Sudoku constraints. If the assignment causes a conflict, the algorithm backtracks and tries another number.

The process continues until all cells are successfully filled or no valid solution can be found.

### 2.2 Graph Matching - Dynamic Matrix Matching

Graph Matching is a problem of finding a set of edges in a graph where no two selected edges share the same vertex.

This project applies the matching concept to an assignment problem represented using a matrix with dynamic dimensions.

The matrix represents the relationship between two sets of vertices:

- Rows represent the first set of vertices.
- Columns represent the second set of vertices.
- Each matrix entry represents a possible connection or assignment between the two sets.

The implementation supports different test cases and dynamic matrix sizes rather than relying on a fixed matrix dimension.

The matching algorithm searches for valid assignments while ensuring that each vertex is matched at most once.

The objective is to find an optimal or maximum matching depending on the problem formulation.

---

## 3. Prerequisites to Run the Code

The following software and tools are required to run the implementations:

- Python 3.x
- Required libraries or dependencies (if any).
- Git (optional, for cloning the repository).

### Dependencies

The implementation uses Python libraries for graph processing and algorithm execution.

List any additional dependencies here if required by the implementation.

---

## 4. Instructions to Run the Code

### 4.1 Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Gaerowes/Graph-Theory-Assignment11-Group-3.git
```

Navigate to the project directory:

```bash
cd Graph-Theory-Assignment11-Group-3
```

### 4.2 Prepare the Input

Prepare the input files according to the format required by each implementation.

#### Sudoku Solver Input

The input consists of a 9×9 Sudoku grid.

Use `0` to represent an empty cell.

Example:

```text
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

### 4.3 Run the Graph Coloring Algorithm

Run the Sudoku Solver implementation:

```bash
python sudoku_solver.py
```

### 4.4 Run the Graph Matching Algorithm

Run the Dynamic Matrix Matching implementation:

```bash
python matching.py
```

---

## 5. Input for Sample Run

This section provides sample inputs used to demonstrate the execution of both algorithms.

### 5.1 Sudoku Solver

**Sample Input:**

```text
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

**Expected Result:**

```text
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

### 5.2 Dynamic Matrix Matching

**Sample Input:**

```text
Enter number of workers: 4
Enter number of tasks: 4

Enter the cost matrix.
Input 4 numbers for each of the 4 rows.
Separate values using spaces.

Worker 1: 90 75 75 80
Worker 2: 35 85 55 60
Worker 3: 125 95 90 105
Worker 4: 45 110 95 115
```

**Expected Result:**

```text
The program displays the matching assignments
and the resulting matching value.
```

---

## 6. Result of Sample Run

This section presents the execution results of the implemented algorithms.

### 6.1 Graph Coloring - Sudoku Solver

**Sample Output:**

```text
Sudoku solved successfully!

5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

**Execution Screenshot:**

<img width="559" height="403" alt="image" src="https://github.com/user-attachments/assets/cbf64568-51be-45af-a3fa-3f21ea99ebb5" />


### 6.2 Graph Matching - Dynamic Matrix Matching

**Sample Output:**

```text
Matching results:

Worker 1: 90 75 75 80
Worker 2: 35 85 55 60
Worker 3: 125 95 90 105
Worker 4: 45 110 95 115

=============================================
             COST MATRIX
=============================================
    90     75     75     80
    35     85     55     60
   125     95     90    105
    45    110     95    115

=============================================
          OPTIMAL ASSIGNMENT
=============================================
Worker 1 -> Task 2 | Cost: 75
Worker 2 -> Task 4 | Cost: 60
Worker 3 -> Task 3 | Cost: 90
Worker 4 -> Task 1 | Cost: 45
---------------------------------------------
Total Minimum Cost: 270
Total Assignments: 4
=============================================
```

**Execution Screenshot:**

<img width="422" height="690" alt="image" src="https://github.com/user-attachments/assets/7e660d12-9b0b-4e1f-9559-90cb30c8d2d8" />


---

## 7. AI Tools Usage Disclosure

AI tools were used as an assistance tool during the development and documentation process.

The use of AI included:

- Assisting with the understanding of Graph Coloring and Graph Matching concepts.
- Supporting the understanding of the Backtracking Algorithm.
- Assisting with the preparation and improvement of README documentation.

All implementations, algorithm explanations, and execution results were reviewed and verified by the group members.

---

## 8. Conclusion

This project demonstrates the application of Graph Coloring and Graph Matching in solving computational problems.

The Sudoku Solver applies Graph Coloring concepts using the Backtracking Algorithm to assign valid numbers to Sudoku cells while satisfying the constraints of rows, columns, and subgrids.

Meanwhile, the Dynamic Matrix Matching implementation demonstrates how graph matching can be applied to assignment problems with different test cases and matrix dimensions.

Through these implementations, the project provides an opportunity to understand graph theory concepts and their applications in algorithmic problem-solving.
