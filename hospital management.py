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


def add_patient():

    patient_id = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    disease = input("Enter Disease: ")
    blood_group = input("Enter Blood Group: ")

    patient = Patient(
        patient_id,
        name,
        age,
        disease,
        blood_group
    )

    patients.append(patient)

    print("Patient Added Successfully")


# Test
add_patient()


def display_patients():

    print("\nAll Patients")

    for patient in patients:
        patient.display()


display_patients()
