import csv
import json
from config import Config

class ParserCBRF:
    def start(self):
        for i in Config.header:
            Config.table_headers.append(i.text)

        with open('currencies.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(Config.table_headers)
            writer.writerows(Config.td_content)
            file.close()

    def serialize(self):
        with open('parsed_data/currencies.json', 'w', encoding='utf-8') as f:
            json.dump(Config.td_content, f)

    def deserialize(self):
        with open('parsed_data/currencies.json', 'r', encoding='utf-8') as l:
            file_contents = l.read()

        with open('parsed_data/currenciesed.csv', 'w', encoding='utf-8') as d:
           data = json.loads(file_contents)
           writer = csv.writer(d)
           writer.writerows(data)
           d.close()
