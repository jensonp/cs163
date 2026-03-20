from pathlib import Path
import subprocess


ROOT = Path("/Users/jensonphan/cs163-github-repo/final_exam_planarity_mechanics")
DOT = "/opt/homebrew/bin/dot"
NEATO = "/opt/homebrew/bin/neato"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="ascii")


def render(dot_path: Path, layout: str = "dot") -> None:
    bin_path = DOT if layout == "dot" else NEATO
    args = [bin_path]
    if layout == "neato":
        args.append("-n")
    for ext in ("png", "svg"):
        with dot_path.with_suffix(f".{ext}").open("wb") as f:
            subprocess.run(args + [f"-T{ext}", str(dot_path)], check=True, stdout=f)


def q1() -> None:
    base = ROOT / "question1_schnyder_wood_reconstruction"

    coordinate_positions = r"""graph G {
  graph [layout=neato, overlap=false, splines=true, outputorder=edgesfirst, bgcolor="white", pad=0.3, labelloc=t, fontsize=20, fontname="Helvetica", label="Question 1: coordinates inside the outer root triangle"];
  node [shape=circle, fixedsize=true, width=1.05, height=1.05, style=filled, fontname="Helvetica", fontsize=15, penwidth=2.1, pin=true];
  edge [color="#94a3b8", penwidth=2.0];

  R [label="Red", fillcolor="#fee2e2", color="#dc2626", pos="210,330!"];
  G [label="Green", fillcolor="#dcfce7", color="#16a34a", pos="55,55!"];
  B [label="Blue", fillcolor="#dbeafe", color="#2563eb", pos="365,55!"];

  v1 [label="v1\n(1,2,2)", fillcolor="#f8fafc", color="#475569", pos="210,155!"];
  v2 [label="v2\n(3,1,1)", fillcolor="#f8fafc", color="#475569", pos="210,220!"];

  R -- G;
  G -- B;
  B -- R;
}"""

    reconstructed = r"""digraph G {
  graph [layout=neato, overlap=false, splines=true, outputorder=edgesfirst, bgcolor="white", pad=0.3, labelloc=t, fontsize=20, fontname="Helvetica", label="Question 1: reconstructed Schnyder wood"];
  node [shape=circle, fixedsize=true, width=1.05, height=1.05, style=filled, fontname="Helvetica", fontsize=15, penwidth=2.1, pin=true];
  edge [fontname="Helvetica", fontsize=13, arrowsize=0.9, penwidth=2.6];

  R [label="Red", fillcolor="#fee2e2", color="#dc2626", pos="210,330!"];
  G [label="Green", fillcolor="#dcfce7", color="#16a34a", pos="55,55!"];
  B [label="Blue", fillcolor="#dbeafe", color="#2563eb", pos="365,55!"];

  v1 [label="v1\n(1,2,2)", fillcolor="#f8fafc", color="#475569", pos="210,155!"];
  v2 [label="v2\n(3,1,1)", fillcolor="#f8fafc", color="#475569", pos="210,220!"];

  R -> G [dir=none, color="#94a3b8", penwidth=2.0];
  G -> B [dir=none, color="#94a3b8", penwidth=2.0];
  B -> R [dir=none, color="#94a3b8", penwidth=2.0];

  v2 -> R [color="#dc2626", fontcolor="#dc2626", label="red"];
  v1 -> v2 [color="#dc2626", fontcolor="#dc2626", label="red"];

  v2 -> G [color="#16a34a", fontcolor="#16a34a", label="green"];
  v1 -> G [color="#16a34a", fontcolor="#16a34a", label="green"];

  v2 -> B [color="#2563eb", fontcolor="#2563eb", label="blue"];
  v1 -> B [color="#2563eb", fontcolor="#2563eb", label="blue"];
}"""

    count_logic = r"""digraph G {
  graph [bgcolor="white", pad=0.3, labelloc=t, fontsize=20, fontname="Helvetica", label="Question 1: region-count logic"];
  node [shape=plain];
  t [label=<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="8">
      <TR><TD><B>Vertex</B></TD><TD><B>Coordinates</B></TD><TD><B>Mechanical reading</B></TD><TD><B>Forced outgoing edges</B></TD></TR>
      <TR>
        <TD><B>v2</B></TD>
        <TD>(3,1,1)</TD>
        <TD ALIGN="LEFT">The red side sees v1 twice; green and blue do not see it.</TD>
        <TD ALIGN="LEFT">v2 goes directly to Red, Green, Blue.</TD>
      </TR>
      <TR>
        <TD><B>v1</B></TD>
        <TD>(1,2,2)</TD>
        <TD ALIGN="LEFT">v2 contributes on the green and blue sides, but not on the red side.</TD>
        <TD ALIGN="LEFT">v1 goes directly to Green and Blue, and its red parent is v2.</TD>
      </TR>
      <TR>
        <TD COLSPAN="4" ALIGN="LEFT"><B>Conclusion:</B> the internal edge is a red edge directed v1 -&gt; v2, and the only missing primal edge is v1-Red.</TD>
      </TR>
    </TABLE>
  >];
}"""

    for name, text, layout in [
        ("coordinate_positions.dot", coordinate_positions, "neato"),
        ("reconstructed_schnyder.dot", reconstructed, "neato"),
        ("count_logic.dot", count_logic, "dot"),
    ]:
        path = base / name
        write(path, text)
        render(path, layout)


