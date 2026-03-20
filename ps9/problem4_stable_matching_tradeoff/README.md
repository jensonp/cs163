# PS9 Problem 4

## 4.1 The second-choice matching is unstable

If every participant gets their second choice, the matching is

- `A-W`
- `B-X`
- `C-Y`
- `D-Z`

This is not stable because `B` prefers `W` to `X`, and `W` prefers `B` to `A`. So `(B, W)` is a blocking pair.

## 4.2 No stable matching is also minimum-weight

Give each participant a cost equal to the rank of their assigned partner. The total cost of a matching is the sum over all eight participants.

First observe:

- `B` and `W` are mutual first choices, so every stable matching must contain `B-W`.
- `C` and `Z` are mutual first choices, so every stable matching must contain `C-Z`.

That leaves only `A, D` to be matched with `X, Y`.

There are only two ways to do that:

- `A-X` and `D-Y`
- `A-Y` and `D-X`

The second one is not stable, because `A` prefers `X` to `Y` and `X` prefers `A` to `D`, so `(A, X)` blocks it.

Therefore the unique stable matching is

- `B-W`
- `C-Z`
- `A-X`
- `D-Y`

Its total score is

- `B-W`: `1 + 1 = 2`
- `C-Z`: `1 + 1 = 2`
- `A-X`: `3 + 3 = 6`
- `D-Y`: `4 + 4 = 8`

for total `18`.

But the minimum-weight perfect matching overall is the second-choice matching

- `A-W`
- `B-X`
- `C-Y`
- `D-Z`

with total score `16`.

So there is **no** stable matching that is also a minimum-weight matching.
