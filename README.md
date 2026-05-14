# The Torchbearer

**Student Name:** Sophia Phung
**Student ID:** 132046561
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis


- **Why a single shortest-path run from S is not enough:**
  A single shortest-path run from S is not enough as it does not tell you what vertices or edges that could be on the shortest-path to a given destination T. It cannot make the decision to know whether a node or edge fall in the shortest path from S to destination T.

- **What decision remains after all inter-location costs are known:**
  The structural decision that remains after all inter-location costs are known is: what structure should be used to optimally organize and connect the locations to fufill our overall objective?

- **Why this requires a search over orders (one sentence):**
  This problem requires a search over orders as the number of different paths that one can take to complete the objective grows combinatorially, and shortest path computations alone do not determine the optimal global arrangement.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| Start Node (S) | Initial node from which we compute the shortest-path to any other node |
| Goal Node (T) | Destination node in which we compute the shortest paths to reaching it |
| Intermediate Nodes | Middle-man nodes that can be used to compute distances between all pairs of nodes needed to find the global optimum |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | Dictionary (hash map) |
| What the keys represent | Pairs of nodes (u, v) representing a source and destination |
| What the values represent | Shortest-path distance between u and v |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Hashing allows direct access to values by key without iteration |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** k
- **Cost per run:** O(m log n)
- **Total complexity:** O(k * m log n)
- **Justification (one line):** If we run Dijkstra once for each of the k important nodes to compute the distances to all other nodes when each costs O(m log n), we get O(k * m log n)

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  For nodes already finalized, the invariant describes that once it is added to S, its distance value is guaranteed to be the shortest possible path from the source x.

- **For nodes not yet finalized (not in S):**
  For nodes not yet finalized, the invariant describes that the current distance is the best path found so far only using finalized nodes, yet will still continue to update if a shorter path is to be found when more nodes are processed.

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  The source node starts with distance 0 since the cost to travel to the source node from itself is 0, and all other distance are infinity as no other paths have been discovered yet.

- **Maintenance : why finalizing the min-dist node is always correct:**
  + Finalizing the min-dist node is always correct because all edge weights are nonnegative, so the smallest unfinalized distance could not possibly get any smaller under another run. 
  + Relaxing outgoing edges continues to update the neighboring nodes' shortest distance paths therefore maintaining that min-dist will always be finalized.

- **Termination : what the invariant guarantees when the algorithm ends:**
  The invariant guarantees that all shortest-paths to each node from the source node will be found and finalized when the algorithm ends.

### Part 3c: Why This Matters for the Route Planner

This matters for the route planner as in order to make the optimal routing decisions, it is necessary to have the finalized shortest paths from each relevant pair node to then find the shortest path from start node S to destination T.

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** A route fails when a smaller cost (more optimal) route is found.
- **Counter-example setup:** Given this table as my counter-example map,
    | From \ To | B   | C   | D   | T   |
    |-----------|-----|-----|-----|-----|
    | S         | 1   | 2   | 2   | --  |
    | B         | --  | 1   | 100 | 1   |
    | C         | 1   | --  | 100 | 100 |
    | D         | 100 | 1   | --  | 100 |
- **What greedy picks:** Greedy chooses S -> B -> C -> D -> T, however, the cost of this path is:
    1 + 1 + 100 + 100 = 202
- **What optimal picks:** The optimal route chooses S -> D -> C -> B -> T, with cost:
    2 + 1 + 1 + 1 = 5
- **Why greedy loses:** Greedy chooses the cheapest next step locally, but that choice can force expensive later steps, so the final route may not be optimal.

### What the Algorithm Must Explore

- The algorithm must explore different orders of visiting the required nodes because the total route cost depends on the sequence in which the nodes are traversed.

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_loc | node | is the current location we are exploring from to find the most optimal sequence of relics following it |
| Relics already collected | relics_visited_order | list | keeps track of already visited relics in order to not re-visit them and stall the program |
| Fuel cost so far | cost_so_far | float | keeps track of the fuel cost so far to be compared with our current best cost to find the smallest cost |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | list |
| Operation: check if relic already collected | Time complexity: O(k) |
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | This structure fits because we are simply keeping track of what has already been visited, and then using append/pop to backtrack when necessary while directly storing thr route order returned by the algorithm |

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** O(k!)
- **Why:** The algorithm may need to explore every possible order of visiting the k relics, and the number of permutations of k items goes as k * (k-1) * (k-2) *... 1 which is k!

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

- Lecture Notes by Manju Muralidharan Priya, Canvas
- "Dijkstra’s Shortest Path Algorithm in Python" by Nkugwa Mark William, Medium Article, 2023
