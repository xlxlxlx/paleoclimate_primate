#########
# Input: protein sequences, 
#        genome and cds blastn reference databases 
#        (built from genome and cds sequences)
# Output: tblastn text results in seperate .tab files
#        (aligning protein to genome/cds) 
#########

import os
import subprocess
import random

# to queue tasks in batch
# not the best practice, can be improved
task_list = "tblastn_batch_task.txt"

# store all the protein sequence files in lists
filepath_denovo = "../protein_sequences_denovo/"
filepath_cgc = "../protein_sequences_cgc/"

protein_sequence_list_denovo = []
protein_sequence_list_cgc = []

for f in os.listdir(filepath_denovo):
    if not f.endswith(".fasta"):
        continue
    protein_id = f.split(".")[0]
    protein_sequence_list_denovo.append(protein_id)

for f in os.listdir(filepath_cgc):
    if not f.endswith(".fasta"):
        continue
    protein_id = f.split(".")[0]
    protein_sequence_list_cgc.append(protein_id)


list_denovo = protein_sequence_list_denovo1

# random 100 cgc genes
list_cgc = [x for x in protein_sequence_list_cgc if x not in list_denovo]
list_cgc = random.choices(list_cgc, k=100)


# store all the genome and cds database files in lists
filepath_ensembl = "../cds_ensembl/"
filepath_ncbi = "../cds_ncbi/"

cds_sequence_ensembl = {}
cds_sequence_ncbi = {}

for f in os.listdir(filepath_ensembl):
    print(f)
    if not f.endswith(".cds.all.fa"):
        continue
    species_name = f.split(".")[0]
    cds_sequence_ensembl[species_name] = f

for f in os.listdir(filepath_ncbi):
    print(f)
    if not f.endswith("cds_from_genomic.fna"):
        continue
    species_name = f.split(".")[0]
    cds_sequence_ncbi[species_name] = f

filepath_ensembl = "../genomes_ensembl/"
filepath_ncbi = "../genomes_ncbi/"

genome_sequence_ensembl = {}
genome_sequence_ncbi = {}

for f in os.listdir(filepath_ensembl):
    print(f)
    if not f.endswith(".dna_sm.toplevel.fa"):
        continue
    species_name = f.split(".")[0]
    genome_sequence_ensembl[species_name] = f

for f in os.listdir(filepath_ncbi):
    print(f)
    if not f.endswith("genomic.fna"):
        continue
    species_name = f.split(".")[0]
    genome_sequence_ncbi[species_name] = f


# queue tblastn jobs in batch
# cds
for protein in list_cgc:
    for species in cds_sequence_ncbi:
        species_db = cds_sequence_ncbi[species]
        task = f"../tools/blast/ncbi-blast-2.13.0+/bin/tblastn -db {species_db} -query ../protein_sequences_cgc/{protein}.fasta -outfmt '7 sscinames scomnames stitle qacc sacc pident length mismatch gapopens qstart qend sstart send evalue bitscore qcovs qcovhsp qseq sseq'  -out rst3_cds_ensembl_ncbi_cgc/{protein}_{species}_ncbi.tab"
        print(task)
        with open(task_list, 'w') as f:
            f.write(task)
        cmd = 'batch < ' + task_list
        os.system(cmd)
    for species in cds_sequence_ensembl:
        species_db = cds_sequence_ensembl[species]
        task = f"../tools/blast/ncbi-blast-2.13.0+/bin/tblastn -db {species_db} -query ../protein_sequences_cgc/{protein}.fasta  -outfmt '7 sscinames scomnames stitle qacc sacc pident length mismatch gapopens qstart qend sstart send evalue bitscore qcovs qcovhsp qseq sseq'  -out rst3_cds_ensembl_ncbi_cgc/{protein}_{species}_ensembl.tab"
        print(task)
        with open(task_list, 'w') as f:
            f.write(task)
        cmd = 'batch < ' + task_list
        os.system(cmd)

# whole genome
for protein in list_cgc:
    for species in genome_sequence_ensembl:
        species_db = genome_sequence_ensembl[species]
        task = f"../tools/blast/ncbi-blast-2.13.0+/bin/tblastn -db {species_db} -query ../protein_sequences_cgc/{protein}.fasta  -outfmt '7 sscinames scomnames stitle qacc sacc pident length mismatch gapopens qstart qend sstart send evalue bitscore qcovs qcovhsp qseq sseq'  -out rst3.1_genome_ensembl_ncbi_cgc2/{protein}_{species}_ensembl.tab"
        print(task)
        with open(task_list, 'w') as f:
            f.write(task)
        cmd = 'batch < ' + task_list
        os.system(cmd)
    for species in genome_sequence_ncbi:
        species_db = genome_sequence_ncbi[species]
        task = f"../tools/blast/ncbi-blast-2.13.0+/bin/tblastn -db {species_db} -query ../protein_sequences_cgc/{protein}.fasta -outfmt '7 sscinames scomnames stitle qacc sacc pident length mismatch gapopens qstart qend sstart send evalue bitscore qcovs qcovhsp qseq sseq'  -out rst3.1_genome_ensembl_ncbi_cgc2/{protein}_{species}_ncbi.tab"
        print(task)
        with open(task_list, 'w') as f:
            f.write(task)
        cmd = 'batch < ' + task_list
        os.system(cmd)

for protein in list_cgc:
    for species in genome_sequence_ensembl:
        species_db = genome_sequence_ensembl[species]
        task = f"../tools/blast/ncbi-blast-2.13.0+/bin/tblastn -db {species_db} -query ../protein_sequences_cgc/{protein}.fasta  -outfmt '7 sscinames scomnames stitle qacc sacc pident length mismatch gapopens qstart qend sstart send evalue bitscore qcovs qcovhsp qseq sseq'  -out rst3.2_genome_ensembl_ncbi_cgc2/{protein}_{species}_ensembl.tab"
        print(task)
        with open(task_list, 'w') as f:
            f.write(task)
        cmd = 'batch < ' + task_list
        os.system(cmd)
    for species in genome_sequence_ncbi:
        species_db = genome_sequence_ncbi[species]
        task = f"../tools/blast/ncbi-blast-2.13.0+/bin/tblastn -db {species_db} -query ../protein_sequences_cgc/{protein}.fasta -outfmt '7 sscinames scomnames stitle qacc sacc pident length mismatch gapopens qstart qend sstart send evalue bitscore qcovs qcovhsp qseq sseq'  -out rst3.2_genome_ensembl_ncbi_cgc2/{protein}_{species}_ncbi.tab"
        print(task)
        with open(task_list, 'w') as f:
            f.write(task)
        cmd = 'batch < ' + task_list
        os.system(cmd)
