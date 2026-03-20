from __future__ import annotations

from pathlib import Path
import subprocess


ROOT = Path("/Users/jensonphan/cs163-github-repo")
PS9 = ROOT / "ps9"
NEATO = "/opt/homebrew/bin/neato"
DOT = "/opt/homebrew/bin/dot"


def render_neato(dot_path: Path) -> None:
    for ext in ("png", "svg"):
        with dot_path.with_suffix(f".{ext}").open("wb") as f:
            subprocess.run([NEATO, "-n", f"-T{ext}", str(dot_path)], check=True, stdout=f)


def render_dot(dot_path: Path) -> None:
    for ext in ("png", "svg"):
        with dot_path.with_suffix(f".{ext}").open("wb") as f:
            subprocess.run([DOT, f"-T{ext}", str(dot_path)], check=True, stdout=f)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="ascii")


def problem2() -> None:
    out = PS9 / "problem2_matching_independent_set_pairs"
    dot_path = out / "construction_example_m3_i5.dot"
    dot_text = """graph G {
  graph [
    layout=neato,
    overlap=false,
    splines=false,
    outputorder=edgesfirst,
    bgcolor="white",
    pad=0.35,
    labelloc=t,
    fontsize=20,
    fontname="Helvetica",
    label="PS9 Problem 2: feasible pairs (M, I) for bipartite graphs\\nExample with M = 3 and I = 5: take M disjoint edges plus I-M isolates. Possible exactly when 0 <= M <= I."
  ];

  node [shape=circle, fixedsize=true, width=0.72, height=0.72, style=filled, fontname="Helvetica", fontsize=18, penwidth=1.8, pin=true];
  edge [color="#dc2626", penwidth=2.8];

  left_label [shape=plain, width=0, height=0, margin=0, style="", label="Independent set of size 5", pos="120,340!"];
  right_label [shape=plain, width=0, height=0, margin=0, style="", label="Other side", pos="420,340!"];

  u1 [label="u1", fillcolor="#dcfce7", color="#166534", pos="120,260!"];
  u2 [label="u2", fillcolor="#dcfce7", color="#166534", pos="120,180!"];
  u3 [label="u3", fillcolor="#dcfce7", color="#166534", pos="120,100!"];
  i1 [label="i1", fillcolor="#dcfce7", color="#166534", pos="120,20!"];
  i2 [label="i2", fillcolor="#dcfce7", color="#166534", pos="120,-60!"];

  v1 [label="v1", fillcolor="#ffedd5", color="#ea580c", pos="420,260!"];
  v2 [label="v2", fillcolor="#ffedd5", color="#ea580c", pos="420,180!"];
  v3 [label="v3", fillcolor="#ffedd5", color="#ea580c", pos="420,100!"];

  u1 -- v1 [label="matched"];
  u2 -- v2 [label="matched"];
  u3 -- v3 [label="matched"];
}
"""
    write(dot_path, dot_text)
    render_neato(dot_path)


def problem3() -> None:
    out = PS9 / "problem3_greedy_weighted_matching"

    counterexample = out / "counterexample_cycle.dot"
    counterexample_text = """graph G {
  graph [
    layout=neato,
    overlap=false,
    splines=false,
    outputorder=edgesfirst,
    bgcolor="white",
    pad=0.35,
    labelloc=t,
    fontsize=20,
    fontname="Helvetica",
    label="PS9 Problem 3.1: 4-cycle counterexample to greedy weighted matching\\nFor 0 < eps < 1, use weights top = 1/2+eps/2, bottom = eps/2, left = right = 1/2. Greedy gets 1/2+eps; optimum gets 1."
  ];

  node [shape=circle, fixedsize=true, width=0.72, height=0.72, style=filled, fillcolor="#f8fafc", color="#0f172a", penwidth=1.8, fontname="Helvetica", fontsize=18, pin=true];
  edge [fontname="Helvetica", fontsize=16];

  tl [label="u", pos="0,220!"];
  tr [label="v", pos="220,220!"];
  br [label="x", pos="220,0!"];
  bl [label="y", pos="0,0!"];

  tl -- tr [color="#dc2626", penwidth=3.2, fontcolor="#dc2626", label="1/2 + eps/2"];
  bl -- br [color="#dc2626", penwidth=3.2, fontcolor="#dc2626", label="eps/2"];
  tl -- bl [color="#2563eb", penwidth=3.2, fontcolor="#2563eb", label="1/2"];
  tr -- br [color="#2563eb", penwidth=3.2, fontcolor="#2563eb", label="1/2"];
}
"""
    write(counterexample, counterexample_text)
    render_neato(counterexample)

    charging = out / "half_approximation_charging.dot"
    charging_text = """graph G {
  graph [
    layout=neato,
    overlap=false,
    splines=false,
    outputorder=edgesfirst,
    bgcolor="white",
    pad=0.35,
    labelloc=t,
    fontsize=20,
    fontname="Helvetica",
    label="PS9 Problem 3.2: why greedy is always a 1/2-approximation\\nEach optimal edge is either chosen by greedy or blocked by a heavier greedy edge. A greedy edge can block at most two optimal edges."
  ];

  node [shape=circle, fixedsize=true, width=0.72, height=0.72, style=filled, fillcolor="#f8fafc", color="#0f172a", penwidth=1.8, fontname="Helvetica", fontsize=18, pin=true];
  edge [fontname="Helvetica", fontsize=16];

  x [label="x", pos="0,0!"];
  u [label="u", pos="200,0!"];
  v [label="v", pos="450,0!"];
  y [label="y", pos="650,0!"];

  x -- u [color="#2563eb", penwidth=3.0];
  u -- v [color="#dc2626", penwidth=3.4];
  v -- y [color="#2563eb", penwidth=3.0];

  o1 [shape=plain, width=0, height=0, margin=0, style="", fontcolor="#2563eb", label="optimal edge o1", pos="100,55!"];
  g1 [shape=plain, width=0, height=0, margin=0, style="", fontcolor="#dc2626", label="greedy edge g", pos="325,55!"];
  o2 [shape=plain, width=0, height=0, margin=0, style="", fontcolor="#2563eb", label="optimal edge o2", pos="550,55!"];
  note2 [shape=plain, width=0, height=0, margin=0, style="", label="Charge each optimal edge to a greedy edge of at least the same weight. Since each greedy edge has two endpoints, it gets charged at most twice.", pos="325,-85!"];
}
"""
    write(charging, charging_text)
    render_neato(charging)


