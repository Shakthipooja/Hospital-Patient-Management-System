class Patient:

    def __init__(self,
                 patient_id,
                 name,
                 age,
                 disease,
                 blood_group):

        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.blood_group = blood_group

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Blood Group:", self.blood_group)
        print()


# Patient database
patients = []


# Create patient objects
patient1 = Patient(
    "P001",
    "Ramesh",
    45,
    "Diabetes",
    "O+"
)

patient2 = Patient(
    "P002",
    "Priya",
    28,
    "Asthma",
    "B+"
)


# Store patients in list
patients.append(patient1)
patients.append(patient2)


# Display all patients
for patient in patients:
    patient.display()
