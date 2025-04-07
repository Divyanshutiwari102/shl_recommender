from recommender import SHLRecommender

if __name__ == "__main__":
    rec = SHLRecommender("assessments.csv")

    job_role = input("Enter job role (e.g., Analyst, Manager): ")
    skill_level = input("Enter skill level (e.g., Entry, Mid, Senior): ")

    result = rec.recommend(job_role, skill_level)

    print("\nRecommended Assessments:\n")
    print(result.to_string(index=False))
