
# Version 3: Event Registration Formatter

# Import date feature
from datetime import date

# Ask for student information
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")

# Ask for event date
year = int(input("Enter event year: "))
month = int(input("Enter event month: "))
day = int(input("Enter event day: "))

# Format student information
first_name = first_name.strip().title()
last_name = last_name.strip().title()
section = section.strip().upper()
event_name = event_name.strip().title()

# Combine full name
full_name = first_name + " " + last_name

# Format event date
event_date = date(year, month, day)

# Display registration summary
print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section)
print("Event:", event_name)
print("Event Date:", event_date.strftime("%B ") + str(event_date.day) + event_date.strftime(", %Y"))
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("Registration record created successfully.")
