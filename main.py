class Patient:
    def __init__(self, id, name, age, complaint):
        self.id = id
        self.name = name
        self.age = age
        self.complaint = complaint

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Age: {self.age} | Complaint: {self.complaint}"


class DentistQueueSystem:
    COMPLAINTS = [
        "Toothache",
        "Cavity",
        "Braces Checkup",
        "Tooth Extraction",
        "Dental Cleaning",
        "Other"
    ]

    def __init__(self):
        self.queue = []
        self.next_id = 1

    def choose_complaint(self):
        print("\nSelect Complaint:")

        for i, complaint in enumerate(self.COMPLAINTS, start=1):
            print(f"{i}. {complaint}")

        while True:
            try:
                choice = int(input("Choose complaint: "))

                if 1 <= choice <= len(self.COMPLAINTS):
                    if self.COMPLAINTS[choice - 1] == "Other":
                        return input("Enter complaint: ")

                    return self.COMPLAINTS[choice - 1]

                print("Invalid choice.")

            except ValueError:
                print("Please enter a number.")

    def add_patient(self, name, age, complaint):
        patient = Patient(self.next_id, name, age, complaint)
        self.queue.append(patient)
        self.next_id += 1

    def view_queue(self):
        if not self.queue:
            print("\nQueue is empty.")
            return

        print("\n===== CURRENT QUEUE =====")

        for position, patient in enumerate(self.queue, start=1):
            print(f"{position}. {patient}")

    def serve_patient(self):
        if not self.queue:
            print("\nQueue is empty.")
            return

        patient = self.queue.pop(0)

        print("\n===== NOW SERVING =====")
        print(patient)

    def search_patient(self, id):
        for patient in self.queue:
            if patient.id == id:
                print("\n===== PATIENT FOUND =====")
                print(patient)
                return

        print("Patient not found.")

    def count_patients(self):
        print(f"\nTotal patients in queue: {len(self.queue)}")


def main():
    system = DentistQueueSystem()

    while True:
        print("\n===== DENTIST CLINIC QUEUE SYSTEM =====")
        print("1. Add Patient")
        print("2. View Queue")
        print("3. Serve Patient")
        print("4. Search Patient")
        print("5. Count Patients")
        print("6. Exit")

        choice = input("Choose menu: ")

        if choice == "1":
            name = input("Patient Name: ")

            try:
                age = int(input("Age: "))
            except ValueError:
                print("Age must be a number.")
                continue

            complaint = system.choose_complaint()

            system.add_patient(name, age, complaint)
            print("Patient added successfully!")

        elif choice == "2":
            system.view_queue()

        elif choice == "3":
            system.serve_patient()

        elif choice == "4":
            try:
                id = int(input("Enter Patient ID: "))
                system.search_patient(id)
            except ValueError:
                print("ID must be a number.")

        elif choice == "5":
            system.count_patients()

        elif choice == "6":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()