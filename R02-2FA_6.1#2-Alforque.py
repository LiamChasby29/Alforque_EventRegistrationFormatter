
# Version 2: Event Registration with String Formatting

# Ask for student information
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")

# Ask for event date
year = input("Enter event year: ")
month = input("Enter event month: ")
day = input("Enter event day: ")

# Format student information
first_name = first_name.strip().title()
last_name = last_name.strip().title()
section = section.strip().upper()
event_name = event_name.strip().title()

# Combine names
full_name = first_name + " " + last_name

# Display formatted information
print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section)
print("Event:", event_name)
print("Year:", year)
print("Month:", month)
print("Day:", day)
