from datetime import date, timedelta

from dateutil.relativedelta import relativedelta


class Calendar():

    def __init__(self, n):
        if n > 0:
            self.nDays = int(n)
        
        else:
            print("Calendar must look ahead more than 1 Day!")
            self.nDays = 1

        
        self.bookingDays = []

        startDate  = date.today()

        self.bookingDate = startDate.strftime('%Y-%m-%d')

        endDate = startDate + relativedelta(days=self.nDays)

        self.finalDate = endDate ('%Y-%m-%d')


        delta = endDate - startDate

        for i in range(delta.days + 1):
            day = startDate + timedelta(days=i)

            x = list((day, 'none'))

            self.bookingDays.append(x)
    
    def returnAllBookingDays(self):
        return self.bookingDays
    

    def returnAvailableDateRange(self):
        return self.bookingDate, self.finalDate