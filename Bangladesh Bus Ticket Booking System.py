import datetime


class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number.upper()
        self.route = route
        self.total_seats = total_seats
        self.booking = {}
   
    def available_seats(self, date):
        return self.total_seats - self.booking.get(date, 0)
   

class Passenger:
    def __init__(self, name , phone, email, bus):
        self.name = name
        self.phone = phone
        self.email = email
        self.bus = bus
        self.fare = 500


class Booking:
    verification_counter = 10000
    seat_price = 500


    def __init__(self, passenger, bus, date, seats):
        Booking.verification_counter += 1567
        self.code = Booking.verification_counter
        self.passenger = passenger
        self.bus = bus
        self.date = date
        self.seats = seats
        self.fare = len(seats)*Booking.seat_price
       
   
    def display_ticket(self):
        ticket_print = [
            f"Passenger : {self.passenger.name}",
            f"Phone  : {self.passenger.phone}",
            f"Email  : {self.passenger.email}",
            f"Date   : {self.date}",
            f"Bus No : {self.bus.number}",
            f"Route  : {self.bus.route}",
            f"Fare   : ৳{self.fare} (৳500 per seat)",
            f"Verification Code: {self.code}"
        ]


        ticket_border = max(len(ticket) for ticket in ticket_print)+ 4
        print("=" * ticket_border)


        for ticket in ticket_print:
            print(f"* {ticket.ljust(ticket_border - 3)} =")
       
        print("=" *ticket_border)


class BusSystem:


    def __init__(self):
        self.buses = []
        self.passenger = []
        self.all_booking = []
        self.add_initial_buses()




    def add_initial_buses(self):


