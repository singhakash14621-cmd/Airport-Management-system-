class AirportSystem:
    def __init__(self):
        # Arrays for flights with initial data
        self.flights = [
            {"id": "AI101", "airline": "Air India Airlines", "destination": "Delhi"},
            {"id": "IN202", "airline": "Indigo Airlines", "destination": "Bengaluru"},
            {"id": "SJ303", "airline": "Spicejet Airlines", "destination": "Lucknow"}
        ]
        
        # Linked List for baggage with initial data
        self.baggage_head = None
        self.add_baggage("B001", "Akash Negi", "AI101", "2", "20kg")
        self.add_baggage("B002", "Aman Jha", "IN202", "1", "15kg")
        
        # Stack for ATC commands with initial data
        self.atc_stack = []
        self.atc_stack.append({"flight": "AI101", "command": "Hold for clearance"})
        self.atc_stack.append({"flight": "IN202", "command": "Ready for takeoff"})
        
        # Queue for takeoff with initial data
        self.takeoff_queue = ["AI101", "IN202"]

    #     Baggage (Linked List) 
    def add_baggage(self, baggage_id, passenger_name, flight_id, num_bags, weight):
        class BaggageNode:
            def __init__(self, baggage_id, passenger_name, flight_id, num_bags, weight):
                self.baggage_id = baggage_id
                self.passenger_name = passenger_name
                self.flight_id = flight_id
                self.num_bags = num_bags
                self.weight = weight
                self.next = None
        
        new_baggage = BaggageNode(baggage_id, passenger_name, flight_id, num_bags, weight)
        
        if self.baggage_head is None:
            self.baggage_head = new_baggage
        else:
            current = self.baggage_head
            while current.next:
                current = current.next
            current.next = new_baggage

    #    Flight Operations (Array) 
    def flight_operations(self):
        while True:
            print("\n--- Flight Operations ---")
            print("1. Show All Flights")
            print("2. Add New Flight")
            print("3. Back to Main Menu")
            
            choice = input("Choose option (1-3): ")
            
            if choice == "1":
                print("\nAll Flights:")
                print("-" * 50)
                print("ID\tAirline\t\t\tDestination")
                print("-" * 50)
                for flight in self.flights:
                    print(f"{flight['id']}\t{flight['airline']:<20}\t{flight['destination']}")
            
            elif choice == "2":
                flight_id = input("Flight ID: ")
                airline = input("Airline: ")
                destination = input("Destination: ")
                self.flights.append({"id": flight_id, "airline": airline, "destination": destination})
                print(f"* Added {airline} flight {flight_id}")
            
            elif choice == "3":
                break
            else:
                print("Invalid choice!")

    #      Baggage Operations (Linked List) 
    def baggage_operations(self):
        while True:
            print("\n--- Baggage Operations ---")
            print("1. Show All Baggage")
            print("2. Show Baggage Details")
            print("3. Add Baggage")
            print("4. Back to Main Menu")
            
            choice = input("Choose option (1-4): ")
            
            if choice == "1":
                print("\nAll Baggage:")
                print("-" * 60)
                print("ID\tPassenger\t\tFlight\tBags\tWeight")
                print("-" * 60)
                current = self.baggage_head
                while current:
                    print(f"{current.baggage_id}\t{current.passenger_name:<15}\t{current.flight_id}\t{current.num_bags}\t{current.weight}")
                    current = current.next
            
            elif choice == "2":
                baggage_id = input("Enter Baggage ID to see details: ")
                current = self.baggage_head
                found = False
                while current:
                    if current.baggage_id == baggage_id:
                        print("\n" + "="*40)
                        print("BAGGAGE DETAILS")
                        print("="*40)
                        print(f"Baggage ID: {current.baggage_id}")
                        print(f"Passenger: {current.passenger_name}")
                        print(f"Flight: {current.flight_id}")
                        print(f"Number of Bags: {current.num_bags}")
                        print(f"Total Weight: {current.weight}")
                        print("="*40)
                        found = True
                        break
                    current = current.next
                if not found:
                    print("Baggage not found")
            
            elif choice == "3":
                baggage_id = input("Baggage ID: ")
                passenger = input("Passenger Name: ")
                flight_id = input("Flight ID: ")
                num_bags = input("Number of Bags: ")
                weight = input("Total Weight: ")
                
                self.add_baggage(baggage_id, passenger, flight_id, num_bags, weight)
                print(f"* Added baggage {baggage_id}")
            
            elif choice == "4":
                break
            else:
                print("Invalid choice!")

    #  ATC Operations (Stack)  
    def atc_operations(self):
        while True:
            print("\n--- ATC Operations ---")
            print("1. Show ATC Commands")
            print("2. Add ATC Command")
            print("3. Process Command")
            print("4. Back to Main Menu")
            
            choice = input("Choose option (1-4): ")
            
            if choice == "1":
                print("\nATC Commands:")
                print("-" * 40)
                for cmd in reversed(self.atc_stack):
                    print(f"{cmd['flight']}: {cmd['command']}")
            
            elif choice == "2":
                flight_id = input("Flight ID: ")
                command = input("Command: ")
                self.atc_stack.append({"flight": flight_id, "command": command})
                print(f"* Added command for {flight_id}")
            
            elif choice == "3":
                if self.atc_stack:
                    command = self.atc_stack.pop()
                    print(f"* Processed: {command['command']} for {command['flight']}")
                else:
                    print("No commands to process")
            
            elif choice == "4":
                break
            else:
                print("Invalid choice!")

    #    Takeoff Operations (Queue)  
    def takeoff_operations(self):
        while True:
            print("\n--- Takeoff Operations ---")
            print("1. Show Takeoff Queue")
            print("2. Request Takeoff")
            print("3. Authorize Takeoff")
            print("4. Back to Main Menu")
            
            choice = input("Choose option (1-4): ")
            
            if choice == "1":
                print("\nTakeoff Queue:")
                print("-" * 40)
                for i, flight in enumerate(self.takeoff_queue, 1):
                    print(f"{i}. {flight}")
            
            elif choice == "2":
                flight_id = input("Flight ID: ")
                self.takeoff_queue.append(flight_id)
                print(f"* {flight_id} added to queue")
            
            elif choice == "3":
                if self.takeoff_queue:
                    flight_id = self.takeoff_queue.pop(0)
                    print(f"* {flight_id} authorized for takeoff")
                else:
                    print("Queue is empty")
            
            elif choice == "4":
                break
            else:
                print("Invalid choice!")

    #    Search Operations 
    def search_operations(self):
        while True:
            print("\n--- Search Operations ---")
            print("1. Search Flight")
            print("2. Search Baggage")
            print("3. Back to Main Menu")
            
            choice = input("Choose option (1-3): ")
            
            if choice == "1":
                flight_id = input("Flight ID: ")
                found = False
                for flight in self.flights:
                    if flight["id"] == flight_id:
                        print(f"* Found: {flight['airline']} to {flight['destination']}")
                        found = True
                        break
                if not found:
                    print("* Flight not found")
            
            elif choice == "2":
                baggage_id = input("Baggage ID: ")
                current = self.baggage_head
                found = False
                while current:
                    if current.baggage_id == baggage_id:
                        print(f"* Found: {current.passenger_name} (Flight: {current.flight_id})")
                        found = True
                        break
                    current = current.next
                if not found:
                    print("Baggage not found")
            
            elif choice == "3":
                break
            else:
                print("Invalid choice!")

    #     Show All Data 
    def show_all_data(self):
        print("\n=== Airport Status ===")
        
        print("\nFlights:")
        print("-" * 50)
        print("ID\tAirline\t\t\tDestination")
        print("-" * 50)
        for flight in self.flights:
            print(f"{flight['id']}\t{flight['airline']:<20}\t{flight['destination']}")
        
        print("\nBaggage:")
        print("-" * 60)
        print("ID\tPassenger\t\tFlight\tBags\tWeight")
        print("-" * 60)
        current = self.baggage_head
        while current:
            print(f"{current.baggage_id}\t{current.passenger_name:<15}\t{current.flight_id}\t{current.num_bags}\t{current.weight}")
            current = current.next
        
        print("\nTakeoff Queue:")
        print("-" * 40)
        for i, flight in enumerate(self.takeoff_queue, 1):
            print(f"{i}. {flight}")
        
        print("\nATC Commands:")
        print("-" * 40)
        for cmd in reversed(self.atc_stack):
            print(f"{cmd['flight']}: {cmd['command']}")

    #     Main Menu 
    def main_menu(self):
        while True:
            print("\n" + "="*40)
            print("AIRPORT MANAGEMENT SYSTEM")
            print("="*40)
            print("1. Flight Operations")
            print("2. Baggage Operations")
            print("3. ATC Operations")
            print("4. Takeoff Operations")
            print("5. Search Operations")
            print("6. Show All Data")
            print("7. Exit")
            
            choice = input("\nChoose option (1-7): ")
            
            if choice == "1":
                self.flight_operations()
            elif choice == "2":
                self.baggage_operations()
            elif choice == "3":
                self.atc_operations()
            elif choice == "4":
                self.takeoff_operations()
            elif choice == "5":
                self.search_operations()
            elif choice == "6":
                self.show_all_data()
            elif choice == "7":
                print("Thank you for using the Airport System!")
                break
            else:
                print("Invalid choice! Please try again.")


#    Run Program   
if __name__ == "__main__":
    airport = AirportSystem()
    airport.main_menu()