def q2() -> None:
    base = ROOT / "question2_bipartite_planar_limit"

    derivation_flow = r"""digraph G {
  graph [bgcolor="white", rankdir=TB, nodesep=0.45, ranksep=0.5, pad=0.3, labelloc=t, fontsize=20, fontname="Helvetica", label="Question 2: deriving the bipartite planar bound"];
  node [shape=box, style="rounded,filled", fillcolor="#f8fafc", color="#475569", fontname="Helvetica", fontsize=15, margin="0.18,0.12"];
  edge [color="#64748b", penwidth=2.0, arrowsize=0.8];

  a [label="Bipartite => no odd cycles =>\nevery face degree is at least 4"];
  b [label="Face handshaking:\nsum deg(face) = 2E"];
  c [label="Therefore 2E >= 4F,\nso F <= E/2"];
  d [label="Euler with V = 100:\n100 - E + F = 2"];
  e [label="Substitute F <= E/2:\n100 - E + E/2 >= 2"];
  f [label="So E <= 196"];
  g [label="Then F = 2 - 100 + 196 = 98"];

  a -> b -> c -> d -> e -> f -> g;
}"""

    quadrangulation_example = r"""graph G {
  graph [layout=neato, overlap=false, splines=true, outputorder=edgesfirst, bgcolor="white", pad=0.3, labelloc=t, fontsize=20, fontname="Helvetica", label="Question 2: small equality-case example (cube graph)"];
  node [shape=circle, fixedsize=true, width=0.55, height=0.55, style=filled, fillcolor="#f8fafc", color="#475569", penwidth=1.8, fontname="Helvetica", fontsize=12, pin=true];
  edge [color="#0f172a", penwidth=2.0];

  a [pos="40,40!"];
  b [pos="160,40!"];
  c [pos="160,160!"];
  d [pos="40,160!"];
  e [pos="80,80!"];
  f [pos="120,80!"];
  g [pos="120,120!"];
  h [pos="80,120!"];

  a -- b -- c -- d -- a;
  e -- f -- g -- h -- e;
  a -- e;
  b -- f;
  c -- g;
  d -- h;
}"""

    summary_table = r"""digraph G {
  graph [bgcolor="white", pad=0.3, labelloc=t, fontsize=20, fontname="Helvetica", label="Question 2: summary"];
  node [shape=plain];
  t [label=<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10">
      <TR><TD><B>Quantity</B></TD><TD><B>Value</B></TD><TD><B>Reason</B></TD></TR>
      <TR><TD>V</TD><TD>100</TD><TD>Given</TD></TR>
      <TR><TD>E_max</TD><TD>196</TD><TD>2E &gt;= 4F and Euler</TD></TR>
      <TR><TD>F_max</TD><TD>98</TD><TD>F = 2 - V + E</TD></TR>
      <TR><TD>Face degree at equality</TD><TD>4</TD><TD>Average face degree is exactly 4, so every face hits the minimum</TD></TR>
    </TABLE>
  >];
}"""

    for name, text, layout in [
        ("derivation_flow.dot", derivation_flow, "dot"),
        ("quadrangulation_example.dot", quadrangulation_example, "neato"),
        ("summary_table.dot", summary_table, "dot"),
    ]:
        path = base / name
        write(path, text)
        render(path, layout)


