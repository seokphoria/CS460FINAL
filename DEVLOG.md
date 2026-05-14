# Development Log – The Torchbearer

**Student Name:** Sophia Phung
**Student ID:** 132046561

---

## Entry 1 – [5/13/2026]: Initial Plan

My plan is to use the Travelling Salesman Problem as the basis of my design and advance from there, as it is similar in terms of what we are solving. I am working on the introductory parts first before programming any code, and figuring out what structure I will be using to implement my solution. I expect the logistics of this problem to be the most difficult, aka the first couple parts, as you must figure out what structure is the best then calculate what the most optimal solution should be and compare with your algorithm's results, which is much more brain power than just putting in code and praying it gives an answer. I plan to test by running my program within VSCode using my terminal on hopes and dreams.

---

## Entry 2 – [5/14/2026]: Implemented Dijkstras Algorithm for Part 2 and Answered Part 3

Hello journal, I have finally implemented the first stage of solving this problem which is using Dijkstra's Algorithm to iterate over each pair node in the graph to find the shortest-path not just in a single run from the start node S to destination T. Intially, I was having difficutly coming up with the correct structure to use in my planning stage, as I wrongly assumed we must use something similar to a priority queue to find the shortest edges. However, after realizing that was for building an MST tree rather than path building, I realized I needed to use a python Dictionary (or hash map) to store the each node and their current distance from the source to build my shortest path algorithm. This was thanks to the help of a Medium article by Nkugwa Mark William called "Dijkstra’s Shortest Path Algorithm in Python" that had the implementation I was looking for to help solve this problem. I also just finished Part 3 which I did not have much trouble with, as the answers were pretty straightforward.

---

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
