class Doctor:
  def _init_(self, name: str):
    self.name = name
    self.patients = []

class Patient:
  def _init_(self,name: str):
    self.name = name
    self.doctors = []

doc = Doctor("Dr. Strange")
pat = Patient("Luchie Luch")

doc.patients.append(pat)
pat.doctors.append(doc)

print(f"{doc.name} knows patient: {doc.patients[0].name})
print(f"{pat.name} knows doctor: {pat.doctors[0].name})