def q3() -> None:
    base = ROOT / "question3_auslander_parter_flap_test"

    cycle_with_chords = r"""graph G {
  graph [layout=neato, overlap=false, splines=true, outputorder=edgesfirst, bgcolor="white", pad=0.3, labelloc=t, fontsize=20, fontname="Helvetica", label="Question 3: cycle C and the three extra chords"];
  node [shape=circle, fixedsize=true, width=0.72, height=0.72, style=filled, fillcolor="#f8fafc", color="#475569", penwidth=1.9, fontname="Helvetica", fontsize=14, pin=true];
  edge [penwidth=2.2];

  n1 [label="1", pos="210,330!"];
  n2 [label="2", pos="340,255!"];
  n3 [label="3", pos="340,105!"];
  n4 [label="4", pos="210,30!"];
  n5 [label="5", pos="80,105!"];
  n6 [label="6", pos="80,255!"];

  n1 -- n2 [color="#334155"];
  n2 -- n3 [color="#334155"];
  n3 -- n4 [color="#334155"];
  n4 -- n5 [color="#334155"];
  n5 -- n6 [color="#334155"];
  n6 -- n1 [color="#334155"];

  n1 -- n4 [color="#dc2626"];
  n2 -- n5 [color="#16a34a"];
  n3 -- n6 [color="#2563eb"];
}"""

    flap_extraction = r"""digraph G {
  graph [bgcolor="white", pad=0.3, labelloc=t, fontsize=20, fontname="Helvetica", label="Question 3: the flaps generated by C"];
  node [shape=plain];
  t [label=<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10">
      <TR><TD><B>Non-cycle edge</B></TD><TD><B>Flap label</B></TD><TD><B>Why it is a flap</B></TD></TR>
      <TR><TD>(1,4)</TD><TD>F14</TD><TD ALIGN="LEFT">All endpoints already lie on C, so this chord is one isolated off-cycle piece.</TD></TR>
      <TR><TD>(2,5)</TD><TD>F25</TD><TD ALIGN="LEFT">Same reason.</TD></TR>
      <TR><TD>(3,6)</TD><TD>F36</TD><TD ALIGN="LEFT">Same reason.</TD></TR>
      <TR><TD COLSPAN="3" ALIGN="LEFT">After the textbook split-edge step, each chord becomes one tiny connected component, so each chord is exactly one flap.</TD></TR>
    </TABLE>
  >];
}"""

    interleaving_checks = r"""digraph G {
  graph [bgcolor="white", pad=0.3, labelloc=t, fontsize=20, fontname="Helvetica", label="Question 3: pairwise interleaving checks"];
  node [shape=plain];
  t [label=<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10">
      <TR><TD><B>Pair</B></TD><TD><B>Cyclic order on C</B></TD><TD><B>Conflict?</B></TD></TR>
      <TR><TD>F14 vs F25</TD><TD>1, 2, 4, 5</TD><TD>Yes</TD></TR>
      <TR><TD>F14 vs F36</TD><TD>1, 3, 4, 6</TD><TD>Yes</TD></TR>
      <TR><TD>F25 vs F36</TD><TD>2, 3, 5, 6</TD><TD>Yes</TD></TR>
    </TABLE>
  >];
}"""

    conflict_graph = r"""graph G {
  graph [layout=neato, overlap=false, splines=true, outputorder=edgesfirst, bgcolor="white", pad=0.3, labelloc=t, fontsize=20, fontname="Helvetica", label="Question 3: compatibility/conflict graph = K3"];
  node [shape=circle, fixedsize=true, width=0.95, height=0.95, style=filled, fillcolor="#fee2e2", color="#dc2626", penwidth=2.0, fontname="Helvetica", fontsize=14, pin=true];
  edge [color="#dc2626", penwidth=2.4];

  f14 [label="F14", pos="210,300!"];
  f25 [label="F25", pos="90,80!"];
  f36 [label="F36", pos="330,80!"];

  f14 -- f25;
  f25 -- f36;
  f36 -- f14;
}"""

    two_color_failure = r"""graph G {
  graph [layout=neato, overlap=false, splines=true, outputorder=edgesfirst, bgcolor="white", pad=0.3, labelloc=t, fontsize=20, fontname="Helvetica", label="Question 3: impossible two-color inside/outside assignment"];
  node [shape=circle, fixedsize=true, width=1.0, height=1.0, style=filled, penwidth=2.0, fontname="Helvetica", fontsize=13, pin=true];
  edge [color="#0f172a", penwidth=2.4];

  f14 [label="F14\ninside", fillcolor="#dcfce7", color="#16a34a", pos="210,300!"];
  f25 [label="F25\noutside", fillcolor="#dbeafe", color="#2563eb", pos="90,80!"];
  f36 [label="F36\n?", fillcolor="#fff7ed", color="#ea580c", pos="330,80!"];

  f14 -- f25;
  f25 -- f36;
  f36 -- f14;
}"""

    for name, text, layout in [
        ("cycle_with_chords.dot", cycle_with_chords, "neato"),
        ("flap_extraction.dot", flap_extraction, "dot"),
        ("interleaving_checks.dot", interleaving_checks, "dot"),
        ("conflict_graph.dot", conflict_graph, "neato"),
        ("two_color_failure.dot", two_color_failure, "neato"),
    ]:
        path = base / name
        write(path, text)
        render(path, layout)


