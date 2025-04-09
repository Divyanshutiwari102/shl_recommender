import pandas as pd

class SHLRecommender:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = pd.read_csv(self.csv_file)
        self.df.columns = self.df.columns.str.lower().str.strip()  # normalize headers

    def recommend(self, job_role, skill_level):
        job_role = job_role.lower()
        skill_level = skill_level.lower()

        # Filter logic
        filtered_df = self.df[
            self.df['target_job_roles'].str.lower().str.contains(job_role, na=False) &
            self.df['skill_level'].str.lower().str.contains(skill_level, na=False)
        ]

        return filtered_df
