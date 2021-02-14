import datetime
import sys
from colored import fore, back, style

#To make the changes required to display the highlighted content on the terminal
import platform
if(platform.system() == "Windows"):
	import ctypes
	kernel32 = ctypes.windll.kernel32
	kernel32.SetConsoleMode(kernel32.GetStdHandle(-11),7)

global monthdays
monthdays = ['',31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#Assuming non leap year - days in a month 


months = ("","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
#Tuple of month names

#Computes the required month, year based on the User input
def reqMonth():
	try:
		inp = sys.argv[1]
		if(inp == "-help"):
			help()
		else:
			inp = int(inp)
	except:
		inp = 0
	req_month = datetime.datetime.now().month + inp
	if(req_month > 12):
		req_month = req_month%12
		year = datetime.datetime.now().year + 1
	elif(req_month < 0):
		req_month = req_month%12
		year = datetime.datetime.now().year - 1
	elif(req_month == 0):
		req_month = 12
		year = datetime.datetime.now().year - 1
	else:
		year = datetime.datetime.now().year
	return year, req_month


#Displays instruction on how to use the application	
def help():
	print("Author: Sai Krishna\nemail: saikrishnabv1998@gmail.com\n\nProject Description:")
	print("\tThis application should be run with the following command line parameters: a positive integer, a negative integer or zero. The positive integer cannot be more than 12, the negative integer cannot be less than -12. The current date will be highlighted in the displayed calendar.\n\nThe calendar for the current month is displayed to present the output. Please re-run with the required commandline argument, to display the calendar for the required month.\n")
	sys.exit()
	
	
#To check if the year to be displayed is a leap year or not and modify monthdays accordingly
def isLeap(year):
	global monthdays
	if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
		monthdays[2] = 29

# To obtain the day corresponding to the first day of the month and  
# then find the offset to be given before printing the first date on the calendar	
def getWeekday(month, year, day):
	return (datetime.date(year, month, day).weekday() + 1)%7

#to get the number of rows required to display the calendar of the desired month	
def getRowsforMonth(month, d1):
	global monthdays
	num = 1
	numDays = monthdays[month]
	d1 = 7 - d1
	remDays = numDays - d1
	while(remDays > 0):
		num += 1
		remDays -= 7
	return num
	
#To format the date to be displayed as a part of the calendar	
def formatDate(date):
	if(date<10):
		return "  "+str(date)
	else:
		return " "+str(date)

#To highlight the current date		
def formatCurrDate(date):
	if(date<10):
		print(fore.RED + back.YELLOW + "  " +str(date) + style.RESET,end='')
	else:
		print(fore.RED + back.YELLOW + " " + str(date) + style.RESET,end='')
	
#To format the month whose calendar is to be displayed 	
def formatMonth(month, year):
	global monthdays
	flag = 0
	d1 = getWeekday(month,year,1)
	row = list(" "*3*d1)
	numRows = getRowsforMonth(month, d1)
	date = 1
	numDays = monthdays[month]
	currDate = datetime.datetime.now().day
	for i in range(numRows):
		count = 0
		while((len(row) < 21 and flag == 0) or (count<21 and flag == 1)):
			if(date == currDate):
				print(''.join(row),end='')
				formatCurrDate(date)
				count = len(row)
				row = []
				flag = 1
			else:
				addItem = formatDate(date)
				row.extend(list(addItem))
			if(flag):
				count+=3
			date +=1
			if(date > numDays):
				break
		flag = 0	
		print(''.join(row))
		row = []
		if(date > numDays):
			break
	
#to print the calendar 	
def printMonth(month, year):
	global months
	print("    ",months[month],year)
	print(" Su","Mo","Tu","We","Th","Fr","Sa")
	formatMonth(month,year)

year, month = reqMonth()
isLeap(year)
printMonth(month,year)	
		
	

