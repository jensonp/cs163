# PS9 Problem 2

Possible pairs are exactly the integer pairs with

`0 <= M <= I`.

Why these are necessary:

- In any bipartite graph with parts `L` and `R`, both `L` and `R` are independent sets.
- So the maximum independent set size `I` is at least `max(|L|, |R|)`, hence at least `n/2`.
- For bipartite graphs we also have `M + I = n`.
- Substituting `n = M + I` into `I >= n/2` gives `I >= M`.

Why these are sufficient:

- For any `M <= I`, let `k = I - M`.
- Build a bipartite graph consisting of `M` disjoint edges plus `k` isolated vertices.
- Then the maximum matching size is exactly `M`, because the `M` disjoint edges can all be matched.
- The maximum independent set size is `M + k = I`, by taking one endpoint from each edge and all `k` isolates.

The picture in this folder shows the example `M = 3`, `I = 5`.
