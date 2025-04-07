import pandas as pd

class SHLRecommender:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self._preprocess()

    def _preprocess(self):
        self.df.fillna('', inplace=True)
        self.df['Target_Job_Roles'] = self.df['Target_Job_Roles'].str.lower()
        self.df['Skill_Level'] = self.df['Skill_Level'].str.lower()
        self.df['Tags'] = self.df['Tags'].str.lower()

    def recommend(self, job_role, skill_level, top_n=5):
        job_role = job_role.lower()
        skill_level = skill_level.lower()

        # First try to match both
        filtered = self.df[
            self.df['Target_Job_Roles'].str.contains(job_role) &
            self.df['Skill_Level'].str.contains(skill_level)
        ]

        # Fallback to partial match
        if filtered.empty:
            filtered = self.df[
                self.df['Target_Job_Roles'].str.contains(job_role) |
                self.df['Skill_Level'].str.contains(skill_level)
            ]

        return filtered[['Assessment_ID', 'Assessment_Name', 'Tags']].head(top_n)
