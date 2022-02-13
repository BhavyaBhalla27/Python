class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = int(seats)
    def getStatus(self):
        print(f"The name of your train is {self.name}")
        print(f"The number of seats available is {self.seats}")

    def getFareInfo(self):
        print(f"The fare of the train is {self.fare}")
    def bookTicket(self):
        if (self.seats>0):
            print("Your ticket has been booked")
            self.seats = self.seats - 1
            print("Seats remaining are ", self.seats-1)
        else:
            print("Sorry we are full")


passenger1 = Train("Rajdhani Express 189021","300", "21" )
passenger1.getStatus()
passenger1.getFareInfo()
passenger1.bookTicket()

passenger2 = Train("Rajdhani Express 189021","300", "20" )
passenger2.getStatus()
passenger2.getFareInfo()
passenger2.bookTicket()

passenger3 = Train("Rajdhani Express 189021","300", "0" )
passenger3.getStatus()
passenger3.getFareInfo()
passenger3.bookTicket()

