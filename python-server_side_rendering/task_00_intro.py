#!/usr/bin/python3
"""
Generate invitation files.
"""


def generate_invitations(template, attendees):
    """Generate invitations."""

    # Check template
    if not isinstance(template, str):
        print("Template must be a string")
        return

    # Check attendees
    if not isinstance(attendees, list):
        print("Attendees must be a list of dictionaries")
        return

    # Check each attendee
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print(f"{attendee} must be a dictionary")
            return

    # Check empty template
    if template == "":
        print("Template is empty, no output files generated.")
        return

    # Check empty list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Placeholders to replace
    placeholders = [
        "name",
        "event_title",
        "event_date",
        "event_location"
    ]

    # Create one file for each attendee
    for i in range(len(attendees)):
        invite = template
        attendee = attendees[i]

        # Replace placeholders
        for data in placeholders:
            value = attendee.get(data)

            if value is None:
                value = "N/A"

            invite = invite.replace("{" + data + "}", str(value))

        filename = f"output_{i + 1}.txt"

        # Write the file
        try:
            with open(filename, "w") as file:
                file.write(invite)
        except Exception as error:
            print(f"Error writing {filename}: {error}")
