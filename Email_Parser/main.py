# import re

# emails = [
#     "john.doe@example.com",
#     "prajwal.naik@company.co.in",
#     "user123@gmail.com",
#     "hello_world@domain.org",
#     "contact-us@my-site.io",
#     "first.last@sub.domain.com",
#     "name+tag@service.net",
#     "plainaddress",
#     "@nouser.com",
#     "username@.com",
#     "username@domain..com",
#     "username@domain,com",
#     "user name@domain.com",
#     "username@domain"
# ]

# email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# valid_emails =[]
# invalid_emails = []

# for email in emails:
#     if re.match(email_pattern, email):
#         print(email)
#         valid_emails.append(email)
#     else:
#         print(f"{email} - Invalid Email")
#         invalid_emails.append(email)

# print(valid_emails)
# print(invalid_emails)

import re

emails = [
    "john.doe@example.com",
    "prajwal.naik@company.co.in",
    "user123@gmail.com",
    "hello_world@domain.org",
    "contact-us@my-site.io",
    "first.last@sub.domain.com",
    "name+tag@service.net",
    "plainaddress",
    "@nouser.com",
    "username@.com",
    "username@domain..com",
    "username@domain,com",
    "user name@domain.com",
    "username@domain"
]

def parse_emails(email_list):
    pattern = (
        r'^(?!.*\.\.)'           # no double dots
        r'[a-zA-Z0-9._%+-]+'     # username
        r'@[a-zA-Z0-9.-]+'       # domain
        r'\.[a-zA-Z]{2,}$'       # TLD
    )
    
    valid = []
    invalid = []
    
    for email in email_list:
        if re.fullmatch(pattern, email):
            valid.append(email)
        else:
            invalid.append(email)
    
    return valid, invalid

valid_emails, invalid_emails = parse_emails(emails)

print("✅ Valid Emails:", valid_emails)
print("❌ Invalid Emails:", invalid_emails)

