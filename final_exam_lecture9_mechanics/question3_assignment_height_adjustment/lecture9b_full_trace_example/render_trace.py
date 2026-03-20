from pathlib import Path
import subprocess


ROOT = Path("/Users/jensonphan/cs163-github-repo/final_exam_lecture9_mechanics/question3_assignment_height_adjustment/lecture9b_full_trace_example")
DOT = "/opt/homebrew/bin/dot"
NEATO = "/opt/homebrew/bin/neato"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="ascii")


def render_dot(dot_path: Path, layout: str = "dot") -> None:
    bin_path = DOT if layout == "dot" else NEATO
    args = [bin_path]
    if layout == "neato":
        args.append("-n")
    for ext in ("png", "svg"):
        with dot_path.with_suffix(f".{ext}").open("wb") as f:
            subprocess.run(args + [f"-T{ext}", str(dot_path)], check=True, stdout=f)


def matrix_table(title: str, red_heights: list[int], blue_heights: list[int], matrix: list[list[str]]) -> str:
    rows = []
    for rh, row in zip(red_heights, matrix):
        cells = "".join(f"<TD>{v}</TD>" for v in row)
        rows.append(f"<TR><TD>{rh}</TD>{cells}</TR>")
    blue = "".join(f"<TD>{h}</TD>" for h in blue_heights)
    return f"""digraph G {{
  graph [bgcolor="white", pad=0.35, labelloc=t, fontsize=20, fontname="Helvetica", label="{title}"];
  node [shape=plain];
  t [label=<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="8">
      <TR><TD></TD><TD COLSPAN="4"><B>blue heights</B></TD></TR>
      <TR><TD><B>red heights</B></TD>{blue}</TR>
      {''.join(rows)}
    </TABLE>
  >];
}}
"""


def state_graph(title: str, red_dist: list[str], blue_dist: list[str], highlight: list[tuple[str, str]], matched: list[tuple[str, str]]) -> str:
    highlights = {(u, v) for u, v in highlight}
    matched_set = {(u, v) for u, v in matched}
    matched_forward = {(v, u) for (u, v) in matched_set}

    def edge(u: str, v: str, label: str, dashed: bool = False) -> str:
        color = "#cbd5e1"
        font = "#0f172a"
        pen = "2.0"
        style = "dashed" if dashed else "solid"
        if (u, v) in highlights:
            color = "#16a34a"
            font = "#16a34a"
            pen = "3.6"
        elif (u, v) in matched_set:
            color = "#334155"
            font = "#334155"
            pen = "3.0"
        return f'  {u} -> {v} [label="{label}", color="{color}", fontcolor="{font}", penwidth={pen}, style="{style}"];'

    reverse_edges = [(b, r, "0") for (b, r) in matched_set]

    s_edges = [edge("s", f"r{i}", "0", True) for i in range(1, 5)]
    highlight_labels = {
        ("r4", "b4"): "1",
        ("r1", "b1"): "0",
        ("r3", "b4"): "0",
        ("r4", "b3"): "0",
        ("r2", "b2"): "0",
        ("b4", "r4"): "0",
        ("b1", "r1"): "0",
        ("b4", "r3"): "0",
        ("b3", "r4"): "0",
    }
    fwd = [edge(u, v, highlight_labels.get((u, v), "")) for (u, v) in highlights if u != "s" and (u, v) not in matched_set]
    rev = [edge(u, v, w) for (u, v, w) in reverse_edges]

    return f"""digraph G {{
  graph [layout=neato, overlap=false, splines=true, outputorder=edgesfirst, bgcolor="white", pad=0.35, labelloc=t, fontsize=20, fontname="Helvetica", label="{title}"];
  node [shape=circle, fixedsize=true, width=0.82, height=0.82, style=filled, fontname="Helvetica", fontsize=17, penwidth=2.0, pin=true];
  edge [arrowsize=0.8, fontname="Helvetica", fontsize=15];

  s [label="s", fillcolor="#fef3c7", color="#d97706", pos="0,120!"];
  r1 [label="r1\\n{red_dist[0]}", fillcolor="#dbeafe", color="#2563eb", pos="170,300!"];
  r2 [label="r2\\n{red_dist[1]}", fillcolor="#dbeafe", color="#2563eb", pos="170,210!"];
  r3 [label="r3\\n{red_dist[2]}", fillcolor="#dbeafe", color="#2563eb", pos="170,120!"];
  r4 [label="r4\\n{red_dist[3]}", fillcolor="#dbeafe", color="#2563eb", pos="170,30!"];

  b1 [label="b1\\n{blue_dist[0]}", fillcolor="#ffedd5", color="#ea580c", pos="390,300!"];
  b2 [label="b2\\n{blue_dist[1]}", fillcolor="#ffedd5", color="#ea580c", pos="390,210!"];
  b3 [label="b3\\n{blue_dist[2]}", fillcolor="#ffedd5", color="#ea580c", pos="390,120!"];
  b4 [label="b4\\n{blue_dist[3]}", fillcolor="#ffedd5", color="#ea580c", pos="390,30!"];

{"".join(s_edges)}
{"".join(fwd)}
{"".join(rev)}
}}
"""


