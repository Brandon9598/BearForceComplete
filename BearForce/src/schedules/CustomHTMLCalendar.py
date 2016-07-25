import os, datetime
from django.contrib.auth.models import User
from calendar import HTMLCalendar
from .models import News_Messages, Shift


class CustomHTMLCalendar(HTMLCalendar):
    
    #information about bearforce worker
    

    # CSS classes for the day <td>s
    cssclasses = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
 
    def formatday(self, date_row):
        bearforce_worker = User.objects.get(username="brandon9598")
        shifts_to_work = bearforce_worker.shift_set.all()
        """
        Return a day as a table cell.
        """
        if date_row.month != self.month:
            return '<td class="noday">&nbsp;</td>' # day outside month
        else:
            day_shifts = '<li class="work_date">'
            for shift in shifts_to_work:
                if shift.date.day == date_row.day:
                    day_shifts = day_shifts + "<ul id='shift_specifics'>" + shift.working_location + " " + str(shift.time) + "</ul>"
            day_shifts = day_shifts + "</li>"
            formatted_day = '<td class="%s" id="numbered_date">%d\n %s</td>' % (self.cssclasses[date_row.weekday()], date_row.day, day_shifts)
            return formatted_day

 
    def formatweek(self, theweek):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(date_row) for date_row in theweek)
        return '<tr>%s</tr>' % s
 
    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
        special_week_header = '<tr id="special_week_header"><th class="sun">Sun</th><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th></tr>'

        v = []
        a = v.append
        a('<table class="table table-bordered">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        #a('<div id="weekheader">')
        a(special_week_header)
       # a('</div>')
        a('\n')
        dates = list(self.itermonthdates(theyear, themonth))
        self.month = themonth
        records = [ dates[i:i+7] for i in range(0, len(dates), 7) ]
        for week in records:
            a(self.formatweek(week))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)
 
    def formatyear(self, theyear, width=3):
        """
        Return a formatted year as a table of tables.
        """
        v = []
        a = v.append
        width = max(width, 1)
        a('<table border="0" cellpadding="0" cellspacing="0" class="year">')
        a('\n')
        a('<tr><th colspan="%d" class="year">%s</th></tr>' % (width, theyear))
        for i in range(January, January+12, width):
            # months in this row
            months = range(i, min(i+width, 13))
            a('<tr>')
            for m in months:
                a('<td>')
                a(self.formatmonth(theyear, m, withyear=False))
                a('</td>')
            a('</tr>')
        a('</table>')
        return ''.join(v)