with open("functions-moodle.xml", "rt") as fin:
    with open("funktions-shuffled-moodle.xml", "wt") as fout:
        for line in fin:
            fout.write(line.replace('{multi}CHOICE:', '{multi}CHOICE_S:'))

