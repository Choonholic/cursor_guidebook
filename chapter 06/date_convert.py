import pandas as pd
from datetime import datetime

# Load the CSV file
df = pd.read_csv('cursor_guidebook/chapter 06/sample/before.csv')

# Function to convert various date formats to ISO 8601
def convert_to_iso(date_str):
    for fmt in ("%Y/%m/%d", "%Y/%d/%m", "%d-%m-%Y", "%d.%m.%Y", "%Y-%m-%d", "%b %d, %Y", "%B %d, %Y", "%Y년 %m월 %d일", "%Y年%m月%d日", "%Y년%m월%d일"):
        try:
            return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue
    raise ValueError(f"Date format for {date_str} not recognized")

# Apply the conversion function to the 'date' column
df['date'] = df['date'].apply(convert_to_iso)

# Save the modified DataFrame to a new CSV file
df.to_csv('cursor_guidebook/chapter 06/sample/after.csv', index=False)
