# article-filename.py

This is a simple program that takes a PubMed link and produces a filename as 
output. This filename is formatted as follows:

If there is only one author the filename is `lastname_year_article title.pdf`

Example:

`Feynman_1974_Structure of the proton.pdf`

If there are two authors the filename is `lastname1&lastname2_year_article title.pdf`

Example:

`Watson&Crick_1953_Molecular structure of nucleic acids; a structure for deoxyribose nucleic acid.pdf`

If there are more than two authors the filename is `lastname-et-al_year_article title.pdf`

Example:

`Cowan-et-al_1956_Detection of the Free Neutrino: a Confirmation.pdf`

This program is written in Python3 and depends on the following packages:

- bs4
- pyperclip
- requests

You can install them with:

```bash
$ pip install beautifulsoup4
$ pip install pyperclip
$ pip install requests
```

If you are using Linux, you will need to install an additional package in order 
to get `pyperclip` working. To install this package just run the following line:

```bash
$ sudo apt install xclip
```