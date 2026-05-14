"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Sophia Phung
Student ID:   132046561

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    
    explanation = """
    1A: A single shortest-path run from S is not enough as it does not tell you what vertices or edges that could be on the shortest-path to a given destination T. It cannot make the decision to know whether a node or edge fall in the shortest path from S to destination T.
    1B: The structural decision that remains after all inter-location costs are known is: what structure should be used to optimally organize and connect the locations to fufill our overall objective?
    1C: This problem requires a search over orders as the number of different paths that one can take to complete the objective grows combinatorially, and shortest path computations alone do not determine the optimal global arrangement.
    """
    return explanation


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):

    sources = set(relics)
    sources.add(spawn)
    sources.add(exit_node)

    return list(sources)


def run_dijkstra(graph, source):

    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    queue = [(0, source)]

    while queue:
        cost, node = heapq.heappop(queue)
        if cost > dist[node]:
            continue
        for neighbor, edge_cost in graph[node]:
            new_cost = cost + edge_cost
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))

    return dist


def precompute_distances(graph, spawn, relics, exit_node):
    
    sources = select_sources(spawn, relics, exit_node)
    dist_table = {}

    for source in sources:
        dist_table[source] = run_dijkstra(graph, source)

    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    answers = """
    3A: For nodes already finalized (in S):
        For nodes already finalized, the invariant describes that once it is added to S, its distance value is guaranteed to be the shortest possible path from the source x.
        
        For nodes not yet finalized (not in S):**
        For nodes not yet finalized, the invariant describes that the current distance is the best path found so far only using finalized nodes, yet will still continue to update if a shorter path is to be found when more nodes are processed.
    
    3B: Initialization : why the invariant holds before iteration 1:
        The source node starts with distance 0 since the cost to travel to the source node from itself is 0, and all other distance are infinity as no other paths have been discovered yet.
        
        Maintenance : why finalizing the min-dist node is always correct:
        Finalizing the min-dist node is always correct because all edge weights are nonnegative, so the smallest unfinalized distance could not possibly get any smaller under another run. 
        Relaxing outgoing edges continues to update the neighboring nodes' shortest distance paths therefore maintaining that min-dist will always be finalized.

        Termination : what the invariant guarantees when the algorithm ends:
        The invariant guarantees that all shortest-paths to each node from the source node will be found and finalized when the algorithm ends.
    
    3C: This matters for the route planner as in order to make the optimal routing decisions, it is necessary to have the finalized shortest paths from each relevant pair node to then find the shortest path from start node S to destination T.
    """
    return answers


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    answers = """
    The failure mode: A route fails when a shorter distance (more optimal) route is found.
    Counter-example setup: Given this table as my counter-example map,
        | From \ To | B   | C   | D   | T   |
        |-----------|-----|-----|-----|-----|
        | S         | 1   | 2   | 2   | --  |
        | B         | --  | 1   | 100 | 1   |
        | C         | 1   | --  | 100 | 100 |
        | D         | 100 | 1   | --  | 100 |
    What greedy picks: Greedy chooses S -> B -> C -> D -> T, however, the cost of this path is:
        1 + 1 + 100 + 100 = 202
    What optimal picks: The optimal route chooses S -> D -> C -> B -> T, with cost:
        2 + 1 + 1 + 1 = 5
    Why greedy loses: Greedy chooses the cheapest next step locally, but that choice can force expensive later steps, so the final route may not be optimal.

    The algorithm must explore different orders of visiting the required nodes because the total route cost depends on the sequence in which the nodes are traversed.
    """
    return answers


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
