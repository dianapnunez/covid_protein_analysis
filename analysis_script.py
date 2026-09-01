# Adapted from the JCharisTech (Jesse E. Agbe) tutorial
from Bio import SeqIO

#load the file from our data subdirectory
# for record in SeqIO.parse("data/sequence.fasta", "fasta"):
#    print(record)

#begin analysis
cov_record = SeqIO.read("data/sequence.fasta", "fasta")
print(cov_record)

cov_dna = cov_record.seq
print(f"\nCovid DNA: {cov_dna}")

#sequence length
len(cov_dna)
print(f"DNA length: {len(cov_dna)}")

#transcription
cov_mrna = cov_dna.transcribe()
print(f"mRNA Sequence: {cov_mrna}")

#translation
cov_protein = cov_mrna.translate()
print(f"Protein Sequence: {cov_protein}")

print(f"Length of protein sequence: {len(cov_protein)}")

#split amino acids by stop codons *
cov_aa = cov_protein.split("*")

#clean the sequences by casting them to strings
cov_clean = [str(i) for i in cov_aa if i]

import pandas as pd

#pass the split list into the dataframe
df= pd.DataFrame({'amino_acid_chains': cov_clean})
print(df)

#calculating character length of the amino acid chains
df['count'] = df['amino_acid_chains'].str.len()
print(df.head())

#largest sequence before "*" stop codon
df.nlargest(10, "count")
print(df.nlargest(10, "count"))

#count amino acid frequency
from collections import Counter
print(f"\nThe 10 most common amino acids: {Counter(cov_protein).most_common(10)}")
