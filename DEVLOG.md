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

## Entry 3 – [5/14/2026]: Establishing why Greedy fails in Part 4 and implementing my solution to find the optimal route in Part 5

Hi again journal, I have since established why a greedy solution would not work for our specific problem and incorporated one that could actually help us find the optimal solution by checking each possible sequence of relics in order to find the lowest cost option, included with backtracking and pruning. At first I was having trouble figuring out how to properly structure my find_optimal_route() and _explore() helper methods, but I used the help of lecture notes and previous assignments to figure out the order in which I should prune, check the base case, and recur with all the necessary features like updating if a smaller cost is found. Then, I updated the README.md to include all of the components and properties I used in my solution as well as the time complexities.

---

## Entry 4 – [5/14/2026]: Post-Implementation Reflection

HELLO JOURNAL FOR THE LAST TIME! It has been quite a ride, rather than spacing out 15 hours of work throughout a couple days, I had decided to do 15 hours of work straight and will reconsider my life choices in the future (I did take sleep and snack breaks). If given more time, I would probably work on better articulating my algorithm and thought process in the README.md since I felt like it got too wordy or redundant for some of the content. With the code implementation, I want to practice retracing my logic steps and translating that into code more, since I spent way too much time thinking about how to start tackling the problem, although I did have a viable solution in the end. Overall, this was a practical final assessment that concludes this whole class semester, and I have learned a lot from the very beginning until now.

---

## Final Entry – [5/14/2026]: Time Estimate

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 1 |
| Part 2: Precomputation Design | 2 |
| Part 3: Algorithm Correctness | 1 |
| Part 4: Search Design | 1 |
| Part 5: State and Search Space | 2 |
| Part 6: Pruning | 1 |
| Part 7: Implementation | 5 |
| README and DEVLOG writing | 2 |
| **Total** | 15 |
