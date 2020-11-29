from tika import parser
import csv
import math
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('-i', '--laptimes_pdf', help='file name for race history chart input pdf')
argparser.add_argument('-o', '--output_csv', help='file name for csv output of lap times')
args = argparser.parse_args()

input_filename = args.laptimes_pdf
output_filename = args.output_csv
raw = parser.from_file(input_filename)
content = raw['content'].replace('\n\n', '\n')

def getLines(content):
    line_array = []
    line_buffer = ""
    for x in content:
        if x != "\n":
            line_buffer += x
        else:
            line_array.append(line_buffer)
            line_buffer = ""
    return line_array

def getFilteredLines(raw_lines):
    lines = []
    dropped_lines = []
    for l in raw_lines:
        if len(l) != 0 and len(l) < 44 and 'Page' not in l and 'Race' not in l and 'FORMULA' not in l:
            lines.append(l)
        else:
            dropped_lines.append(l)
    return(lines, dropped_lines)


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier



def getLapTimeSec(lap_time):
    lap_time_min = float(lap_time[0:lap_time.find(":")].strip())
    lap_time_sec = float(lap_time[lap_time.find(":")+1:].strip())
    lap_time_sec_new = round_half_up(lap_time_min * 60.0 + lap_time_sec, 3)
    return lap_time_sec_new

class LapTime:
    def __init__(self, lap_no, driver_no, gap, lap_time, lap_time_sec, position):
        self.lap_no = lap_no
        self.driver_no = driver_no
        self.gap = gap
        self.lap_time = lap_time
        self.lap_time_sec = lap_time_sec
        self.position = position
    
    def __str__(self):
        return "Driver: " + self.driver_no + "\nLap: " + self.lap_no + "\nLap Time: " + self.lap_time + "\nGap to P1: " + self.gap + "\nPosition: " + self.position


def getLapTimes(final_lines):
    lap_no = 0
    lap_times = []
    position = 0
    for l in final_lines:
        if l.startswith("LAP"):
            lap_no = l.split(" ")[1]
            position = 0
        else:
            position += 1
            driver_no = l[0:l.find(" ")]
            gap = l[l.find(" "):l.rfind(" ")].strip()
            lap_time = l[l.rfind(" "):].strip()
            lap_time_sec = getLapTimeSec(lap_time)
            lap_time_obj = LapTime(str(lap_no), driver_no, gap, lap_time, lap_time_sec, position)
            lap_times.append(lap_time_obj)

    return lap_times


def writeToCsv(lap_times, fileName):
    with open(fileName, mode='w') as outputFile:
        writer = csv.writer(outputFile, delimiter = ',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["lap_no", "position", "driver_no", "lap_time", "lap_time_sec", "gap"])
        for l in lap_times:
            writer.writerow([l.lap_no, l.position, l.driver_no, l.lap_time, l.lap_time_sec, l.gap])



lines = getLines(content)
(final_lines, dropped_lines) = getFilteredLines(lines)
lap_times = getLapTimes(final_lines)
writeToCsv(lap_times, output_filename)
