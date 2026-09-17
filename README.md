# GC Content Calculator

A Python tool that reads DNA sequences from a file and calculates the GC content (percentage of guanine and cytosine bases) for each one.

## Why GC content matters

GC content is a fundamental metric in molecular biology and bioinformatics. It affects DNA stability (G-C base pairs form three hydrogen bonds versus two for A-T, making high-GC regions more thermally stable), is used in primer design for PCR, and varies characteristically between species and genome regions, making it useful for genome comparison and identification.

## How it works

1. Reads DNA sequences line by line from sample.txt
2. For each sequence, counts the number of G and C bases
3. Calculates the percentage: (GC count / total length) × 100
4. Prints the result for each sequence, rounded to 2 decimal places

## Example output
ATGCGTACG = 55.56 %
GGCCAATTT = 44.44 %
TTTAAACGC = 33.33 %

## Usage

1. Add your DNA sequences to sample.txt, one sequence per line
2. Run the script:
python gc_calculator.py

## What I learned building this

This was my first Python project, built while learning fundamentals: variables, string indexing, loops, conditionals, functions, and file handling. It taught me the difference between print() and return, and the importance of testing code by predicting output before running it.

## Next steps

Planned improvements: handling FASTA-format files, adding reverse complement and translation features, and exporting results with pandas.