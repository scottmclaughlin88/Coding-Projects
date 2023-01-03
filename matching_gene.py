
gene = 'acgta'
dna = 'assldfsalkdfacgtahcduotaccacghsdoacgtattufhaaawaeladacgtaskfhalskdhflkacgta123123'

#Write a function that will  find the number of occurances of the given gene in the given DNA.

def gene_occurances(gene, dna):
    occurances = 0
    occurances = dna.count(gene)
    return occurances

# answer = gene_occurances(gene, dna)
# print(answer)


#Write a function that finds the index of each occurance of the given gene in the given DNA.

def gene_locations(gene, dna):
    locations = []
    start = 0
    stop = len(dna)
    for x in range(gene_occurances(gene, dna)):
        location = dna.index(gene, start, stop)
        start = location + 1
        locations.append(location)
    return locations

answer = gene_locations(gene, dna)
print(answer)

#write a function that returns the DNA between two occurances of the given gene.
# def gene_

def get_sequence_between_genes(gene, dna):
    gene_locs = gene_locations(gene, dna)
    
    results = []
    for x in range(gene_occurances(gene, dna) -1):
        result = ''
        for letter in range(gene_locs[x] + len(gene) , gene_locs[x + 1]):
            result += dna[letter]
        results.append(result)
    return results

result = get_sequence_between_genes(gene, dna)
print(result)

#