def q4() -> None:
    base = ROOT / "question4_disconnected_dual"

    primal_forest_example = r"""graph G {
  graph [layout=neato, overlap=false, splines=true, outputorder=edgesfirst, bgcolor="white", pad=0.3, labelloc=t, fontsize=20, fontname="Helvetica", label="Question 4: disconnected primal graph with one tree per component"];
  node [shape=circle, fixedsize=true, width=0.62, height=0.62, style=filled, fillcolor="#f8fafc", color="#475569", penwidth=1.8, fontname="Helvetica", fontsize=12, pin=true];
  edge [penwidth=2.4];

  a1 [label="a1", pos="60,200!"];
  a2 [label="a2", pos="170,200!"];
  a3 [label="a3", pos="115,100!"];

  b1 [label="b1", pos="320,200!"];
  b2 [label="b2", pos="430,200!"];
  b3 [label="b3", pos="375,100!"];

  a1 -- a2 [color="#0f172a"];
  a2 -- a3 [color="#0f172a"];
  a3 -- a1 [color="#dc2626", style=dashed, penwidth=2.0];

  b1 -- b2 [color="#0f172a"];
  b2 -- b3 [color="#0f172a"];
  b3 -- b1 [color="#dc2626", style=dashed, penwidth=2.0];
}"""

    dual_tree_example = r"""graph G {
  graph [layout=neato, overlap=false, splines=true, outputorder=edgesfirst, bgcolor="white", pad=0.3, labelloc=t, fontsize=20, fontname="Helvetica", label="Question 4: the dual is glued together at the one outside face"];
  node [shape=circle, fixedsize=true, width=1.0, height=1.0, style=filled, penwidth=2.0, fontname="Helvetica", fontsize=14, pin=true];
  edge [color="#2563eb", penwidth=2.6];

  o [label="outside\nface", fillcolor="#dbeafe", color="#2563eb", pos="245,260!"];
  fa [label="face A", fillcolor="#fef3c7", color="#d97706", pos="130,80!"];
  fb [label="face B", fillcolor="#fef3c7", color="#d97706", pos="360,80!"];

  o -- fa [label="unused edge in A", fontcolor="#2563eb"];
  o -- fb [label="unused edge in B", fontcolor="#2563eb"];
}"""

    count_argument = r"""digraph G {
  graph [bgcolor="white", pad=0.3, labelloc=t, fontsize=20, fontname="Helvetica", label="Question 4: count argument for why the dual subgraph is a tree"];
  node [shape=plain];
  t [label=<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10">
      <TR><TD><B>Step</B></TD><TD><B>Equation</B></TD></TR>
      <TR><TD>Euler for c = 2</TD><TD>n - m + f = 3</TD></TR>
      <TR><TD>Primal forest size</TD><TD>|T| = n - 2</TD></TR>
      <TR><TD>Unused primal edges</TD><TD>m - (n - 2) = m - n + 2</TD></TR>
      <TR><TD>Replace using Euler</TD><TD>m - n + 2 = f - 1</TD></TR>
      <TR><TD>Conclusion</TD><TD>The dual subgraph is connected and has exactly f - 1 edges, so it is a tree.</TD></TR>
    </TABLE>
  >];
}"""

    for name, text, layout in [
        ("primal_forest_example.dot", primal_forest_example, "neato"),
        ("dual_tree_example.dot", dual_tree_example, "neato"),
        ("count_argument.dot", count_argument, "dot"),
    ]:
        path = base / name
        write(path, text)
        render(path, layout)


def main() -> None:
    q1()
    q2()
    q3()
    q4()


if __name__ == "__main__":
    main()
