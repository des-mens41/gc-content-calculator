def calculate_gc_content(sequence):
    '''
    Calculate the GC content of a DNA sequence as a percentage.

    Parameters:
        sequence (str): A DNA sequence containing A, T, G, C bases.

    Returns:
        float: GC content percentage.
    
    '''
    sequence = sequence.upper()


    gc_count = 0
    for base in sequence:
        if base == 'G' or base == 'C':
            gc_count += 1
    total_length = len(sequence)
    if total_length == 0:
        return 0.0
    gc_percentage = (gc_count / total_length) * 100
    return(gc_percentage)

# Read DNA sequences from a file and print each one's GC content
with open('sample.txt', 'r') as file:
    for line in file:
        clean_line = line.strip()
        results = calculate_gc_content(clean_line)
        print(f"{clean_line} -> {results:.2f}%")
