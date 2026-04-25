import csv
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILENAME = "leads.csv"
CSV_PATH = os.path.join(BASE_DIR, CSV_FILENAME)

def send_email_simulation(name: str, email: str) -> None:
    message = f"""
-------------------------------
To: {email}
Subject: Follow-up

Hi {name},

Just wanted to follow up and see if you had any questions.

Best,
Ryan
-------------------------------
"""
    print(message)

def read_leads(path: str):
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

def main():
    if not os.path.exists(CSV_PATH):
        print(f"❌ Error: {CSV_FILENAME} not found at {CSV_PATH}")
        return

    leads = read_leads(CSV_PATH)
    for lead in leads:
        name = lead.get("name") or lead.get("Name")
        email = lead.get("email") or lead.get("Email")
        if not name or not email:
            continue
        send_email_simulation(name, email)
        time.sleep(1)

if __name__ == "__main__":
    main()