# GC Content Calculator

A lightweight Python utility designed to analyze DNA sequences from text files and calculate their GC content percentage. 

GC content is a fundamental metric in molecular biology and bioinformatics. It affects the stability of DNA molecules (since G-C pairs form three hydrogen bonds versus two for A-T, lending high-GC regions more thermal stability). It is widely used in primer design for PCR, and tracking variations between species and genomic regions.

## How It Works
1. Reads DNA sequences line-by-line from a text file (`sample.txt`).
2. Cleans inputs automatically by stripping trailing whitespaces or hidden newline characters (`\n`).
3. Normalizes Case to seamlessly handle both uppercase and lowercase DNA strings.
4. Calculates & Formats the exact GC ratio, cleanly printing results to 2 decimal places.

## Example output
ATGCGTACG -> 55.56 %
GGCCAATTT -> 44.44 %
TTTAAACGC -> 33.33 %

## How to Run
1. Ensure you have your target sequences inside a file named sample.txt in the same directory.
2. Run the script from your terminal:
python gc_calculator.py