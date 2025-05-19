# note.py
import pandas as pd

class NoteManager:
    def __init__(self, file_path='./docs/PA3_Notes.csv'):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def view_notes(self, date):
        notes = self.df[self.df['Note_ID'].str.contains(date, na=False)]
        if notes.empty:
            print("No notes found for that date.")
        else:
            for _, row in notes.iterrows():
                print(f"\nNote ID: {row['Note_ID']}")
                print(f"Type: {row['Note_type']}")
                print(f"Text: {row['Note_text']}")
