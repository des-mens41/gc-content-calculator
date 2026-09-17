def calculate_gc_content(sequence):
    '''
    Calculate the GC content of a DNA sequence as a percentage.

    Parameters:
        sequence (str): A DNA sequence containing A, T, G, C bases.

    Returns:
        float: GC content rounded to 2 decimal places.
    
    '''
    gc_count = 0
    for base in sequence:
        if base == 'G':
            gc_count += 1
        elif base == "C":
            gc_count += 1
    total_length = len(sequence)
    gc_percentage = (gc_count / total_length) * 100
    return(round(gc_percentage, 2))
with open('sample.txt', 'r') as file:
    for line in file:
        clean_file = line.strip()
        results = calculate_gc_content(clean_file)
        print(clean_file, '=' , results, "%")
