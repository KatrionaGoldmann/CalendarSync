
import pandas as pd
import numpy as np
from DF_to_ICS import df_to_ics

text_file = open("schedule_path.txt", "r")
file = text_file.read()
data_safe = pd.read_csv(file)

data = data_safe
data['Subject'] = data['Presenter'] + " presenting at journal club"

data['Start Date'] = data['Date']
data['End Date'] = data['Date']
data['Start Time'] = data['Start Time'].astype(str).str.split().str[1]
data['Start Time'] = data['Start Time'].str.split(":").str[0] + ':' + data['Start Time'].str.split(":").str[1]

data['End Time'] = data['End Time'].astype(str).str.split().str[1]
data['End Time'] = data['End Time'].str.split(":").str[0] + ':' + data['End Time'].str.split(":").str[1]

data['All Day'] = "FALSE"
data['Description'] = data['Topic']
data['UID'] = ""
data['Location'] = data['Location'].fillna("Biopharmacology meeting room")

data = data[["Subject", "Start Date", "Start Time", "End Date", "End Time", "All Day", "Description",	"Location",	"UID"]]


data = data.dropna(axis=0, subset=['Subject'])

df_to_ics(Filename="JC_schedule.ics", Hour=24, DF=data, Reminder=96)
