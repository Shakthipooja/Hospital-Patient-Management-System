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


patient1 = Patient(
    "P001",
    "Ramesh",
    45,
    "Diabetes",
    "O+"
)

patient1.display()
