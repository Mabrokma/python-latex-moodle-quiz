# python-latex-moodle-quiz

Hier finden Sie einige Beispiele/Vorlagen zur Batch-Erzeugung parametrisierter Fragen (inklusive Lückentext- und Freitext-Fragen) für die Test-Aktivität in Moodle, die die Paketen`moodle` und `python` für LaTeX nutzen.

[Switch to the English version of this README](https://github.com/avohns/python-latex-moodle-quiz)

Voraussetzungen
===============

1. Eine lauffähige LaTeX-Installation
1. Eine lauffähige Installation von Python (>=3.6)
1. Die folgenden Pakete müssen für LaTeX installiert sein:
   1. `moodle` see https://ctan.org/pkg/moodle
   1. `python` see https://github.com/brotchie/python-sty
1. Wenn Sie in irgendeiner Art Bilder (statisch, dynamisch) einbinden wollen, dann benötigen Sie eine lauffähige Installation von [ImageMagick](https://imagemagick.org/index.php).
   
Benutzung/Workflow
==================

Die Ordner `simple-examples-ger` und `simple-examples-eng` enthalten einfache Demonstrationen/Minimalbeispiele (in englischer bzw. deutscher Sprache), die `àdvanced-examples-`-Ordner enthalten einige praktisch in meiner Tätgkeit in der Mathematiklehrerbildung eingesetzte Fallbeispiele.

1. Machen Sie sich mit der Dokumentation des Paketes `moodle` vertraut, die Sie [hier](http://mirrors.ctan.org/macros/latex/contrib/moodle/moodle.pdf) finden können.
1. Öffnen und bearbeiten Sie eines der TeX-Beispieldokumente in ihrem bevorzugten LaTeX-Editor.
1. Kompilieren Sie die Datei mit `pdflatex`.
1. Sie erhalten als Ergebnis eine intermediäre .py-Datei, eine .pdf-Datei und eine -moodle.xml Datei (und je nach Beispiel u.U. auch noch einige .png-Dateien). Für den Import nach Moodle benötigen Sie allerdings nur die -moodle.xml Datei.
1. Importieren Sie die -moodle.xml Datei in Ihre Fragensammlung in Moodle. Falls nicht anders angegeben, werden alle Fragen automatisch in eine neue Kategorie importiert, deren Name mit dem Titel des Quizzes in der .tex-Datei übereinstimmt.
1. Create a quiz activity and choose a random question from the respective category.

Wie das Ganze funktioniert
==========================

Die grundlegende Struktur aller Beispiele schaut in etwas so aus:

1. Wir haben eine gewöhnliche LaTeX Datei mit Header und Body.
1. Im Header sollten die beiden genannten Pakete aufgerufen werden, zusätzlich noch das T1 Font-Encoding, falls Sie rohes HTML in die Datei schreiben wollen (s. unten):
    ```latex 
    \usepackage[T1]{fontenc}
    \usepackage{moodle}
    \usepackage{python}
    ```
1. Innerhalb des Bodys haben wir eine `quiz`-Umgebung (s. Beispiel unten), welche beim Kompilieren mit `pdflatex` durch das `moodle`-Paket interpretiert wird und neben der gewohnten .pdf-Datei zusätzlich eine -moodle.xml-Datei erzeugt.
    ```latex
    \begin{quiz}{quiz title}
      ...
    \end{quiz}
    ```
1. Die `quiz`-Umgebung enthät ihrerseits eine `python`-Umgebung, die wenigstens eine zentrale `for`-Schleife enthält (s. Beispiel unten). Sobald `pdflatex` aufgerufen wird, ruft dieses nun seinerseits Python auf, welches mehrfach durch die `for`-Schleife iteriert und dabei in jeder Iteration dynamisch ein Stück LaTeX-Code ergänzt, das dann wieder durch `pdflatex`interpretiert und in die .pdf- und -moodle.xml-Datei integriert wird.
    ```latex
    \begin{python}
    for x in range(2,10):
      ...
    \end{python}
    ```
1. Die `for`-Schleife enthält wenigstens einen `print`-Befehl mit einem Multiline-f-String, der wenigstens eine Fragenumgebung enthält (Multiple-Choice, Numerisch (s. Beispiel unten), Kurzantwort, Freitext, Zuordnung, Lückentext (Cloze), vgl. Abschnitt 3 der Dokumentation des `moodle`-Paketes für weitere Details). 
    ```python
    print(rf"""\begin{{numerical}}
      ${x} + {y} =$
      \item {x+y} 
    \end{{numerical}}""")
    ```
1. Jede der Fragen enthält einige Variablen (z.B. `x`und `y`im Beispiel oben), für welche mit jedem Durchlauf der `for`-Schleife verschiedene Werte eingesetzt werden, was mit jedem Durchlauf eine neue Frage erzeugt.

Known Limitations
=================

Restrictions on interpreted LaTeX commands
------------------------------------------

The set of LaTeX commands getting converted to HTML and included in the resulting -moodle.xml file is limited (please refer to section 4 of the `moodle` package documentation for details). 

If you want to use additional HTML for layout purposes (e.g. lists or tables), you can include raw HTML inside your LaTeX document. Unfortunately, the raw HTML code will also be visible in the resulting PDF document.

Graphics
--------

It is both possible to include static images and to create images dynamically using `python` (even tikZ may be invoked). Any images included will be converted into .png files, which in turn are base64 encoded and directly included into the -moodle.xml file during compilation. 

You should specify the image dimensions (width, height in either cm or inch) and the conversion depends on a dpi setting (if not defined specifically, 103 dpi will be used as a default). Please refer to section 5 of the `moodle` package documentation for more details. 

In my experience, it is advisable to strictly stick to png files, as the conversion via ImageMagick implemented by the `moodle` package is a bit prone to errors.

Encoding/Umlauts
----------------

The `moodle` package does not play nicely with utf8 text encoding, when e.g. writing examples in German, you will need to write umlauts (Ä, Ö, Ü, ä, ö, ü, ß) in code (`\"A, \"O, \"U, \"a, \"o, \"u und \ss{}`).


Shuffling answers in embedded questions
---------------------------------------

The `moodle` package was written before shuffling answers was introduced for subquestions inside embedded questions in moodle (>= 3.0). 

If you want to use shuffled answers for subquestions inside embedded questions, you have to include another `python` environment below the `quiz` environment inside the TeX document's body to change the questions type directly within the -moodle.xml file (please refer to https://bit.ly/2ZbQnTB for more details on the different types of subquestions). 

Let us suppose our xml file is e.g. `example-moodle.xml`and we have a `MULICHOICE` question, we then need to change each occurence of `MULICHOICE` to `MULTICHOICE_S`, which can be achieved with the following bit of code:

```python
with open("example-moodle.xml", "rt") as fin:
  with open("example-shuffled-moodle.xml", "wt") as fout:
    for line in fin:
      fout.write(line.replace('MULTICHOICE:', 'MULTICHOICE_S:'))
```

Limitations inherited from the usable question types
----------------------------------------------------

As the `moodle` package only uses standard moodle question types, the generated questions should be useable on any moodle installation, there are no additional plugins required whatsoever (the MathML filter should be set to active in your moodle installation if you want to display formulas written in TeX code).

These question types come with their own set of limitations. For STEM subjects you might want to check answers for algebraic equivalence, which is simply not possible with these question types. You might want to check out the [STACK](https://moodle.org/plugins/qtype_stack) or [WIRIS](https://moodle.org/plugins/view.php?id=26) plugins for such purposes.


