import csv
from pathlib import Path

folder = Path("ideas_for_test/work_with_csv")

files = [
    folder / "r-m-c.csv",
    folder / "random-michaels.csv",
]

unique_rows = []
seen = set()

for file_path in files:
    with file_path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            # Прибираємо зайві пробіли на краях клітинок
            row = [cell.strip() for cell in row]

            # Вважаємо дублікатом повністю однаковий рядок
            row_key = tuple(row)

            if row_key not in seen:
                seen.add(row_key)
                unique_rows.append(row)

result_file = Path("result_Nedilko.csv")

with result_file.open("w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(unique_rows)

print(f"Результат збережено у {result_file}")
print(f"Кількість унікальних рядків: {len(unique_rows)}")