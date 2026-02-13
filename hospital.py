class Hospital:
    def __init__(self):
        self.patients = {}

    def add_patient(self, pid, name, age, disease):
        self.patients[pid] = {
            "Name": name,
            "Age": age,
            "Disease": disease,
            "Doctor": "Not Assigned",
            "Days": 0,
            "Bill": 0
        }
        return "Patient Added Successfully"

    def assign_doctor(self, pid, doctor):
        if pid in self.patients:
            self.patients[pid]["Doctor"] = doctor
            return "Doctor Assigned"
        else:
            return "Patient ID Not Found"

    def generate_bill(self, pid, days, room_charge, medicine_charge):
        if pid in self.patients:
            bill = (days * room_charge) + medicine_charge
            self.patients[pid]["Days"] = days
            self.patients[pid]["Bill"] = bill
            return bill
        else:
            return "Patient ID Not Found"

    def display_patient(self, pid):
        if pid in self.patients:
            return self.patients[pid]
        else:
            return "Patient ID Not Found"

    def discharge_patient(self, pid):
        if pid in self.patients:
            del self.patients[pid]
            return "Patient Discharged Successfully"
        else:
            return "Patient ID Not Found"

main.py
from hospital import Hospital

hospital = Hospital()

while True:
    print("\n----- HOSPITAL MANAGEMENT SYSTEM -----")
    print("1. Add Patient")
    print("2. Assign Doctor")
    print("3. Generate Bill")
    print("4. Display Patient Details")
    print("5. Discharge Patient")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = int(input("Enter Age: "))
        disease = input("Enter Disease: ")
        print(hospital.add_patient(pid, name, age, disease))

    elif choice == 2:
        pid = input("Enter Patient ID: ")
        doctor = input("Enter Doctor Name: ")
        print(hospital.assign_doctor(pid, doctor))

    elif choice == 3:
        pid = input("Enter Patient ID: ")
        days = int(input("Enter number of days admitted: "))
        room = int(input("Enter room charge per day: "))
        medicine = int(input("Enter medicine charges: "))
        bill = hospital.generate_bill(pid, days, room, medicine)
        print("Total Bill Amount: Rs.", bill)

    elif choice == 4:
        pid = input("Enter Patient ID: ")
        details = hospital.display_patient(pid)
        print(details)

    elif choice == 5:
        pid = input("Enter Patient ID: ")
        print(hospital.discharge_patient(pid))

    elif choice == 6:
        print("Exiting Hospital System")
        break

    else:
        print("Invalid Choice")
