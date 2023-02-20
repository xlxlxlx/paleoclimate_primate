#########
# Input: (1) a table storing number of cds/genome hits 
#            in each primate clade 
#            (output of divergence_time_clades_hits.py)
#        (2) climate66ma.csv table
# Output: a plot shows estimated gene frequency along with
#         global surface temperature in recent 66 million years
#########

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# this is the output of divergence_time_clades_hits.py
fn = "clades_gene_hits_0.8_dedup.csv"
df = pd.read_csv(fn)

fn2 = "climate66ma.csv"
df2 = pd.read_csv(fn2)

x_axis_list = list(np.linspace(0, 71, 142+1))

fig, ax=plt.subplots(figsize=(40, 20))

# Choices:
# (1) Plot all cds results
ax.plot(df.divergence_time, df.count_all_cds, marker="o", color="#7E2F8E")

# (2) Plot cgc and denovo results separately
# (3) Replace "cds" with "genome" to plot results for whole genome
# ax.plot(df.divergence_time, df.count_denovo_cds, marker="o", color="red")
# ax.plot(df.divergence_time, df.count_cds_cgc, marker="o", linestyle='--', linewidth=2, color="green", alpha=0.8)

ax.set_ylim(ymin=0)
# ax.set_ylim(ymax=15)
ax.set_yticks(range(0, 20, 1))
ax.set_xlabel("divergence_time", fontsize=20)
ax.set_ylabel("# Emerged Gene (estimated)", fontsize=20)
ax.legend([])
ax.tick_params(axis='x', which='both', labelsize=18)
ax.tick_params(axis='y', which='both', labelsize=18)
ax.invert_xaxis()

ax2 = ax.twinx()
ax2.set_xticks(range(0, 71, 1))
# x_axis_list2 = list(np.linspace(0, 71, 71+1))
# ax2.set_xticks(x_axis_list2)
ax2.set_yticks(range(8, 31, 1))
ax2.set_xlabel("Time (Mya)", fontsize=20)
ax2.set_ylabel("Surface Temperature (°C)", fontsize=20)
ax2.legend([])
ax2.tick_params(axis='x', which='both', labelsize=18)
ax2.tick_params(axis='y', which='both', labelsize=18)

ax2.set_ylim(ymin=8)

for (tickvalue, ticklbl) in zip(x_axis_list2, ax.xaxis.get_ticklabels()):
    ticklbl.set_color('blue' if tickvalue % 5 == 0 else 'black')
# ax2.invert_xaxis()

# plot temperature curve
ax2.plot(df2['Time delta_18O(Myr BP)'], df2['Ts(C)'], alpha = 0.5)

plt.show()
