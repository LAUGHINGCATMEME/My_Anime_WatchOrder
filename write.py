import json


def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def add_anime():
    file_path = 'anime.json'
    name = input("Enter the name of the anime: ")
    episodes = int(input("Enter the number of episodes: "))
    start_date = input("Enter the start date: ")
    end_date = input("Enter the end date: ")
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


add_anime()
