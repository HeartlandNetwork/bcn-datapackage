
# QC_bcn_dataset.py
# -----------------

# Initial QC from dataset sent from Cornell Lab


import pandas as pd
import matplotlib.pyplot as plt

#plt.figure(figsize=(10, 6))

# Set option to display all columns 

# Set options to display all rows and columns 
#pd.set_option('display.max_rows', None) 
#pd.set_option('display.max_columns', None)


df = pd.read_csv("BCN_eBird_data_20241004.csv", low_memory=False)

df

# Do you want to remove observer names and preserve user_ids?

df.dtypes

#  text (object) ----------------------------------

print(df['sub_id'].unique())

df['group_id'].unique() 

df['proj_id'].unique() 

df['obs_id'].unique() 

df['primary_com_name'].unique() 

df['orig_species_code'].unique() 

df['report_as'].unique() 

df['obs_comments'].unique() 

df['group_id.1'].unique() 

df['protocol_id'].unique() 

df['loc_id'].unique() 

df['name'].unique() 

df['subnational2_code'].unique() 

df['subnational1_code'].unique() 

df['user_id'].unique() 

df['sub_comments'].unique() 

df['obs_dt'].unique() 

df['checklist_id'].unique() 

# Date / time (object) -----------------------

df['obs_dt'].unique() 


# true / false --------------------------

df['all_obs_reported'].unique() 

df['obs_time_valid'].unique() 

df['valid'].unique()  

df['reviewed'].unique() 

df['reviewed'].unique()

df['is_birding_hotspot'].unique()

df['all_obs_reported'].unique() 

df['obs_time_valid'].unique() 

# integer -----------------------

df['how_many_atleast'].unique() 

df['how_many_atmost'].unique()


# float - continous histograms - matplotlib ---------------------

df['duration_hrs'].unique() 

df['duration_hrs'].plot(kind='hist', bins=100, color='skyblue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()


df['num_observers'].unique() 

df['num_observers'].plot(kind='hist', bins=100, color='skyblue', edgecolor='black')
plt.xlabel('No. Observers')
plt.ylabel('Frequency')
plt.show()

df['effort_distance_km'].unique() 

df['effort_distance_km'].plot(kind='hist', bins=100, color='skyblue', edgecolor='black')
plt.xlabel('distance km')
plt.ylabel('Frequency')
plt.show()

df['effort_area_ha'].unique() 

df['effort_area_ha'].plot(kind='hist', bins=100, color='skyblue', edgecolor='black')
plt.xlabel('area ha')
plt.ylabel('Frequency')
plt.show()

# spatial - x, y plots and Power BI map

df['latitude'].unique() 

df['longitude'].unique() 


plt.plot(df['longitude'], df['latitude'], marker='o', linestyle='-', color='b') 
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.show()





