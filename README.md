# CalendarSync

This repository contains scripts which convert schedules in data frame or csv format to ics format files compatible with calendar feeds. 

*DF_to_ICS.py* contains the function which converts dataframes to ics files.
*WHRI_JC_Sync.py* script which converts the WHRI Computational Biology Journal Club schedule to an ics file feed

## Getting Started
**Input data frame** must be of the format:

| Subject       | Start Date | Start Time | End Date | End Time | All Day | Description | Location | UID |
| ------------- | ---------- | ---------- | -------- | -------- | ------- | ----------- | -------- | --- |
| Event 1 | Event 1 | Event 1 | Event 1 | Event 1 | Event 1 | Event 1 | Event 1 | Event 1 |
| Event 2 | Event 2 | Event 2 | Event 2 | Event 2 | Event 2 | Event 2 | Event 2 | Event 2 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| Event n | Event n | Event n | Event n | Event n | Event n | Event n | Event n | Event n |

**Dates** must be of the format the format:  YYYY-MM-DD, or at least YYYY-M-D

**Time** must be of the format: 12-hour (e.g. 1:45pm) or 24-hour (e.g. 13:45)

### Inputs
The function df_to_ics reads in five inputs:
* data - the schedule as a pandas data frame 
* filename - the output filename
* Hour - Dictates whether the input time is in 12-hour or 24 hour format (input options = 12 or 24)
* calendarName - the name of the calendar when imported (default="New Calendar")
* reminder - the number of hours prior to the event at which to receive a reminder. If reminder = NULL then there is no reminder (default=NULL)

## Examples
To create an ics file for the [WHRI Computational Biology Journal Club schedule](https://github.com/WHRICompBio/WHRICompBio.github.io/blob/master/_data/schedule.csv):
```
import pandas as pd
from DF_to_ICS import df_to_ics

# Import the csv file and tidy the data frame
data = pd.read_csv('https://raw.githubusercontent.com/WHRICompBio/WHRICompBio.github.io/master/_data/schedule.csv')
data.columns = ['Start Date', 'Subject']
data['End Date'] = data['Start Date']
data['End Time'] = "3:00pm"
data['Start Time'] = "2:00pm"
data['All Day'] = "FALSE"
data['Description'] = ""
data['UID'] = ""
data['Location'] = "JVSC biopharmacology meeting room"

df_to_ics(Filename="JC_schedule.ics", Hour=12, DF=data, Reminder=96)
```


## Authors
Katriona Goldmann
