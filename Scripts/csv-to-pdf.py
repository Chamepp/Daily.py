import openpyxl
import sys


csv_name = input("Name Of The CSV File For Input (Extention Required): ")
sep = input("Seperator Of The CSV File: ")
excel_name = input("Name Of The Excel File For Output (Extention Required): ")
sheet_name = input("Name Of The Excel Sheet For Output: ")

# Open Files
try:
	wb = openpyxl.load_workbook(excel_name)
	sheet = wb.get_sheet_by_name(sheet_name)

	file = open(csv_name,"r",encoding = "utf-8")
except:
	print("File Error!")
	sys.exit()

# Set Data
row = 1
column = 1

# Generate a List
for line in file:
	line = line[:-1]
	line = line.split(sep)

    # Write Data
	for data in line:
		sheet.cell(row,column).value = data
		column += 1

	column = 1
	row += 1

# Save and Close
wb.save(excel_name)
file.close()
