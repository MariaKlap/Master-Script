# Regulatory Intelligence Automation Script

This repository contains the automation logic for collecting, consolidating, and reporting regulatory news updates across multiple channels. The output includes Excel, CSV, SQLite, and Word formats, ready for sharing and reporting in Power BI.

---

## ✅ Prerequisites

Before running the script, ensure you have:

- Python installed (version 3.8 or above)
- Required libraries:

📥 1. Update GitHub Data
Ensure that the latest RI.csv file is uploaded to the Master-Script repository at:

👉 https://github.com/MariaKlap/Master-Script

⚠️ The file name must be RI.csv for the comparison and merging to work properly.

💻 2. Run MasterscriptGit.py Locally
From your local system:

Download MasterscriptGit.py from this repository.

Place it in a working folder.

Run the script:
python MasterscriptGit.py

This will generate the following files in the same directory:

RI.xlsx: Combined news entries from all Excel sources

RI.csv: CSV version of the combined news

RI.db: SQLite database for analysis

News.xlsx: Newly published articles compared to existing GitHub data

RI_News.docx: Word report for Regulatory Affairs team

📊 3. Import Data into Power BI
Open Power BI Desktop, then:

Go to: Home > Get Data > More > Python Script

Paste the following code:
import sqlite3
import pandas as pd

# Change this to the full local path where your RI.db file is stored
db_path = r'C:\Path\To\Your\RI.db'  # ← replace with actual path

conn = sqlite3.connect(db_path)
query = "SELECT * FROM regulatory_intelligence"
df = pd.read_sql_query(query, conn)
conn.close()

Click OK and import the data.

Build your report as needed and publish it to the Power BI Service.

✉️ 4. Email Template to RA Department
Attach the following files: RI_News.docx & RI.xlsx

Subject: Monthly Regulatory Intelligence Update

Body:

Dear All,

You can find new news from last month in the attached RI_News.docx.

All news collected from last month (including repeated ones) is available in RI.xlsx, and you can explore the full dashboard using the link below:

👉 [Share your Power BI report link here]

Best regards,

Kind regards,  
[Your Name]

Stay informed. Stay compliant.
