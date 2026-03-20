# Backward Edge Example

This is the standard tiny example showing why residual graphs need **backward edges**.

The question is:

> Can a flow algorithm ever need to go backward because it picked a bad path earlier?

Yes.

That is exactly what residual backward edges are for.

## The network

Start with this flow network, where every edge has capacity `1`:

![Original network](backward_edge_original.png)

Edges:

- `s -> a`
- `s -> b`
- `a -> b`
- `a -> t`
- `b -> t`

The true maximum flow is `2`, because we can eventually send:

- one unit on `s -> a -> t`
- one unit on `s -> b -> t`

## Step 1: take a bad path first

Suppose the algorithm first augments along:

`s -> a -> b -> t`

That sends `1` unit of flow and gives:

![Bad first path](backward_edge_bad_path.png)

Now three edges are saturated:

- `s -> a`
- `a -> b`
- `b -> t`

If you only looked at the original graph, it would feel like you got stuck with value `1`.

But you are **not** supposed to look only at the original graph.

You must look at the **residual graph**.

## Step 2: the residual graph creates a backward edge

After sending `1` unit on `a -> b`, the residual graph contains the backward edge:

`b -> a`

Why?

Because the algorithm is allowed to **undo** some or all of the flow it previously placed on `a -> b`.

The residual graph now has this augmenting path:

`s -> b -> a -> t`

shown here:

![Residual fix](backward_edge_residual_fix.png)

The important part is the middle edge `b -> a`.

That edge does **not** exist in the original network.

It exists only in the residual graph, and it means:

- cancel the old `1` unit on `a -> b`

So this second augmentation does three things at once:

1. sends a new unit on `s -> b`
2. removes the old unit on `a -> b`
3. sends a unit on `a -> t`

## Step 3: the flow is corrected

After that rerouting, the final flow is:

![Final corrected flow](backward_edge_final_flow.png)

Now the flow uses:

- `s -> a -> t`
- `s -> b -> t`

with total value `2`.

So the algorithm did need to "go backward," but not because it was confused.

It went backward because:

- the first augmenting path used the middle edge `a -> b` in a way that blocked a better arrangement
- the residual graph let the algorithm undo that local mistake and reroute the flow

## What this example teaches

- **Backward residual edges are essential.**
  Without them, augmenting-path algorithms could get trapped in bad early choices.

- **A backward edge means "you may cancel flow here."**
  It is not a new real pipe in the original network.

- **Residual graphs describe flexibility, not just unused capacity.**
  They tell you where you can push more flow and where you can reverse earlier flow.

- **Going backward is really rerouting.**
  The algorithm is not losing flow value. It is rearranging the existing flow to make room for more.
