# stats.py
import pandas as pd
import matplotlib.pyplot as plt

class StatsGenerator:
    def __init__(self, data_file='./PA3_data.csv'):
        self.df = pd.read_csv(data_file)
        self.df['Visit_time'] = pd.to_datetime(self.df['Visit_time'], format='mixed', dayfirst=False, errors='coerce')

    def generate_all_stats(self):
        self.plot_trend('Visit_time', 'Total Visits', title='Hospital Visit Trends Over Time')
        self.plot_trend('Insurance', 'Insurance Type', title='Visits by Insurance Type')
        self.plot_trend('Gender', 'Gender', title='Visits by Gender')
        self.plot_trend('Race', 'Race', title='Visits by Race')

    def plot_trend(self, group_by, label, title='Trend'):
        if group_by == 'Visit_time':
            grouped = self.df.groupby(self.df['Visit_time'].dt.date).size()
        else:
            grouped = self.df[group_by].value_counts()

        grouped.plot(kind='bar', title=title)
        plt.xlabel(label)
        plt.ylabel('Number of Visits')
        plt.tight_layout()
        filename = f"{label.lower().replace(' ', '_')}_trend.png"
        plt.savefig(filename)
        plt.close()
        print(f"{title} saved as {filename}")