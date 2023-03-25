#########
# Input: tblastn result database table
# Output: table with species as rows, genes as columns, 
#         gene existence status in species as values
#########

import os
import sqlite3
import pandas as pd

# thresholds
filter_thre = 80
# genome or cds
sequence_type = "cds" 
# denovo or cgc
protein_type = "cgc"

column_names = ["protein",
                "subject_sci_names",
                "subject_com_names",
                "subject_title",
                "query_accuracy",
                "subject_accuracy",
                "percentage_identity",
                "alignment_length",
                "mismatches",
                "query_start",
                "query_end",
                "sequence_start",
                "sequence_end",
                "e_value",
                "bit_score",
                "percentage_query_coverage_per_subject",
                "percentage_query_coverage_per_hsp",
                "qseq",
                "sseq"
               ]

protein_sequence_list_denovo = [
    "Q9NXD8","Q6ZSS4","Q86TU6","Q8N964","Q96MQ0","Q8N2B8","P0CZ25","O15544","Q6ZNZ3","Q8IZY5","Q8N446","Q0IIN9","P40205","D6REC4","P0C5J1","Q9BRP9","P08172","Q8NEM0","Q96EZ4","Q9GZY1","Q9H693","P04233","P07951","A0A024R1L7","Q9H1L0","Q96MZ4","O75044","Q3Y452","P31941","P06731","P40199","Q8WZ02","Q494W8","Q71RD9","Q9H669","Q7Z3S9","Q107X0","Q8NBC4","A0A024R0A3","P36269","Q8NBG7","Q6ZU27","Q8NFR3","Q9BR46","Q8N2X6","P56555","Q9H6Y8","Q6RUI8","Q6ZTI0","Q6ZVB9","P86434","Q6ZR03","P50991","Q96NU5","O43295","Q86UQ5","P24001","Q8N204","Q5K131","Q9H5F7","B3KNC5","Q3KRB8","Q7L8T7","Q6ZUY4","Q1W209","P58512","Q96NC1","Q8IZP1"
    ]

protein_sequence_list_cgc = [
    "P49915","Q6DJT9","Q86SG4","Q8NG31","Q14683","P16455","P29350","Q04721","Q9BYW2","P33076","O14980","Q99835","Q8TF68","O94992","P14373","P47813","P84243","P07949","Q7KZF4","P06400","P21802","P51826","Q9Y618","P36507","P23246","P04626","Q70Z35","P40259","Q9NRR4","Q15375","P40189","Q13485","O15164","P51679","Q13015","P49815","P29320","P04637","Q969V6","Q13765","P51825","O14522","Q02223","P68402","P20848","O75943","P40818","Q9HCK4","Q9UJQ4","O60934","Q96RU3","P55287","P31151","Q9Y2W1","Q9Y3A5","P11802","Q5JWF2","O95467","P41161","P56279","Q9UPS6","Q9P0J6","Q9HBE5","Q92570","P11912","P40238","O95573","Q9Y5J3","Q8WXI7","P10275","Q92889","Q14832","Q13492","P21359","P12931","P04198","Q9UPY3","P42680","Q93063","Q16665","P49792","Q9NQ94","P23193","P37173","O95071","Q9NZQ3","P0DTU4","P17542","P08151","Q06124","P36888","P43246","P29992","Q13017","Q9Y6N8","P08575","Q9NRL2","O14497","P31271","P49589"
    ]

primate_species = [
    'Saimiri boliviensis boliviensis', 'Theropithecus gelada', 'Aotus nancymaae', 'Callithrix jacchus', 'Carlito syrichta', 'Cebus capucinus', 'Cercocebus atys', 'Chlorocebus sabaeus', 'Colobus angolensis palliatus', 'Gorilla gorilla', 'Homo sapiens', 'Macaca fascicularis', 'Macaca mulatta', 'Macaca nemestrina', 'Mandrillus leucophaeus', 'Microcebus murinus', 'Nomascus leucogenys', 'Otolemur garnettii', 'Pan paniscus', 'Pan troglodytes', 'Papio anubis', 'Piliocolobus tephrosceles', 'Pongo abelii', 'Prolemur simus', 'Propithecus coquereli', 'Rhinopithecus bieti', 'Rhinopithecus roxellana', 'Cebus imitator', 'Hylobates moloch', 'Lemur catta', 'Sapajus apella', 'Trachypithecus francoisi'
    ]

con = sqlite3.connect('climate_primate.db')
cur = con.cursor()

protein_sequence_list = eval(f"protein_sequence_list_{protein_type}")

identity_threshold = coverage_threshold = filter_thre
table_name = f"protein_primate_species_{sequence_type}_{protein_type}_thre{filter_thre}"

query_cmd = f"select * from {table_name} where Percentage_identity > {identity_threshold} and percentage_query_coverage_per_subject > {coverage_threshold}"

rst = cur.execute(query_cmd)

df = pd.DataFrame(rst.fetchall())
df.columns = column_names

# make blank cells visually obvious
df_result = pd.DataFrame(columns = protein_sequence_list, index = primate_species).fillna(' ')

for index, row in df.iterrows():
    protein = row['protein']
    species = row['subject_sci_names']    
    df_result.loc[species, protein] = row['subject_title']

df_result.to_csv(f'tblastn_summary_id{identity_threshold}_cover{coverage_threshold}_{sequence_type}_{protein_type}.csv')    
