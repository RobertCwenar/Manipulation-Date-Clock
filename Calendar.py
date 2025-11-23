import datetime
import calendar

year = 2026

calendar.setfirstweekday(calendar.MONDAY)


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

for month in range(1, 13):

    month = int(input("Month number (1-12): "))
    if month in var:
        print(f"{var[month]} {year}".center(28))
        print(" CW Mon Tue Wed Thu Fri Sat Sun")
    else:
        print("Invalid month number.")

    

    for week in calendar.monthcalendar(year, month):
        first_day = next((day for day in week if day != 0), None)
        Week = datetime.date(year, month, first_day).isocalendar()[1]


        days =" ".join(f"{day:>3}" if day != 0 else "   " for day in week)
        print(f"{Week:>3} {days}")
    print()

    