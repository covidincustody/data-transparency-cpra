# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 15:06:35 2023

@author: apkom
"""
from utils import *
import pandas as pd

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

# Specify path to write final transparency scores table
cpra_transparency_scores = gen_data_transparency_scores(all_data = all_jails_data, 
                                                        write_path = "C:/Users/apkom/Documents/COVID19_Data_Analysis_CA_Incarcerated_Jails/All_Data/Transparency_Scores.xlsx",
                                                        historical_data_lim = 10)