# 1.Sylhet, 2.Khulna, 2.Chittagong, 3.Barisal, 4.Dhaka, 5. Rangpur, 6.Rajshahi


        self.buses.append(Bus("SYL-DHK-01", "Sylhet to Dhaka", 45))
        self.buses.append(Bus("SYL-CTG-02", "Sylhet to Chittagong", 45))
        self.buses.append(Bus("SYl-KHU-03", "Sylhet to Khulna", 45))
        self.buses.append(Bus("SYL-MYM-04", "Sylhet to Mymensingh", 45))
        self.buses.append(Bus("SYL-RAN-05", "Sylhet to Rangpur", 45))
        self.buses.append(Bus("SYL-RAJ-06", "Sylhet to Rajshahi", 45))
        self.buses.append(Bus("SYL-BAR-07", "Sylhet to Barisal", 45))


        self.buses.append(Bus("KHU-SYL-01", "Khulna to Sylhet", 45))
        self.buses.append(Bus("KHU-DHK-02", "Khulna to Dhaka", 45))
        self.buses.append(Bus("KHU-MYM-03", "Khulna to Mymensingh", 45))
        self.buses.append(Bus("KHU-CTG-04", "Khulna to Chittagong", 45))
        self.buses.append(Bus("KHU-RAJ-05", "Khulna to Rajshahi", 45))
        self.buses.append(Bus("KHU-BAR-06", "Khulna to Barisal", 45))
        self.buses.append(Bus("KHU-RAN-07", "Khulna to Rangpur", 45))


        self.buses.append(Bus("CTG-SYL-01", "Chittagong to Sylhet", 45))
        self.buses.append(Bus("CTG-DHK-02", "Chittagong to Dhaka", 45))
        self.buses.append(Bus("CTG-MYM-03", "Chittagong to Mymensingh", 45))
        self.buses.append(Bus("CTG-KHU-04", "Chittagong to Khulna", 45))
        self.buses.append(Bus("CTG-RAJ-05", "Chittagong to Rajshahi", 45))
        self.buses.append(Bus("CTG-RAN-06", "Chittagong to Rangpur", 45))
        self.buses.append(Bus("CTG-BAR-07", "Chittagong to Barisal", 45))


        self.buses.append(Bus("BAR-SYL-01", "Barisal to Sylhet", 45))
        self.buses.append(Bus("BAR-DHK-02", "Barisal to Dhaka", 45))
        self.buses.append(Bus("BAR-MYM-03", "Barisal to Mymensingh", 45))
        self.buses.append(Bus("BAR-CTG-04", "Barisal to Chittagong", 45))
        self.buses.append(Bus("BAR-RAJ-05", "Barisal to Rajshahi", 45))
        self.buses.append(Bus("BAR-KHU-06", "Barisal to Khulna", 45))
        self.buses.append(Bus("BAR-RAN-07", "Barisal to Rangpur", 45))


        self.buses.append(Bus("DHK-SYL-01", "Dhaka to Sylhet", 45))
        self.buses.append(Bus("DHK-KHU-02", "Dhaka to Khulna", 45))
        self.buses.append(Bus("DHK-MYM-03", "Dhaka to Mymensingh", 45))
        self.buses.append(Bus("DHK-CTG-04", "Dhaka to Chittagong", 45))
        self.buses.append(Bus("DHK-RAJ-05", "Dhaka to Rajshahi", 45))
        self.buses.append(Bus("DHK-BAR-06", "Dhaka to Barisal", 45))
        self.buses.append(Bus("DHK-RAN-07", "Dhaka to Rangpur", 45))


        self.buses.append(Bus("RAN-MYM-01", "Rangpur to Mymensingh", 45))
        self.buses.append(Bus("RAN-DHK-02", "Rangpur to Dhaka", 45))
        self.buses.append(Bus("RAN-CTG-03", "Rangpur to Chittagong", 45))
        self.buses.append(Bus("RAN-KHU-04", "Rangpur to Khulna", 45))
        self.buses.append(Bus("RAN-SYL-05", "Rangpur to Sylhet", 45))
        self.buses.append(Bus("RAN-RAJ-06", "Rangpur to Rajshahi", 45))
        self.buses.append(Bus("RAN-BAR-07", "Rangpur to Barisal", 45))


        self.buses.append(Bus("RAJ-MYM-01", "Rajshahi to Mymensingh", 45))
        self.buses.append(Bus("RAJ-DHK-02", "Rajshahi to Dhaka", 45))
        self.buses.append(Bus("RAJ-CTG-03", "Rajshahi to Chittagong", 45))
        self.buses.append(Bus("RAJ-KHU-04", "Rajshahi to Khulna", 45))
        self.buses.append(Bus("RAJ-SYL-05", "Rajshahi to Sylhet", 45))
        self.buses.append(Bus("RAJ-RAN-06", "Rajshahi to Rangpur", 45))
        self.buses.append(Bus("RAJ-BAR-07", "Rajshahi to Barisal", 45))


        self.buses.append(Bus("MYM-RAJ-01", "Mymensingh to Rajshahi", 45))
        self.buses.append(Bus("MYM-DHK-02", "Mymensingh to Dhaka", 45))
        self.buses.append(Bus("MYM-CTG-03", "Mymensingh to Chittagong", 45))
        self.buses.append(Bus("MYM-KHU-04", "Mymensingh to Khulna", 45))
        self.buses.append(Bus("MYM-SYL-05", "Mymensingh to Sylhet", 45))
        self.buses.append(Bus("MYM-RAN-06", "Mymensingh to Rangpur", 45))
        self.buses.append(Bus("MYM-BAR-07", "Mymensingh to Barisal", 45))


    def add_bus(self, number , route , seats):
        if seats <= 0:
            print("Error : Enter positive Seat Number:")
            return False
       
        if any (bus.number == number.upper() for bus in self.buses):
            print(f"Bus{number} already in service!")
            return False
       
        self.buses.append(Bus(number, route, seats))
        print(f'Bus {number} added succesfully!')
        return True
   


    def find_route_buses(self, route, date):
        return [bus for bus in self.buses if bus.route.lower() == route.lower() and bus.available_seats(date) > 0 ]
   
    def validate_date(self, date_str):
        try:
            day , month, year = [int(i) for i in date_str.split('-')]
            datetime.date(year, month, day)
            return True
       
        except ValueError:
            return False
       
    def book_seats(self):
        while True:
            date = input("Enter trval date (DD-MM-YYYY):").strip()
            if self.validate_date(date):
                break
            print("Invalid date format! Please enter in correct format.")




        departure = input("Enter Departure City:").strip()
        arrival = input("Enter Arrival city:").strip()
        route = f"{departure} to {arrival}"


        available_buses = self.find_route_buses(route, date)
        if not available_buses:
            print(f"\n No buses available for {route} on {date}")
            return



        print(f"\nAvilable  buses for {route} on {date}:")
        for bus in available_buses:
            print(f"Bus {bus.number} - {bus.available_seats(date)} seats avilable")
       
        while True:
            bus_num = input("Enter bus number (DHK-SYL-01): ").upper()
            selected_bus = next((b for b in available_buses if b.number == bus_num), None)
            if selected_bus:
                break
            print("Invalid Bus Number! Please Enter correct Bus Number.")


        name = input("Enter Passenger Full Name :").strip()


        while True:
            phone = input("Enter phone number(11 Digits:)").strip()
            if phone.isdigit() and len(phone) == 11:
                break
            print("Invalid phone Number! Must be 11 digits.").strip()


        while True:
            email = input("Enter Email address:").strip()
            if '@' in email and '.' in email.split('@')[-1]:
                break
            print("Invalid email format! Please Enter correct email address.")



        while True:
            try:


                seats_needed = int(input("Number of seats  needed :").strip())
                if seats_needed <= 0 :
                    raise ValueError
                if seats_needed <= selected_bus.available_seats(date):
                    break
                print(f"Only {selected_bus.available_seats(date)} seats available!")
              
            except ValueError:


                print("Inalid input! Please enter a Correct number.")


        current_booked = selected_bus.booking.get(date, 0)
        selected_bus.booking[date] = current_booked + seats_needed
        seats = list(range(current_booked + 1, current_booked + seats_needed+1))


        passenger = Passenger(name, phone,email,selected_bus)
        self.passenger.append(passenger)


        booking = Booking(passenger, selected_bus,date,seats)
        self.all_booking.append(booking)  


        print("\nBooking successful!")
        print("Printing ticket...")
        booking.display_ticket()


    def show_buses(self):
        print("\n=============== Avialble Bus Routes==============\n")
        for bus in self.buses:
            print(f"Bus {bus.number} - {bus.route}")
        print("\n==================================================\n")
           

