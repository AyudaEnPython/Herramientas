import csv
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, mode="r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            try:
                data.append({
                    "title": row["title"],
                    "content": row["content"],
                    "dir": row["dir"],
                    "url": row["url"],
                })
            except Exception as e:
                logging.error("Error: %s", e)
    with open(json_file, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    logging.info(f"> Converted {csv_file} to {json_file}")


if __name__ == "__main__":
    csv_to_json("data/data.csv", "data/data.json")
