from enumerations import roomType, roomReservationStatus


class Room:

    reservedStatus = {}
    reservedStatus['1'] = roomReservationStatus.AVAILABLE
    reservedStatus['2'] = roomReservationStatus.RESERVED

    
    def __init__(self, suite):

        self.suiteType = suite
        self.roomCal = None
        self.status = Room.reservedStatus['1']
        self.rFlag = False
        self.rangeStart = None
        self.rangeEnd = False
        self.bookFlag = False



        if self.suiteType == roomType.STANDARD:
            self.price = 100
        elif self.suiteType ==  roomType.DELUXE:
            self.price = 200
        elif self.suiteType == roomType.EXECUTIVE:
            self.price = 500

    def returnRoomCalendar (self):
        pass
        # TODO

    def returnRoomCalendarRange(self):
        pass
        # TODO
    def returnRoomPrice(self):
        return self.price
    
    def bookCustomer(self, ID):

        for i in range(self.rangeStart, self.rangeEnd):
            self.roomCal.returnAllbookingDays()[i] = ID


    def checkReservationDates(self, ckInDate, ckOutDate):
         # Re-initialize at the start

        self.rFlag = False
        self.rangeStart = None
        self.rangeEnd  = None

        # list Comprehension to get the date
        datesOnly = []

        for i in range(len(datesOnly)):
            if datesOnly[i] == ckInDate:
                self.rangeStart = i
            elif datesOnly[i] == ckOutDate:
                self.rangeEnd = i 
        
        if (self.rangeStart and self.rangeEnd) !=None :

            idOnly = []

        else:
            print('Dates out of range or invalid values!')
            self.rFlag = False

        return self.rFlag, self.statuss
    


    def cancelBookindByID(self, ID):
        pass
    # TODO