# # Day 5: String & Regex
# # String manipulation
# # Using re module for pattern matching
# # Problem: Extract all emails & phone numbers from a text file

# import re

# # File to read
# file_path = "sample.txt"

# # Regex patterns
# email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# phone_pattern = r"(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{3,4}"

# def read_file():
#     try:
#         with open(file_path, 'r') as file:
#             emails_extracted = []
#             phone_numbers_extracted = []
#             for line in file:
#                 emails = re.findall(email_pattern, line)
#                 phone_numbers = re.findall(phone_pattern, line)
#                 emails_extracted.extend(emails)
#                 phone_numbers_extracted.extend(phone_numbers)
#             return emails_extracted, phone_numbers_extracted
#     except FileNotFoundError:
#         print(f"File {file_path} not found")
#     except Exception as e:
#         print(f"An error occurred: {e}")
        
# if __name__ == "__main__":
#     emails, phones = read_file()
#     print("Emails found:", emails)
#     print("Phone numbers found:", phones)


import re

file_path = "sample.txt"

# Regex patterns with boundaries
email_pattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
phone_pattern = r"(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{3,4}"

def read_file():
    emails_extracted = []
    phone_numbers_extracted = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                emails_extracted.extend(re.findall(email_pattern, line))
                phone_numbers_extracted.extend(re.findall(phone_pattern, line))
        
        # Remove duplicates
        emails_extracted = sorted(set(emails_extracted))
        phone_numbers_extracted = sorted(set(phone_numbers_extracted))
        
        return emails_extracted, phone_numbers_extracted
    
    except FileNotFoundError:
        print(f"❌ File '{file_path}' not found.")
        return [], []
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return [], []

if __name__ == "__main__":
    emails, phones = read_file()
    print("📧 Emails found:", emails)
    print("📱 Phone numbers found:", phones)
