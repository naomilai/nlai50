Naomi Lai
peaches & mangoes
SoftDev
K11 -- flask static
2024-09-25
time spent: 0.5

DISCO:
- accessing foo (plaintext) via http://localhost:5000/static/foo.html leads to webpage displaying contents of foo.html (Is this plaintext, though?)
- http://localhost:5000/static/fixie.html

QCC:
- <!DOCTYPE html> to set up html file
- dir name "static"

INVESTIGATIVE APPROACH
- copy foo.html -> fixie.html and change contents to requirements for fixie
- head to http://localhost:5000/static/fixie.html instead of http://localhost:5000/static/foo.html