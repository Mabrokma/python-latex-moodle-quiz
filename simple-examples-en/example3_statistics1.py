import matplotlib.pyplot as plt
import random

def drawpie(names,percentages):
  labels = names
  sizes = percentages
  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, labels=labels, startangle=90, textprops={'fontsize': 14})
  ax1.axis('equal')
  plt.savefig(pngfile,dpi=150,quality=95,transparent=True)
  return

for x in range(0,10):
  pets=['Hamster', 'Cat', 'Dog', 'Parakeet']
  pngfile='piechart-'+str(x)+'.png'
  a=random.randint(4,8)
  b=random.randint(0,3)
  values=[15+a,30-a,45-b,10+b]
  random.shuffle(values)
  drawpie(pets,values)
  print(rf"""
  \begin{{shortanswer}}{{Pie Chart of Pets ({x+1})}}
  \textbf{{Share of Pets in a School Class}}\\The following pie chart shows the share of pets in a particular school class:\\
  \includegraphics[width=9cm]{{{pngfile}}}\\
  Which pet occurs with a share of ${values[b]}\,\%\,$?
  \item {pets[b]}
  \end{{shortanswer}}""")
  if x%2==1 and x<9:
    print(r"\newpage")

