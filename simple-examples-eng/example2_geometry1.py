auswahl=[
  ['Trapezoid','(at least) one pair of parallel sides'],
  ['Parallelogram','opposite sides are parallel'],
  ['Rectangle','has three right angles'],
  ['Rhombus','four sides of equal length'],
  ['Deltoid','one diagonal is an axis of symmetry'],
  ['Square','a rectangle, which is also a rhombus']]
for x in auswahl:
  print(rf"""\begin{{essay}}[points=2, response format=html]{{Quadliteral Definitions ({x[0]})}}
  Give a definition of the following type of quadliteral: {x[0]}
  \item {x[1]}
  \end{{essay}}""")

