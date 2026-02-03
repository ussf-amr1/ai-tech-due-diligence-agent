from ast import main
from agent.analyzer import analyze_project
from agent.risk_engine import assess_risks
from agent.recommender import make_recommendation
import os

# Path to the sample project
project_path = "sample_project"

# Make sure report folder exists
if not os.path.exists("report"):
    os.makedirs("report")

# Analyze the project
file_report = analyze_project(project_path)

# Assess technical risks
risks = assess_risks(file_report)

# Generate Go/No-Go recommendation
recommendation = make_recommendation(risks)

# Print the report
print("File Report:", file_report)
print("Risks Detected:", risks)
print("Recommendation:", recommendation)

# Save the report to a file
with open("report/output.txt", "w") as f:
    f.write("File Report:\n" + str(file_report) + "\n")
    f.write("Risks Detected:\n" + str(risks) + "\n")
    f.write("Recommendation:\n" + recommendation + "\n")

if __name__ == "__main__":
    main()