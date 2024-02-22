#This is the part 1 of the FBI 
import requests
import json
import csv
import re

def clean_html(text):
    if text is None:
        return 'None'
    clean_text = re.sub(r'<p>|</p>', '\n', text)
    clean_text = re.sub(r'\.', '.\n', clean_text)
    #clean_text = re.sub(r'<[^>]+>', '', clean_text) 
    return clean_text.strip()

response_API = requests.get('https://api.fbi.gov/wanted/v1/list')
data = response_API.text
parse_json = json.loads(data)

with open('FBI.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Name", "Aliases", "Details"])
    
    for item in parse_json['items']:
        category = ', '.join(item.get('subjects', []))
        name = item['title']
        
        aliases = item.get('aliases', [])
        if isinstance(aliases, list):
            aliases_str = clean_html('\n'.join(aliases)) 
        else:
            aliases_str = clean_html(aliases) 

        details = clean_html(item.get('details', ''))
        
        writer.writerow([category, name, aliases_str, details])