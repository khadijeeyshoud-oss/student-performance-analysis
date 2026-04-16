import pandas as pd

# Create dataset of students
data = {
    "Student": ["Aisha", "Fatima", "Zainab", "Maryam", "Hauwa"],
    "Math": [85, 78, 92, 70, 88],
    "English": [90, 85, 88, 75, 95],
    "Science": [80, 82, 91, 73, 89]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate total score
df["Total"] = df["Math"] + df["English"] + df["Science"]

# Calculate average score
df["Average"] = df["Total"] / 3

# Find highest scoring student
top_student = df.loc[df["Average"].idxmax()]

# Display results
print("Student Performance Data:")
print(df)

print("\nTop Performing Student:")
print(top_student)
