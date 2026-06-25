import csv
import re


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def validate_phone(phone):
    return phone.isdigit() and len(phone) >= 7


def export_to_csv(filename, headers, data):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(data)
        print(f"✅ Data exported to {filename}")
    except Exception as e:
        print(f"❌ Export failed: {e}")