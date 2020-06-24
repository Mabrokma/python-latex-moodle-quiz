import matplotlib.pyplot as plt
import numpy as np


def relation(a,b,funktion):
  i,t=1,set()
  while i<=b:
    if eval(funktion):
      t.add(i)
    i+=1
  return list(t)

def plot(a,what):
  alle_y,alle_x=[],[]
  for i in range(-(a+1),a+1):
    if what[0]==3 and i==0:
      i+=1
    if eval(what[1])==round(eval(what[1])):
          alle_x.append(i)
          alle_y.append(eval(what[1]))
  yunten = min(alle_y)-0.125
  yoben = max(alle_y)+0.125
  plt.figure(figsize=[9.5,6.5])
  plt.xticks(np.arange(-14, 14, step=2))
  i = np.arange(-12.125, 12.125, 0.01)
  s = eval(what[1])
  plt.plot(i,s)
  plt.plot(alle_x, alle_y,'o')
  plt.ylim(yunten,yoben)
  plt.xlim(-12.125,12.125)
  plt.grid(True, linestyle='--')
  plt.tight_layout()
  plt.savefig(pngfile,dpi=150,quality=95,transparent=True)
  return [alle_x,alle_y]

a=[[1,"i**3+i**2+1",r"x^3+x^2+1",r"$A=\mathbb{R},B=\mathbb{R}$",['','','','','*'],r"$A=\mathbb{Z},B=\mathbb{R}$",['','','*','',''],r"$A=\mathbb{R},B=\mathbb{Z}$",['*','','','','']],
  [2,"np.sqrt(abs(i))",r"\sqrt{|x|}",r"$A=\mathbb{R},B=\mathbb{R}^+_0$",['','','','*',''],r"$A=\mathbb{Z},B=\mathbb{R}^+$",['*','','','',''],r"$A=\mathbb{R}^+,B=\mathbb{R}^+$",['','','','','*']],
  [3,"i/abs(i)*np.sqrt(abs(i))",r"\frac{x}{|x|}\cdot \sqrt{|x|}",r"$A=\mathbb{R}\setminus\left\{0\right\},B=\mathbb{R}\setminus\left\{0\right\}$",['','','','','*'],r"$A=\mathbb{Z}\setminus\left\{0\right\},B=\mathbb{R}\setminus\left\{0\right\}$",['','','*','',''],r"$A=\mathbb{N},B=\mathbb{R}\setminus\left\{0\right\}$",['','','*','','']],
  [4,"np.floor(i)",r"f(x)=\lfloor x\rfloor$, d.h. der gr\"o\ss ten ganzen Zahl $\leq x",r"$A=\mathbb{R},B=\mathbb{R}$",['','*','','',''],r"$A=\mathbb{R},B=\mathbb{Z}$",['','','','*',''],r"$A=\mathbb{N},B=\mathbb{Z}$",['','','*','','']]
  ]


for x in a:
  pngfile='plot-fkt-'+str(x[0])+'.png'
  plot(12,x)
  print(rf"""\begin{{cloze}}[points=6]{{Funktion untersuchen ({x[0]})}}
  \textbf{{Aufgabe: Eigenschaften von Funktion}} \\ \\Gegeben ist folgende Zuordnung: $f:A \to B$ mit $x\mapsto {x[2]}$ f\"ur alle $x\in A$.\\ Im Bereich $-12\leq x\leq 12$ schaut ihr Graph wie folgt aus:\\  \includegraphics[width=10cm]{{{pngfile}}}  \\
  Entscheiden Sie anhand des Graphen, welche Eigenschaften die Zuordnung in Abh\"angigkeit von der Definitionsmenge $A$ und der Zielmenge $B$ jeweils hat.\\
  \begin{{multi}}[single]
  \\ (a) Die Zuordnung ist f\"ur {x[3]} \item {x[4][0]} keine \item {x[4][1]} eine \item {x[4][2]} eine injektive \item {x[4][3]} eine surjektive \item {x[4][4]} eine bijektive
  \end{{multi}} Funktion.\\
  \begin{{multi}}[single]
  (b) Die Zuordnung ist f\"ur {x[5]} \item {x[6][0]} keine \item {x[6][1]} eine \item {x[6][2]} eine injektive \item {x[6][3]} eine surjektive \item {x[6][4]} eine bijektive
  \end{{multi}} Funktion.\\
  \begin{{multi}}[single]
  \\ (c) Die Zuordnung ist f\"ur {x[7]} \item {x[8][0]} keine \item {x[8][1]} eine \item {x[8][2]} eine injektive \item {x[8][3]} eine surjektive \item {x[8][4]} eine bijektive
  \end{{multi}} Funktion.\\ \\ \emph{{Bitte notieren Sie Ihre Argumentation zu den Teilaufgaben. Sie sollen diese im Anschluss eingeben oder als Scan/Datei hochladen und im Pr\"ufungsgespr\"ach erl\"autern.}} \\
  \end{{cloze}} \newpage""")

