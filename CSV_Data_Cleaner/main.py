# CSV Data Cleaner: Write a script that:
# Reads a CSV of employee records
# Removes duplicates
# Fills missing emails with unknown@company.com

import csv

def clean_employee_csv(input_file, output_file):
    cleaned_records = []
    seen = set()  # To track duplicates

    with open(input_file, newline='') as infile:
        reader = csv.DictReader(infile)
        print("reader", reader.fieldnames)
        for row in reader:
            print("row", row)
            # Fill missing email
            if not row['email']:
                row['email'] = "unknown@company.com"

            # Create a unique key to detect duplicates
            unique_key = (row['name'].strip().lower(), row['email'].strip().lower(), row['department'].strip().lower())

            if unique_key not in seen:
                seen.add(unique_key)
            cleaned_records.append(row)

    # Write cleaned data
    with open(output_file, 'w', newline='') as outfile:
        fieldnames = ['name', 'email', 'department']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_records)

    print(f"✅ Cleaned CSV saved to {output_file}")

# Run the function
clean_employee_csv("employees.csv", "employees_cleaned.csv")