def problem4() -> None:
    out = PS9 / "problem4_stable_matching_tradeoff"

    table = out / "preferences_table.dot"
    table_text = """digraph G {
  graph [
    bgcolor="white",
    pad=0.35,
    labelloc=t,
    fontsize=20,
    fontname="Helvetica",
    label="PS9 Problem 4 preference table"
  ];
  node [shape=plain];
  prefs [label=<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="8">
      <TR><TD><B>Participant</B></TD><TD><B>Preference order</B></TD></TR>
      <TR><TD>A</TD><TD>Z, W, X, Y</TD></TR>
      <TR><TD>B</TD><TD>W, X, Y, Z</TD></TR>
      <TR><TD>C</TD><TD>Z, Y, W, X</TD></TR>
      <TR><TD>D</TD><TD>W, Z, X, Y</TD></TR>
      <TR><TD>W</TD><TD>B, A, C, D</TD></TR>
      <TR><TD>X</TD><TD>C, B, A, D</TD></TR>
      <TR><TD>Y</TD><TD>B, C, A, D</TD></TR>
      <TR><TD>Z</TD><TD>C, D, A, B</TD></TR>
    </TABLE>
  >];
}
"""
    write(table, table_text)
    render_dot(table)

    unstable = out / "second_choice_unstable_matching.dot"
    unstable_text = """graph G {
  graph [
    layout=neato,
    overlap=false,
    splines=false,
    outputorder=edgesfirst,
    bgcolor="white",
    pad=0.35,
    labelloc=t,
    fontsize=20,
    fontname="Helvetica",
    label="PS9 Problem 4.1: everyone gets second choice, but the matching is unstable\\nMatching: A-W, B-X, C-Y, D-Z. Blocking pair: B-W."
  ];

  node [shape=circle, fixedsize=true, width=0.72, height=0.72, style=filled, fontname="Helvetica", fontsize=18, penwidth=1.8, pin=true];
  edge [fontname="Helvetica", fontsize=16];

  A [label="A", fillcolor="#dbeafe", color="#2563eb", pos="0,240!"];
  B [label="B", fillcolor="#dbeafe", color="#2563eb", pos="0,160!"];
  C [label="C", fillcolor="#dbeafe", color="#2563eb", pos="0,80!"];
  D [label="D", fillcolor="#dbeafe", color="#2563eb", pos="0,0!"];

  W [label="W", fillcolor="#ffedd5", color="#ea580c", pos="300,240!"];
  X [label="X", fillcolor="#ffedd5", color="#ea580c", pos="300,160!"];
  Y [label="Y", fillcolor="#ffedd5", color="#ea580c", pos="300,80!"];
  Z [label="Z", fillcolor="#ffedd5", color="#ea580c", pos="300,0!"];

  A -- W [color="#2563eb", penwidth=3.0, fontcolor="#2563eb", label="(2,2)"];
  B -- X [color="#2563eb", penwidth=3.0, fontcolor="#2563eb", label="(2,2)"];
  C -- Y [color="#2563eb", penwidth=3.0, fontcolor="#2563eb", label="(2,2)"];
  D -- Z [color="#2563eb", penwidth=3.0, fontcolor="#2563eb", label="(2,2)"];
  B -- W [color="#dc2626", penwidth=3.0, style=dashed, fontcolor="#dc2626", label="blocking pair"];
}
"""
    write(unstable, unstable_text)
    render_neato(unstable)

    stable_only = out / "stable_matching_only.dot"
    stable_only_text = """graph G {
  graph [
    layout=neato,
    overlap=false,
    splines=false,
    outputorder=edgesfirst,
    bgcolor="white",
    pad=0.35,
    labelloc=t,
    fontsize=20,
    fontname="Helvetica",
    label="PS9 Problem 4.2: the unique stable matching\\nB-W and C-Z are forced because they are mutual first choices."
  ];

  node [shape=circle, fixedsize=true, width=0.7, height=0.7, style=filled, fontname="Helvetica", fontsize=18, penwidth=1.8, pin=true];
  edge [fontname="Helvetica", fontsize=16];

  A [label="A", fillcolor="#dbeafe", color="#2563eb", pos="0,220!"];
  B [label="B", fillcolor="#dbeafe", color="#2563eb", pos="0,140!"];
  C [label="C", fillcolor="#dbeafe", color="#2563eb", pos="0,60!"];
  D [label="D", fillcolor="#dbeafe", color="#2563eb", pos="0,-20!"];
  W [label="W", fillcolor="#ffedd5", color="#ea580c", pos="300,220!"];
  X [label="X", fillcolor="#ffedd5", color="#ea580c", pos="300,140!"];
  Y [label="Y", fillcolor="#ffedd5", color="#ea580c", pos="300,60!"];
  Z [label="Z", fillcolor="#ffedd5", color="#ea580c", pos="300,-20!"];

  B -- W [color="#16a34a", penwidth=3.2];
  C -- Z [color="#16a34a", penwidth=3.2];
  A -- X [color="#2563eb", penwidth=3.0];
  D -- Y [color="#2563eb", penwidth=3.0];
  stable_note1 [shape=plain, width=0, height=0, margin=0, style="", label="Forced pairs: B-W and C-Z", pos="150,285!"];
  stable_note2 [shape=plain, width=0, height=0, margin=0, style="", label="Pair costs: B-W (1,1), C-Z (1,1), A-X (3,3), D-Y (4,4)", pos="150,-85!"];
  stable_score [shape=plain, width=0, height=0, margin=0, style="", label="Total score = 18", pos="150,-110!"];
}
"""
    write(stable_only, stable_only_text)
    render_neato(stable_only)

    min_unstable = out / "minweight_but_unstable.dot"
    min_unstable_text = """graph G {
  graph [
    layout=neato,
    overlap=false,
    splines=false,
    outputorder=edgesfirst,
    bgcolor="white",
    pad=0.35,
    labelloc=t,
    fontsize=20,
    fontname="Helvetica",
    label="PS9 Problem 4.2: the minimum-weight perfect matching is not stable\\nThe minimum-weight matching has score 16, but B-W is a blocking pair."
  ];

  node [shape=circle, fixedsize=true, width=0.7, height=0.7, style=filled, fontname="Helvetica", fontsize=18, penwidth=1.8, pin=true];
  edge [fontname="Helvetica", fontsize=16];

  A [label="A", fillcolor="#dbeafe", color="#2563eb", pos="0,220!"];
  B [label="B", fillcolor="#dbeafe", color="#2563eb", pos="0,140!"];
  C [label="C", fillcolor="#dbeafe", color="#2563eb", pos="0,60!"];
  D [label="D", fillcolor="#dbeafe", color="#2563eb", pos="0,-20!"];
  W [label="W", fillcolor="#ffedd5", color="#ea580c", pos="300,220!"];
  X [label="X", fillcolor="#ffedd5", color="#ea580c", pos="300,140!"];
  Y [label="Y", fillcolor="#ffedd5", color="#ea580c", pos="300,60!"];
  Z [label="Z", fillcolor="#ffedd5", color="#ea580c", pos="300,-20!"];

  A -- W [color="#2563eb", penwidth=3.0];
  B -- X [color="#2563eb", penwidth=3.0];
  C -- Y [color="#2563eb", penwidth=3.0];
  D -- Z [color="#2563eb", penwidth=3.0];
  B -- W [color="#dc2626", penwidth=3.0, style=dashed, fontcolor="#dc2626", label="blocking pair"];
  note1 [shape=plain, width=0, height=0, margin=0, style="", label="All matched pairs contribute (2,2)", pos="150,-85!"];
  note2 [shape=plain, width=0, height=0, margin=0, style="", label="Total score = 16, but not stable", pos="150,-110!"];
}
"""
    write(min_unstable, min_unstable_text)
    render_neato(min_unstable)


def main() -> None:
    problem2()
    problem3()
    problem4()


if __name__ == "__main__":
    main()
