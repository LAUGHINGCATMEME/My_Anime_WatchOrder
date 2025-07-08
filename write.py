import json
from datetime import datetime


def get_today_date():
    """
    Returns the current date in the format "DD MMM YYYY".
    """
    now = datetime.now()
    formatted_date = now.strftime("%d %b %Y")
    return formatted_date


def check_date_format(date_string):
    """
    Checks if the given date string matches the format "DD MMM YYYY".
    Returns True if the format is valid, False otherwise.
    """
    try:
        datetime.strptime(date_string, '%d %b %Y')
        return True
    except ValueError:
        return False


def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def add_anime():
    file_path = 'anime.json'
    # Name
    name = input("Enter the name of the anime: ")
    # Episodes
    while True:
        try:
            episodes = int(input("Enter the number of episodes: "))
            break
        except ValueError:
            print("Enter a valid Integer")
    # Start Date
    start_date = input("Enter the start date: ")
    while not check_date_format(start_date) and start_date != "":
        print("Invalid date format.")
        start_date = input("Enter the start date: ")
    start_date = start_date if start_date != "" else get_today_date()
    # End Date
    end_date = input("Enter the end date: ")
    while not check_date_format(end_date) and end_date != "":
        print("Invalid date format.")
        end_date = input("Enter the end date: ")
    end_date = end_date if end_date != "" else get_today_date()

    # Write the data
    with open(file_path, 'r') as file:
        data = json.load(file)
    next_key = str(len(data) + 1)
    new_entry = {
        "Name": name,
        "Episodes": episodes,
        "Start Date": start_date,
        "End Date": end_date
    }
    data[next_key] = new_entry
    write_json_file(file_path, data)
    print("New anime entry added successfully!")


while True:
    add_anime()
