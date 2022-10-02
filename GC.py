from Bio import SeqIO


def compute_gc_percentage(sequence):
    gc_symbols = sequence.count('G') + sequence.count('C')
    return (gc_symbols / len(sequence)) * 100


records = list(SeqIO.parse("dataset.fasta", "fasta"))
highest_gc_id, highest_gc_percentage = None, 0

for record in records:
    percentage = compute_gc_percentage(record.seq)
    if percentage > highest_gc_percentage:
        highest_gc_percentage = percentage
        highest_gc_id = record.id

print(highest_gc_id)
print(highest_gc_percentage)
