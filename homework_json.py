import json
import logging
from pathlib import Path

folder = Path("ideas_for_test/work_with_json")
log_file = "json__Nedilko.log"

logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

for file_path in folder.glob("*.json"):
    try:
        with file_path.open(encoding="utf-8") as file:
            json.load(file)

    except json.JSONDecodeError as error:
        logging.error(
            "Invalid JSON in file %s: %s",
            file_path.name,
            error
        )

print("Перевірку JSON-файлів завершено.")