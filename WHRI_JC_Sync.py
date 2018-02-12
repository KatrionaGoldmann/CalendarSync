
import pandas as pd
from DF_to_ICS import df_to_ics

data = pd.read_csv('https://raw.githubusercontent.com/WHRICompBio/WHRICompBio.github.io/master/_data/schedule.csv')
data.columns = ['Start Date', 'Subject']
data['Subject'] = data['Subject'] + " presenting at journal club"
data['End Date'] = data['Start Date']
data['End Time'] = "3:00pm"
data['Start Time'] = "2:00pm"
data['All Day'] = "FALSE"
data['Description'] = ""
data['UID'] = ""
data['Location'] = "biopharmacology meeting room"

data = data[["Subject", "Start Date", "Start Time", "End Date", "End Time", "All Day", "Description",	"Location",	"UID"]]

df_to_ics(Filename="JC_schedule.ics", Hour=12, DF=data, Reminder=96)
