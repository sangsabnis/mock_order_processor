import csv

def load_csv_as_dict(path: str):
    try:
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"File {path} not found")
        return []