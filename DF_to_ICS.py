# Katriona Goldmann, 12/02/2018
# Script converts a pandas data frame to and ics file (iCalendar file).

# ---------------------------
# Inputs:
# DF - pandas data frame with columns: "Subject", "Start Date", "Start Time", "End Date", "End Time", "All Day", "Description", "Location", "UID"
# Filename - Output file name
# Hour - options = 12 or 24 to determine whether the times are 12 or 24 hour format (1:45pm or 13:45)
# CalendarName - The calendar name when imported (default="New Calendar")
# Reminder - the number of hours prior to the event at which to receive a reminder. If reminder = 'NULL' then there is no reminder (default='NULL')
# ---------------------------
import re

def df_to_ics(DF, Filename, Hour, CalendarName="New Calendar", Reminder='NULL', dateFormat="DD-MM-YY"):

    list_a = ["Subject",  "Start Date", "Start Time", "End Date", "End Time", "All Day", "Description", "Location", "UID"]
    list_b = list(DF.columns)

    missing_cols  = list(set(list_a).difference(set(list_b)) )
    if len(missing_cols) > 0:
        import sys
        sys.exit("------\n ERROR: You are missing the following columns:" + str(missing_cols) + "\n------")

    DF = DF[["Subject", "Start Date", "Start Time", "End Date", "End Time", "All Day", "Description",	"Location",	"UID"]]

    def get_time(time):
        if Hour == 12: time = int(time[0]) *10000 + 120000 +  int(time[2:3])*100
        else: time = int(time.replace(":", "")) *100
        return time

    def get_date(date):
        index = [m.start() for m in re.finditer('y', dateFormat.lower())]
        year = date[(index[0]+1):(index[-1]+2)] #date[0:4]
        if len(year) == 2 : year = '20' + year
        index = [m.start() for m in re.finditer('m', dateFormat.lower())]
        month = date[(index[0]+1):(index[-1]+2)] #date[5:7]
        month = str('{num:02d}'.format(num=int(month)))
        index = [m.start() for m in re.finditer('d', dateFormat.lower())]
        day = date[(index[0]+1):(index[-1]+2)] #date[8:]
        day = str('{num:02d}'.format(num=int(day)))
        return year+month+day

    DF['End Time'] = [get_time(x) for x in DF['End Time']]
    DF['Start Time'] = [get_time(x) for x in DF['Start Time']]
    DF['Start Date'] = [get_date(x) for x in DF['Start Date']]
    DF['End Date'] = [get_date(x) for x in DF['End Date']]

    F = open(Filename, "w")
    F.write("BEGIN:VCALENDAR\nPRODID:-//CSV to iCal Convertor//KatrionaGoldmann//EN\nMETHOD:PUBLISH\nX-MS-OLK-FORCEINSPECTOROPEN:TRUE\nX-WR-CALNAME;VALUE=TEXT:" + CalendarName + "\n")

    for index, row in DF.iterrows():
        F.write("BEGIN:VEVENT\nCLASS:PUBLIC\n")
        F.write("DESCRIPTION:" + str(row['Description']) + "\n")
        F.write("LOCATION:" + row['Location'] + "\n")
        F.write("DTSTAMP:" + row['Start Date'] + "T" + str(row['Start Time'])  + "\n")
        F.write("DTSTART:" + row['Start Date'] + "T" + str(row['Start Time'])  + "\n")
        F.write("DTEND:" + row['End Date'] + "T" + str(row['End Time']) + "\n")
        F.write("UID:" + str(row['Subject']).split(' ', 1)[0] + str(row['Start Date']) + "T" + str(row['Start Time']) + "\n")
        F.write("PRIORITY:5" + "\n")
        F.write("SEQUENCE:0" + "\n")
        F.write("SUMMARY;LANGUAGE=en-us:" + str(row['Subject']) + "\n")
        F.write("X-MICROSOFT-CDO-ALLDAYEVENT:FALSE\nX-MICROSOFT-MSNCALENDAR-ALLDAYEVENT:FALSE\n")
        if Reminder != 'NULL':
            F.write("BEGIN:VALARM\nTRIGGER:-PT" + str(Reminder) +"H\nEND:VALARM\n")
        F.write("END:VEVENT" + "\n")

    F.write("END:VCALENDAR")
