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


patient1 = Patient(
    "P001",
    "Ramesh",
    45,
    "Diabetes",
    "O+"
)

print(patient1.patient_id)
print(patient1.name)
print(patient1.age)
print(patient1.disease)
print(patient1.blood_group)
