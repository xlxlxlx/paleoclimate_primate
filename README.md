# Towards Understanding Paleoclimate Impacts on Primate De Novo Genes

This is a repository storing data and scripts used in our manuscript titled "Towards Understanding Paleoclimate Impacts on Primate De Novo Genes".

# Data files
- uniprot_cgc.tsv   
The UniProt ID mapping [^1] result for the original 733 cancer associated genes obtained from Cancer Gene Census [^2]. Note that this table contains both reviewed and unreviewed proteins. 

- denovo_literature_gene_protein_list.xlsx    
The de novo genes obtained from literature and used in this study

- cgc_random100_gene_protein_list.xlsx    
The random 100 genes and their corresponding proteins used in this study

- genome_accession.xlsx    
The genome accession numbers for the 32 primate genomes used in this study


# Runn the scripts
Run the scripts in the order in filenames:
- 1_tblastn_genome_cds.py    
Align protein sequence to genome or CDS sequence

- 2_tblastn_result2sql.py    
Input the aligning results into a relational database

- 3_tblastn_summary_thre.py   
Summarize the aligning result into a gene x species matrix

- 4_divergence_time_clades_hits.py    
Estimate gene emergence time based on divergence time of primate clades   

- 5_climate_66ma_plot.py   
Generate time-dependent distribution plot for gene emergence time    

- 6_climate_interval_plots.py   
Generate zoomed in temperature curve plots for each clade divergence time and range


In addition: 
- climate_primate.sql    
The database table creation file when a new table is needed

# Input data for scripts
Input files needed for the scripts are under `input_data/`.   
`clades_divergence_time.csv` and `divergence_time.csv` are derived from TimeTree database [^3]. `climate66ma` is obtained from Hansen et al. [^4]. 

[^1]: "UniProt: the universal protein knowledgebase in 2021." Nucleic acids research 49, no. D1 (2021): D480-D489.
[^2]: Sondka, Zbyslaw, et al. "The COSMIC Cancer Gene Census: describing genetic dysfunction across all human cancers." Nature Reviews Cancer 18.11 (2018): 696-705.
[^3]: Kumar, Sudhir, et al. "TimeTree 5: An expanded resource for species divergence times." Molecular Biology and Evolution 39.8 (2022): msac174.
[^4]: Hansen, James, et al. "Climate sensitivity, sea level and atmospheric carbon dioxide." Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 371.2001 (2013): 20120294.