class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"
        self.logged_in = False


    def login (self, username , password):
        if username == self.username and password == self.password:
            self.logged_in = True
            return True
        return False
   
    def logout(self):
        self.logged_in = False
        print("Logged out successfully!")


def admin_menu(system, admin):
    while admin.logged_in:
        print("\n Bus Authority Portal")
        print("1. Add New Bus")
        print("2. View All Bookings")
        print("3. View All Bus Routes")
        print("4. Logout")
       


        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input! Please enter 1-3")
            continue


        if choice == 1:
            number = input("Enter bus number: ").strip()
            route = input("Enter route: ").strip()
            try:
                seats = int(input("Enter total seats: "))
                system.add_bus(number, route, seats)
            except ValueError:
                print("Invalid seats number! Enter positive ")
           
        elif choice == 2:
            print("\n=== All Bookings ===")
            if not system.all_booking:
                print("No bookings avilable.")
            else:
                for booking in system.all_booking:
                    print(f"Verfification Code : {booking.code}")
                    print(f"Date : {booking.date} | Bus: {booking.bus.number}")
                    print(f"Contact : {booking.passenger.phone} | {booking.passenger.email}")
                    print(f"Seats: {','.join(str(i) for i in booking.seats)} | Total Fare: ৳{booking.fare}")
                    print("-"*50)


        elif choice == 3:
            system.show_buses()


        elif choice == 4:
            admin.logout()
            break
        else:
            print("Not Found! Enter correct option between. (1-4):")






def main():
    system = BusSystem()
    admin = Admin()


    while True:
        print("\nBangladesh Bus Ticket Booking System")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")


        try:
            choice = int (input("Enter choice:"))
        except ValueError:
            print("Invalid input! Please enter (1-4)")
            continue
       
        if choice == 1:
            if admin.logged_in:
                print("You are already logged in!")
                continue


            username = input("Username: ").strip()
            password = input("Password: ").strip()
            if admin.login(username,password):
                admin_menu (system, admin)
            else:
                print("Wrong! Enter correct Username and Password")


        elif choice == 2:
            system.book_seats()


        elif choice == 3:
            system.show_buses()


        elif choice == 4:
            print("Thank for staying with our service." \
            "Wishing a Enjoyable and Nice Journey!!!")
            break
           
        else:
            print("Invalid choice! Please enter between (1-4) :").strip()

if __name__ == "__main__":
    main()
