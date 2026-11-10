

import sys

DEFAULT_INPUT = "input.txt"

N = 9
BOX = 3
COLORS = range(1, N + 1)


def build_graph():
    """Build adjacency list: vertex id = row * 9 + col."""
    adj = [set() for _ in range(N * N)]
    for r in range(N):
        for c in range(N):
            v = r * N + c
            for k in range(N):
                if k != c:
                    adj[v].add(r * N + k)      # same row
                if k != r:
                    adj[v].add(k * N + c)      # same column
            br, bc = (r // BOX) * BOX, (c // BOX) * BOX
            for i in range(br, br + BOX):
                for j in range(bc, bc + BOX):
                    if (i, j) != (r, c):
                        adj[v].add(i * N + j)  # same 3x3 subgrid
    return adj


def parse_grid(text):
    nums = text.split()
    if len(nums) != N * N:
        raise ValueError(f"Input must contain {N * N} numbers, got {len(nums)}.")
    values = [int(x) for x in nums]
    if any(v < 0 or v > 9 for v in values):
        raise ValueError("Numbers must be between 0 and 9.")
    return values


def is_safe(adj, color, v, c):
    """A color c is safe for vertex v if no neighbor already has it."""
    return all(color[u] != c for u in adj[v])


def initial_is_valid(adj, color):
    """Check that the given clues do not already conflict."""
    for v in range(N * N):
        if color[v] != 0:
            for u in adj[v]:
                if color[u] == color[v]:
                    return False
    return True


def color_graph(adj, color):
    """Backtracking graph coloring with MRV (pick most constrained vertex)."""
    best_v, best_opts = -1, None
    for v in range(N * N):
        if color[v] == 0:
            opts = [c for c in COLORS if is_safe(adj, color, v, c)]
            if not opts:
                return False  # dead end
            if best_opts is None or len(opts) < len(best_opts):
                best_v, best_opts = v, opts
                if len(opts) == 1:
                    break

    if best_v == -1:
        return True  # all vertices colored

    for c in best_opts:
        color[best_v] = c
        if color_graph(adj, color):
            return True
        color[best_v] = 0  # backtrack
    return False


def print_grid(color):
    for r in range(N):
        print(" ".join(str(color[r * N + c]) for c in range(N)))


def main():
    try:
        path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
        with open(path) as f:
            color = parse_grid(f.read())
    except (OSError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

    adj = build_graph()

    print("Input puzzle:\n")
    print_grid(color)
    print()

    if not initial_is_valid(adj, color):
        print("Invalid puzzle: the given numbers already conflict.")
        sys.exit(1)

    if color_graph(adj, color):
        print("Sudoku solved successfully!\n")
        print_grid(color)
    else:
        print("No valid coloring exists. This Sudoku has no solution.")


if __name__ == "__main__":
    main()