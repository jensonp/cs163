# CS163 Graphviz Exports

This directory is organized by practice set and problem number.
Each problem folder contains a `README.md` with a solution walkthrough and a fundamentals section.

## PS8

- `ps8/problem1_shortest_residual_paths/`
  - Problem 1
  - Sequence of flows and residual graphs for augmenting on unweighted shortest residual paths

- `ps8/problem2_widest_residual_paths/`
  - Problem 2
  - Sequence of flows and residual graphs for augmenting on widest residual paths

- `ps8/problem3_minimum_cuts/`
  - Problem 3
  - The two minimum cuts, plus the final max-flow state used by residual reachability

- `ps8/problem4_cancel_opposite_edge_flows/`
  - Problem 4
  - Cancelling flow on opposite directed edges `a -> b` and `b -> a`

- Source: `https://ics.uci.edu/~eppstein/163/w26-ps8.html`

## PS9

- `ps9/problem1_cube_matching_flow/`
  - Problem 1
  - Cube graph to flow-network reduction for bipartite matching
  - Includes the full network and one example integer maximum flow/perfect matching

- `ps9/problem2_matching_independent_set_pairs/`
  - Problem 2
  - Feasible `(M, I)` pairs for bipartite graphs with matching number `M` and independent set size `I`
  - Includes a construction example and an explanation of why the possible pairs are exactly `0 <= M <= I`

- `ps9/problem3_greedy_weighted_matching/`
  - Problem 3
  - 4-cycle counterexample for greedy weighted matching and a visual proof of the `1/2` approximation guarantee

- `ps9/problem4_stable_matching_tradeoff/`
  - Problem 4
  - Stable matching instance with the second-choice blocking pair and the stable-vs-minimum-weight comparison

- Source: `https://ics.uci.edu/~eppstein/163/w26-ps9.html`

## PS10

- `ps10/problem1_infinite_planar_tiling_degree_gt5/`
  - Problem 1
  - Infinite planar tiling example with all vertex degrees greater than five

- `ps10/problem2_nonplanar_k33_subdivision/`
  - Problem 2
  - Nonplanar graph proved via a `K3,3` subdivision
  - Includes the original graph, deleted edges, subdivision, contracted `K3,3`, and a detailed step-by-step explanation

- `ps10/problem3_k5_flaps_compatibility_graph/`
  - Problem 3
  - Pentagon drawing of `K5`, flap alternation example, and flap compatibility/conflict graph

- `ps10/problem4_maximal_planar_separating_triangle/`
  - Problem 4
  - Counterexample showing a maximal planar graph can contain a triangle that is not a face
  - Includes an extended explanation of separating triangles, connectivity, and the Hamiltonian caveat

- Source: `https://ics.uci.edu/~eppstein/163/w26-ps10.html`
