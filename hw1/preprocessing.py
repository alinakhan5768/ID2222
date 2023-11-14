import csv

with open('dataset/drugsComTest_raw.tsv', 'r') as input, open('output.txt', 'w') as output:
    reader = csv.reader(input, delimiter='\n')
    next(reader)  # Skip the header row
    for row in reader:
        if (len(row) == 0): continue
        if (len(row[0].split('"""')) != 3): continue
        review: str = row[0].split('"""')[1]
        output.write(f"{review}\n")