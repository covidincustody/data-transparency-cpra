# -*- coding: utf-8 -*-

import pandas as pd
import os

# Definitions

def select_vars(vars_list, keywords, point_in_time, historical, staff, population):
    selected_vars = []
    for var in vars_list:
        if point_in_time:
            if staff:
                for word in keywords:
                    if (word in var) and ('point_in_time' in var) and ('Incarcerated population' not in var):
                        selected_vars.append(var)
            if population:
                for word in keywords:
                    if (word in var) and ('point_in_time' in var) and ('Incarcerated population' in var):
                        selected_vars.append(var)
        
        if historical:
            if staff:
                for word in keywords:
                    if (word in var) and ('historical' in var) and ('Incarcerated population' not in var):
                        selected_vars.append(var)
            if population:
                for word in keywords:
                    if (word in var) and ('historical' in var) and ('Incarcerated population' in var):
                        selected_vars.append(var)
    return selected_vars



def select_numerical_vars(vars_list):
    selected_vars = []
    for var in vars_list:
        if (var not in ['As of Date', 'County', 'Facility Name']) and ('time_window' not in var):
            selected_vars.append(var)
    return selected_vars



def gen_palette(x_val):
    palette = []
    x_val = sorted(x_val.tolist(), reverse = True)
    for val in x_val:
        if val >= 80 and val <= 100:
            palette.append('darkgreen')
        elif val >= 60 and val < 80:
            palette.append('mediumseagreen')
        elif val >= 40 and val < 60:
            palette.append('gold')
        elif val >= 20 and val < 40:
            palette.append('sandybrown')
        elif val >= 0 and val < 20:
            palette.append('tomato')
    return palette
    


def gen_data_transparency_scores(all_data, write_path):
    # Initializing dictionary with transparency scores
    data_transparency = {}
    
    # Removing hours, mins and seconds from timestamps
    all_data['As of Date'] = pd.to_datetime(all_data['As of Date'])
    
    # Loop through all counties
    for county in all_data['County']:
        if 'County' in data_transparency.keys():
            data_transparency['County'].append(county)
        else:
            data_transparency['County'] = [county]
        
        # Loop through all variables
        for var in all_data.columns:
            if var not in ['As of Date', 'County', 'Facility Name']:
                county_var_data = all_data[(pd.isna(all_data[var]) == False) & (all_data['County'] == county)][['As of Date', var]]
                
                # If the key value pair exists then append to the list of values
                if str(var+' point_in_time') in data_transparency.keys():
                    if len(county_var_data) >= 1 and len(county_var_data) < 50:
                        data_transparency[str(var+' point_in_time')].append(1)
                        data_transparency[str(var+' historical')].append(0)
                        data_transparency[str(var+' time_window')].append((str(county_var_data['As of Date'].iloc[0]), str(county_var_data['As of Date'].iloc[-1])))
                    elif len(county_var_data) >= 50:
                        data_transparency[str(var+' point_in_time')].append(1)
                        data_transparency[str(var+' historical')].append(1)
                        data_transparency[str(var+' time_window')].append((str(county_var_data['As of Date'].iloc[0]), str(county_var_data['As of Date'].iloc[-1])))
                    elif len(county_var_data) == 0:
                        data_transparency[str(var+' point_in_time')].append(0)
                        data_transparency[str(var+' historical')].append(0)
                        data_transparency[str(var+' time_window')].append('not applicable')
                    else: 
                        data_transparency[str(var+' point_in_time')].append('invalid input')
                        data_transparency[str(var+' historical')].append('invalid input')
                        data_transparency[str(var+' time_window')].append('invalid input')
                # Initializing the key, value pair in the dictionary if it does not exist yet
                else:
                    if len(county_var_data) >= 1 and len(county_var_data) < 50:
                        data_transparency[str(var+' point_in_time')] = [1]
                        data_transparency[str(var+' historical')] = [0]
                        data_transparency[str(var+' time_window')] = [(str(county_var_data['As of Date'].iloc[0]), str(county_var_data['As of Date'].iloc[-1]))]
                    elif len(county_var_data) >= 50:
                        data_transparency[str(var+' point_in_time')] = [1]
                        data_transparency[str(var+' historical')] = [1]
                        data_transparency[str(var+' time_window')] = [(str(county_var_data['As of Date'].iloc[0]), str(county_var_data['As of Date'].iloc[-1]))]
                    elif len(county_var_data) == 0:
                        data_transparency[str(var+' point_in_time')] = [0]
                        data_transparency[str(var+' historical')] = [0]
                        data_transparency[str(var+' time_window')] = ['not applicable']
                    else: 
                        data_transparency[str(var+' point_in_time')] = ['invalid input']
                        data_transparency[str(var+' historical')] = ['invalid input']
                        data_transparency[str(var+' time_window')] = ['invalid input']
     
    # Convert dictionary to df
    df_scores = pd.DataFrame(data_transparency)
    
    # Write transparency scores to file
    with pd.ExcelWriter(write_path) as writer:  
        df_scores.to_excel(writer, sheet_name='Scores', index = False)
    print('Table with data transparency scores written to specified path')
    
    return df_scores
        
        
# Read the COVID data for all counties
# Data can be downloaded from this link: https://docs.google.com/spreadsheets/d/1q9zoEN_nI_oBAxO8k_9kd5612gCaMHSfViU-1WKVSKY/edit#gid=0
all_jails_data = pd.read_excel("C:/Users/apkom/Documents/COVID19_Data_Analysis_CA_Incarcerated_Jails/All_Data/All_Data.xlsx")

# Select and order the columns of interest
all_jails_data = all_jails_data[['As of Date', 'Facility Name', 'County',
       'Active Cases (Incarcerated population, current)',
       'Confirmed Cases (Incarcerated population, cumulative)',
       'Deaths (Incarcerated population, cumulative)',
       'Tests (Incarcerated population, cumulative)',
       'Pending Tests (Incarcerated population, current)',
       'Population (Incarcerated population, current)',
       'Fully Vaccinated (Incarcerated population, current)',
       'Boosted (Incarcerated population, current)',
       'Percent of Population Fully Vaccinated (Incarcerated population)',
       'Percent of Population Boosted (Incarcerated population)',
       'Active Cases (Jail staff, current)',
       'Confirmed Cases (Jail staff, cumulative)',
       'Deaths (Jail staff, cumulative)', 
       'Tests (Jail staff, cumulative)',
       'Population (Jail staff, current)',
       'Fully Vaccinated (Jail staff, current)',
       'Boosted (Jail staff, current)',
       'Percent of Population Fully Vaccinated (Jail staff)',
       'Percent of Population Boosted (Jail staff)',
       "Active Cases (Sheriff's office, current)",
       "Confirmed Cases (Sheriff's office, cumulative)",
       "Deaths (Sheriff's office, cumulative)",
       "Tests (Sheriff's office, cumulative)",
       "Population (Sheriff's office, current)",
       "Fully Vaccinated (Sheriff's office, current)",
       "Boosted (Sheriff's office, current)",
       "Percent of Population Fully Vaccinated (Sheriff's office)",
       "Percent of Population Boosted (Sheriff's office)",
       'Population (Medical staff, current)',
       'Fully Vaccinated (Medical staff, current)',
       'Boosted (Medical staff, current)',
       'Percent of Population Fully Vaccinated (Medical staff)',
       'Percent of Population Boosted (Medical staff)']]

cpra_transparency_scores = gen_data_transparency_scores(all_data = all_jails_data, write_path = "C:/Users/apkom/Documents/COVID19_Data_Analysis_CA_Incarcerated_Jails/All_Data/Transparency_Scores.xlsx")


