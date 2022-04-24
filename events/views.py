from django.shortcuts import render

import calendar
from calendar import HTMLCalendar

from datetime import datetime

def home(request, year=False, month=False):
    currTime = datetime.now()

    if year == False:
        # year and month not passed in, so 
        # default them to current time/date
        year = currTime.year
        month = currTime.strftime("%B")
        # and then just continue as before

    # convert month from name to number
    month_number = list(calendar.month_name).index(month.capitalize())
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(
        year,
        month_number
    )

    return render(
        request,            # the request
        'events/home.html', # the template to render
        {                   # the context dict
            'test': "test".capitalize(),
            'year': year,
            'month': month,
            'month_number': month_number,
            'cal': cal,
        }
    )
