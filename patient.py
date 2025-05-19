# patient.py
import pandas as pd
import uuid

class PatientManager:
    def __init__(self, file_path='./docs/PA3_data.csv'):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def save_data(self):
        self.df.to_csv(self.file_path, index=False)

    def add_patient(self):
        pid = input("Enter Patient ID: ")
        existing = self.df[self.df['Patient_ID'] == pid]
        visit_id = str(uuid.uuid4().hex[:8])
        visit_time = input("Enter Visit Time (YYYY-MM-DD): ")

        if existing.empty:
            new_data = {
                "Patient_ID": pid,
                "Visit_ID": visit_id,
                "Visit_time": visit_time,
                "Visit_department": input("Department: "),
                "Gender": input("Gender: "),
                "Race": input("Race: "),
                "Age": int(input("Age: ")),
                "Ethnicity": input("Ethnicity: "),
                "Insurance": input("Insurance: "),
                "Zip code": input("Zip code: "),
                "Chief complaint": input("Chief complaint: ")
            }
            self.df = pd.concat([self.df, pd.DataFrame([new_data])], ignore_index=True)
            self.save_data()
            print("New patient added.")
        else:
            dept = input("Visit Department: ")
            new_row = {
                "Patient_ID": pid,
                "Visit_ID": visit_id,
                "Visit_time": visit_time,
                "Visit_department": dept,
                "Gender": existing.iloc[0]['Gender'],
                "Race": existing.iloc[0]['Race'],
                "Age": existing.iloc[0]['Age'],
                "Ethnicity": existing.iloc[0]['Ethnicity'],
                "Insurance": existing.iloc[0]['Insurance'],
                "Zip code": existing.iloc[0]['Zip code'],
                "Chief complaint": input("Chief complaint: ")
            }
            self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
            self.save_data()
            print("Visit added for existing patient.")

    def remove_patient(self):
        pid = input("Enter Patient ID to remove: ")
        pid = pid.strip()  # remove any extra whitespace
        self.df['Patient_ID'] = self.df['Patient_ID'].astype(str)  # ensure string comparison

        if pid not in self.df['Patient_ID'].values:
            print(f"Patient ID {pid} not found in records.")
            return

        self.df = self.df[self.df['Patient_ID'] != pid]
        self.save_data()
        print("Patient removed.")

    def retrieve_patient(self):
        pid = input("Enter Patient ID: ")
        pid = pid.strip()
        self.df['Patient_ID'] = self.df['Patient_ID'].astype(str)

        result = self.df[self.df['Patient_ID'] == pid]
        if result.empty:
            print("Patient not found.")
        else:
            print(result)

    def count_visits(self, date):
        count = len(self.df[self.df['Visit_time'] == date])
        print(f"Total visits on {date}: {count}")
