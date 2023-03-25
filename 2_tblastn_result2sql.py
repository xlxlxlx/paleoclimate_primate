#########
# This script stores tblastn results in SQLite database
#
# Input: tblastn results in .tab files
# Output: SQLite database table storing results
#         (the table needs to be created beforehand)
#########

import os
import sqlite3
import numbers

con = sqlite3.connect('climate_primate.db')
cur = con.cursor()

# if there are too many hits in whole genome, 
# take first k that pass the threshold
#
# this handles the case where there are too 
# many findings to go through
line_limit_per_f = 1

# thresholds for both percentage_identity and percentage_query_coverage
# can be separated if needed
filter_thre = 80

# genome or cds
sequence_type = "cds" 
# denovo or cgc
protein_type = "cgc"

filepath = f"../rst_tblastn/"+f"rst_{sequence_type}_ensembl_ncbi_{protein_type}/"
table_name = f"protein_primate_species_{sequence_type}_{protein_type}_thre{filter_thre}"

for f in os.listdir(filepath):
    print(f)
    if not f.endswith(".tab"):
        continue
    f_values = [f[:-4].split("_")[0]]
    line_count = 0
    with open(filepath+f,'r') as f_open:
        for line in f_open:
            if line_count >= line_limit_per_f:
                break
            if line.startswith("#"):
                continue   
            line_values_list = f_values+line.split('\n')[0].split("\t")
            line_values_list = [x.replace("'","") for x in line_values_list]
            # filter result entries based on thresholds
            if int(line_values_list[-4]) < filter_thre or int(line_values_list[7]) < filter_thre:
                continue
            line_values = ','.join(x if x.isdigit() or x.replace('.', '', 1).isdigit() else "'{0}'".format(x) for x in line_values_list) 
            print(line_values)   
            line_count += 1
            cur.execute(f"INSERT OR IGNORE INTO {table_name} VALUES ({line_values})")
            con.commit()
            
