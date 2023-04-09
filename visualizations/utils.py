# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 14:40:18 2023

@author: apkom
"""

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

