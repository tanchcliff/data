from tika import parser
import csv
import math
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('-i', '--driverlist', help='file name for entry list pdf')
args = argparser.parse_args()

input_filename = args.driverlist
raw = parser.from_file(input_filename)
content = raw['content'].replace('\n\n', '\n')

# characters to lines
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


# filtering away text used for formatting
def getFilteredLines(raw_lines):
    lines = []
    dropped_lines = []
    for l in raw_lines:
        if len(l) != 0 and len(l) != 1 and l[0:1].isdigit() and "\\x" not in l and "2019" not in l:
            lines.append(l)
        else:
            dropped_lines.append(l)
    return(lines, dropped_lines)


lines = getLines(content)
(drivers, dropped) = getFilteredLines(lines)
for d in drivers:
    print(d)

# with the printed lines, it is an easy job to copy and further process on a text editor.
