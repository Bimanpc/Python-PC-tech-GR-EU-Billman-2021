# calender viewer
import sys
import calendar

# function to view calendar
viewCalender = lambda yy, mm: print("\n\n Calendar > \n %s\n" % calendar.month(yy, mm))

# UI
while True:
	if str(input("[+] Πάμε!! [Y/n] ?  ")).strip().lower() == "y":
		try:
			viewCalender(int(input("\nYear: ")), int(input("Month: ")))
		except IndexError:
			print("  -> Try Again!! With valid numbers!\n")
	else:
		print("\nSee Byy Soon!!")
		sys.exit(0)
