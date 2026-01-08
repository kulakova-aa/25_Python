# TODO импортировать необходимые молули



def task() -> None:
    ...  # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4



import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task():
    def csv_to_json(input_file, output_file, delimiter=',', line_delimiter='\n'):
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
            rows = content.split(line_delimiter)
            if not rows:
                print("Файл пустой или некорректный формат.")
                return

            headers = rows[0].split(delimiter)
            data = []

            for row in rows[1:]:
                if row.strip():
                    values = row.split(delimiter)
                    if len(values) == len(headers):
                        record = {headers[i]: values[i] for i in range(len(headers))}
                        data.append(record)

        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)


    csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME)



if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME, encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")

