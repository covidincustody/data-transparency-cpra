# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 15:46:47 2023

@author: apkom
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from utils import *

# Load transparency scores table
df_scores = pd.read_excel("C:/Users/apkom/Documents/COVID19_Data_Analysis_CA_Incarcerated_Jails/All_Data/Transparency_Scores.xlsx")



# Fully vaccinated + boosted plot

# Transparency scores per county    
f, ax = plt.subplots(figsize=(7, 20))  

# Generate data for plot 
selected_vars = select_vars(vars_list = select_numerical_vars(vars_list = df_scores.columns), 
                            keywords = ['Percent of Population Fully Vaccinated', 'Percent of Population Boosted'], 
                            point_in_time = True, 
                            historical = False, 
                            staff = True, 
                            population = True)
print('Variables included in the plot are:', selected_vars)

# Store filtered data
selected_vars.append('County')
df_filter = pd.DataFrame()
df_filter = df_scores[selected_vars]

# Calculate percentage of data variables reported by a county in the category
transparency_scores = list((df_filter.sum(axis = 1, numeric_only = True)/(len(selected_vars)-1))*100)
df_filter['Transparency Scores']  = transparency_scores
df_filter.sort_values(by = 'Transparency Scores', ascending = False, inplace = True)

# Plot the data transparency score (%) per county
y = df_filter['County'] 
x = df_filter['Transparency Scores']
sns.barplot(x=x, y=y, palette=gen_palette(x_val = x)).set_title('Vaccinations - Point in time (>= 1 data point)')




# Point in time cases plot

# Transparency scores per county    
f, ax = plt.subplots(figsize=(7, 20))  

# Generate data for plot 
selected_vars = select_vars(vars_list = select_numerical_vars(vars_list = df_scores.columns), 
                            keywords = ['Cases'], 
                            point_in_time = True, 
                            historical = False, 
                            staff = True, 
                            population = True)
print('Variables included in the plot are:', selected_vars)

# Store filtered data
selected_vars.append('County')
df_filter = pd.DataFrame()
df_filter = df_scores[selected_vars]

# Calculate percentage of data variables reported by a county in the category
transparency_scores = list((df_filter.sum(axis = 1, numeric_only = True)/(len(selected_vars)-1))*100)
df_filter['Transparency Scores']  = transparency_scores
df_filter.sort_values(by = 'Transparency Scores', ascending = False, inplace = True)

# Plot the data transparency score (%) per county
y = df_filter['County'] 
x = df_filter['Transparency Scores']
sns.barplot(x=x, y=y, palette=gen_palette(x_val = x)).set_title('Positive Cases - Point in time (>=1 data point)')




# Historical cases plot

# Transparency scores per county    
f, ax = plt.subplots(figsize=(7, 20))  

# Generate data for plot 
selected_vars = select_vars(vars_list = select_numerical_vars(vars_list = df_scores.columns), 
                            keywords = ['Cases'], 
                            point_in_time = False, 
                            historical = True, 
                            staff = True, 
                            population = True)
print('Variables included in the plot are:', selected_vars)

# Store filtered data
selected_vars.append('County')
df_filter = pd.DataFrame()
df_filter = df_scores[selected_vars]

# Calculate percentage of data variables reported by a county in the category
transparency_scores = list((df_filter.sum(axis = 1, numeric_only = True)/(len(selected_vars)-1))*100)
df_filter['Transparency Scores']  = transparency_scores
df_filter.sort_values(by = 'Transparency Scores', ascending = False, inplace = True)

# Plot the data transparency score (%) per county
y = df_filter['County'] 
x = df_filter['Transparency Scores']
sns.barplot(x=x, y=y, palette=gen_palette(x_val = x)).set_title('Positive Cases - Historical (>=50 data points)')
