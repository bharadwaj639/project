# user.py
import pandas as pd

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

def authenticate_user(username, password, file_path='./PA3_credentials.csv'):
    try:
        df = pd.read_csv(file_path)
        match = df[(df['username'] == username) & (df['password'] == password)]
        if not match.empty:
            role = match.iloc[0]['role']
            return User(username, role)
    except Exception as e:
        print(f"Error reading credentials: {e}")
    return None
