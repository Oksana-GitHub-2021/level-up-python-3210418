import csv

def merge_csv(csv_list, output_path):
  rows = []
  header_fields = []

  for csv_file in csv_list:
    print(f'Reading file: {csv_file}')
    with open(csv_file, 'r', encoding='utf-8', newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      data = list(reader)
    rows.extend(data)
    for field in reader.fieldnames:
      if field not in header_fields:
        header_fields.append(field)

  with open(output_path, 'w', encoding='utf-8', newline='') as output_csv:
    writer = csv.DictWriter(output_csv, list(header_fields))
    writer.writeheader()
    for row in rows:
      writer.writerow(row)   


merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')