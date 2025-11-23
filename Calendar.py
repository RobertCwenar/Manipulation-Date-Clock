#Import libraries datetime & calendar
import datetime
import calendar

#Create a calendar for the year 2026
year = 2026

#Set the first weekday to Monday
calendar.setfirstweekday(calendar.MONDAY)

#Dictionary mapping month numbers to month names
var = {1: "January", 
       2: "February", 
       3: "March",
       4: "April",
       5: "May",
       6: "June",
       7: "July",
       8: "August",
       9: "September",
       10: "October",
       11: "November",
       12: "December"} 

#Loop through each month
for month in range(1, 13):
#Write number of month and print the formatted calendar
    month = int(input("Month number (1-12): "))
    if month in var:
        print(f"{var[month]} {year}".center(28))
        print(" CW Mon Tue Wed Thu Fri Sat Sun")
    else:
        print("Invalid month number.")
    
#Loop through each week in the month
    for week in calendar.monthcalendar(year, month):
        first_day = next((day for day in week if day != 0), None)
        Week = datetime.date(year, month, first_day).isocalendar()[1]

#Beautifully format the output
        days =" ".join(f"{day:>3}" if day != 0 else "   " for day in week)
        print(f"{Week:>3} {days}")
    print()

    