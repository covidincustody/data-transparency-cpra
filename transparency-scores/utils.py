# -*- coding: utf-8 -*-

import pandas as pd
import os

# Definitions

def gen_var_transparency_score(data_transparency_dict, var, var_data, historical_data_lim):
    
    # Generate transparency scores for a single variable
    
    # If the key value pair exists then append to the list of values
    if str(var+' point_in_time') in data_transparency_dict.keys():
        if len(var_data) >= 1 and len(var_data) < historical_data_lim:
            data_transparency_dict[str(var+' point_in_time')].append(1)
            data_transparency_dict[str(var+' historical')].append(0)
            data_transparency_dict[str(var+' time_window')].append((str(var_data['As of Date'].iloc[0]), str(var_data['As of Date'].iloc[-1])))
        elif len(var_data) >= historical_data_lim:
            data_transparency_dict[str(var+' point_in_time')].append(1)
            data_transparency_dict[str(var+' historical')].append(1)
            data_transparency_dict[str(var+' time_window')].append((str(var_data['As of Date'].iloc[0]), str(var_data['As of Date'].iloc[-1])))
        elif len(var_data) == 0:
            data_transparency_dict[str(var+' point_in_time')].append(0)
            data_transparency_dict[str(var+' historical')].append(0)
            data_transparency_dict[str(var+' time_window')].append('not applicable')
        else: 
            data_transparency_dict[str(var+' point_in_time')].append('invalid input')
            data_transparency_dict[str(var+' historical')].append('invalid input')
            data_transparency_dict[str(var+' time_window')].append('invalid input')
    # Initializing the key, value pair in the dictionary if it does not exist yet
    else:
        if len(var_data) >= 1 and len(var_data) < historical_data_lim:
            data_transparency_dict[str(var+' point_in_time')] = [1]
            data_transparency_dict[str(var+' historical')] = [0]
            data_transparency_dict[str(var+' time_window')] = [(str(var_data['As of Date'].iloc[0]), str(var_data['As of Date'].iloc[-1]))]
        elif len(var_data) >= historical_data_lim:
            data_transparency_dict[str(var+' point_in_time')] = [1]
            data_transparency_dict[str(var+' historical')] = [1]
            data_transparency_dict[str(var+' time_window')] = [(str(var_data['As of Date'].iloc[0]), str(var_data['As of Date'].iloc[-1]))]
        elif len(var_data) == 0:
            data_transparency_dict[str(var+' point_in_time')] = [0]
            data_transparency_dict[str(var+' historical')] = [0]
            data_transparency_dict[str(var+' time_window')] = ['not applicable']
        else: 
            data_transparency_dict[str(var+' point_in_time')] = ['invalid input']
            data_transparency_dict[str(var+' historical')] = ['invalid input']
            data_transparency_dict[str(var+' time_window')] = ['invalid input']
    
    return data_transparency_dict


def gen_data_transparency_scores(all_data, write_path, historical_data_lim):
    # Initializing dictionary with transparency scores
    data_transparency_dict = {}
    
    # Removing hours, mins and seconds from timestamps
    all_data['As of Date'] = pd.to_datetime(all_data['As of Date'])
    
    # Loop through all counties
    for county in all_data['County'].unique():
        if 'County' in data_transparency_dict.keys():
            data_transparency_dict['County'].append(county)
        else:
            data_transparency_dict['County'] = [county]
        
        # Loop through all variables
        for var in all_data.columns:
            if var not in ['As of Date', 'County', 'Facility Name']:
                # Extract var data - single var, single county
                county_var_data = all_data[(pd.isna(all_data[var]) == False) & (all_data['County'] == county)][['As of Date', var]]
                
                # Generate transparency scores for var data
                data_transparency_dict = gen_var_transparency_score(data_transparency_dict = data_transparency_dict,
                                                                    var = var, 
                                                                    var_data = county_var_data, 
                                                                    historical_data_lim = historical_data_lim)
                
    # Convert dictionary to df
    df_scores = pd.DataFrame(data_transparency_dict)
    
    # Write transparency scores to file
    with pd.ExcelWriter(write_path) as writer:  
        df_scores.to_excel(writer, sheet_name='Scores', index = False)
    print('Table with data transparency scores written to specified path')
    
    return df_scores
        
