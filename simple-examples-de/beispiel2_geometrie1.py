auswahl=[
  ['Trapez','ein Paar paralleler Seiten'],
  ['Parallelogramm',r'gegen\"uberliegende Seiten sind parallel'],
  ['Rechteck','hat drei rechte Winkel'],
  ['Raute','alle Seiten gleich lang'],
  ['Deltoid','eine Diagonale ist Symmetrieachse'],
  ['Quadrat','Rechteck, das eine Raute ist']]
for x in auswahl:
  print(rf"""\begin{{essay}}[points=2, response format=html]{{Vierecke definieren ({x[0]})}}
  Definiere den Begriff: {x[0]}
  \item {x[1]}
  \end{{essay}}""")

