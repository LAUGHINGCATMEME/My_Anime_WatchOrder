import json

# Read the JSON file
with open(r'..\anime.json') as file:
    data = json.load(file)

# Convert the data to the desired format
output = []
for i, (key, value) in enumerate(data.items(), start=1):
    name = value['Name']
    episodes = value['Episodes']
    start_date = value['Start Date']
    end_date = value['End Date']
    i = str(i) + ")"
    episodes_text = 'episode' if episodes == 1 else 'episodes'
    if start_date == end_date:
        line = "{:<4} {:<69} {:<2} {:<15} on {}".format(i, name, episodes, episodes_text, start_date)
    else:
        line = "{:<4} {:<69} {:<2} {:<15} from {} to {}".format(i, name, episodes, episodes_text, start_date, end_date)
    output.append(line)

print('\n'.join(output))