def final_matching_board() -> str:
    return """digraph G {
  graph [bgcolor="white", pad=0.35, labelloc=t, fontsize=20, fontname="Helvetica", label="Final perfect matching from the lecture example"];
  node [shape=plain];
  t [label=<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="16">
      <TR><TD></TD><TD><B>b1</B></TD><TD><B>b2</B></TD><TD><B>b3</B></TD><TD><B>b4</B></TD></TR>
      <TR><TD><B>r1</B></TD><TD><B>X</B></TD><TD></TD><TD></TD><TD></TD></TR>
      <TR><TD><B>r2</B></TD><TD></TD><TD><B>X</B></TD><TD></TD><TD></TD></TR>
      <TR><TD><B>r3</B></TD><TD></TD><TD></TD><TD></TD><TD><B>X</B></TD></TR>
      <TR><TD><B>r4</B></TD><TD></TD><TD></TD><TD><B>X</B></TD><TD></TD></TR>
    </TABLE>
  >];
}
"""


def summary_table() -> str:
    return """digraph G {
  graph [bgcolor="white", pad=0.35, labelloc=t, fontsize=20, fontname="Helvetica", label="Lecture 9b Hungarian trace summary"];
  node [shape=plain];
  t [label=<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="8">
      <TR><TD><B>Step</B></TD><TD><B>Shortest alternating path</B></TD><TD><B>Distance</B></TD><TD><B>Matching after augment</B></TD></TR>
      <TR><TD>1</TD><TD>s -&gt; r4 -&gt; b4</TD><TD>1</TD><TD>{r4-b4}</TD></TR>
      <TR><TD>2</TD><TD>s -&gt; r1 -&gt; b1</TD><TD>0</TD><TD>{r1-b1, r4-b4}</TD></TR>
      <TR><TD>3</TD><TD>s -&gt; r3 -&gt; b4 -&gt; r4 -&gt; b3</TD><TD>0</TD><TD>{r1-b1, r3-b4, r4-b3}</TD></TR>
      <TR><TD>4</TD><TD>s -&gt; r2 -&gt; b2</TD><TD>0</TD><TD>{r1-b1, r2-b2, r3-b4, r4-b3}</TD></TR>
    </TABLE>
  >];
}
"""


def main() -> None:
    # Matrix states from lecture slides
    states = [
        ("step0_initial_matrix.dot", "Step 0: initial adjusted weights and zero heights", [0, 0, 0, 0], [0, 0, 0, 0],
         [["5", "9", "17", "21"], ["8", "12", "25", "18"], ["14", "23", "15", "6"], ["19", "16", "3", "1"]]),
        ("step1_after_first_matrix.dot", "Step 1: after matching r4-b4", [0, 0, 0, 0], [5, 9, 3, 1],
         [["0", "0", "14", "20"], ["3", "3", "22", "17"], ["9", "14", "12", "5"], ["14", "7", "0", "0"]]),
        ("step2_after_second_matrix.dot", "Step 2: after matching r1-b1 and r4-b4", [0, 0, 0, -5], [5, 9, 8, 6],
         [["0", "0", "9", "15"], ["3", "3", "17", "12"], ["9", "14", "7", "0"], ["19", "12", "0", "0"]]),
        ("step3_after_third_matrix.dot", "Step 3: after rerouting to match r3-b4 and r4-b3", [-3, 0, 0, -5], [8, 12, 8, 6],
         [["0", "0", "12", "18"], ["0", "0", "17", "12"], ["6", "11", "7", "0"], ["16", "9", "0", "0"]]),
    ]
    for filename, title, rh, bh, mat in states:
        path = ROOT / filename
        write(path, matrix_table(title, rh, bh, mat))
        render_dot(path)

    graphs = [
        ("step0_initial_graph.dot", "Step 0: shortest path is s -> r4 -> b4", ["0", "0", "0", "0"], ["5", "9", "3", "1"], [("s", "r4"), ("r4", "b4")], []),
        ("step1_after_first_graph.dot", "Step 1: shortest path is s -> r1 -> b1", ["0", "0", "0", "5"], ["0", "0", "5", "5"], [("s", "r1"), ("r1", "b1")], [("b4", "r4")]),
        ("step2_after_second_graph.dot", "Step 2: rerouting path is s -> r3 -> b4 -> r4 -> b3", ["3", "0", "0", "0"], ["3", "3", "0", "0"], [("s", "r3"), ("r3", "b4"), ("b4", "r4"), ("r4", "b3")], [("b1", "r1"), ("b4", "r4")]),
        ("step3_after_third_graph.dot", "Step 3: final augmenting path is s -> r2 -> b2", ["0", "0", "12", "12"], ["0", "0", "12", "12"], [("s", "r2"), ("r2", "b2")], [("b1", "r1"), ("b4", "r3"), ("b3", "r4")]),
    ]
    for filename, title, rd, bd, hi, matched in graphs:
        path = ROOT / filename
        write(path, state_graph(title, rd, bd, hi, matched))
        render_dot(path, "neato")

    final_path = ROOT / "step4_final_matching.dot"
    write(final_path, final_matching_board())
    render_dot(final_path)

    summary = ROOT / "summary_paths.dot"
    write(summary, summary_table())
    render_dot(summary)


if __name__ == "__main__":
    main()
