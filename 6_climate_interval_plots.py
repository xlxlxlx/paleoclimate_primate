#########
# Input: (1) divergence_time.csv table
#        (2) climate66mya.csv table
# Output: separate zoomed in plots showing estimated 
#         divergence time and range for primate clades 
#         along with global surface temperature curve
#########

import pandas as pd
import numpy as np
import matplotlib

# how much space to visually show before and after 
# the clade divergence range
range_multiplier = 0.5

# global surface temperature data in recent 66 million years
fn = "climate66ma.csv"
df = pd.read_csv(fn)

# this table is less detailed than clades_divergence_time.csv
# can be replaced by this file if also change the row.tolist() line
df_divergence = pd.read_csv("divergence_time.csv")
df_divergence.columns.values.tolist()

for index, row in df_divergence.iterrows():
    print(row.tolist())
    divergence_time, range_start, range_end, right_ranch_first_species, left_branch_species, right_branch_species, name, rank = row.tolist()
    
    # adjust visual x-axis range based on range_multiplier
    real_extended_start = range_start - range_multiplier*(range_end - range_start)
    extended_start = max(real_extended_start, 0)
    
    real_extended_end = range_end + range_multiplier*(range_end - range_start)
    # show the plot up to 72 Ma
    extended_end = min(real_extended_end, 72)
    
    # adjust visual x-axis range based on divergence range
    axis_multiplier = 1
    if (real_extended_end - real_extended_start) <= 15:
        axis_multiplier = 2
    if (real_extended_end - real_extended_start) <= 8:
        axis_multiplier = 4
    print(real_extended_start, real_extended_end, axis_multiplier)
    x_axis_list = list(np.linspace(0, 71, (71*axis_multiplier)+1))

    max_temp = df[(df["Time delta_18O(Myr BP)"] > extended_start) & (df["Time delta_18O(Myr BP)"] < extended_end)]['Ts(C)'].max()
    max_temp = int(max_temp) + 1
    min_temp = df[(df["Time delta_18O(Myr BP)"] > range_start) & (df["Time delta_18O(Myr BP)"] < range_end)]['Ts(C)'].min()
    min_temp = int(min_temp)

    ax = df.plot.line('Time delta_18O(Myr BP)', 'Ts(C)', figsize=(40, 20))
    # ax.set_xticks(range(0, 71, 1))
    ax.set_xticks(x_axis_list)
    ax.set_yticks(range(8, 31, 1))
    ax.set_xlabel("Time (Mya)", fontsize=40)
    ax.set_ylabel("Surface Temperature (°C)", fontsize=40)
    ax.legend([])
    ax.tick_params(axis='x', which='both', labelsize=32)
    ax.tick_params(axis='y', which='both', labelsize=32)

    for (tickvalue, ticklbl) in zip(x_axis_list, ax.xaxis.get_ticklabels()):
        ticklbl.set_color('blue' if tickvalue % 5 == 0 else 'black')

    ax.axvline(divergence_time, color='green', linestyle='--') 
    ax.axvspan(range_start, range_end, alpha=0.5, color='lightgreen')

    ax.set_xlim([extended_start, max(extended_start+2, extended_end)])
    # use fixed y axis range to make figures comparable
    ax.set_ylim([15, 25])
    # ax.set_ylim([min_temp, max(min_temp+5, max_temp)])
    ax.invert_xaxis()

    # add clade name, clade size and range multiplier 
    # to the result plot
    plot_name = f"figure_intervals/{divergence_time}_"
    if isinstance(name, str) and isinstance(rank, str):
        plot_name += name + "_" + rank
    else:
        plot_name += "noname" + "_" + right_ranch_first_species + "_size" + str(right_branch_species + left_branch_species)
        
    plot_name += f"_extend{range_multiplier}.png"

    ax.figure.savefig(plot_name)