import json
import csv
import re
json_file_path = "logs.json"
csv_file_path = "error_logs.csv"

with open(json_file_path, 'r') as jsonFile:
    data = json.load(jsonFile)
    header = data[0].keys()
    with open(csv_file_path, 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(header)
        for i in data:
            pattern = r"ERROR"
            match = re.search(pattern, str(i.values()), re.IGNORECASE)
            # pattern2 = r"ERROR+."
            # match2 = re.search(pattern, str(i.values()), re.IGNORECASE)
            # if match2:
            if match:
                writer.writerow(i.values())

