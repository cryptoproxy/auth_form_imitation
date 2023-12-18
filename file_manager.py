try:
    import json
except:
    print('Не получилось импортировать json 0-0')


class FileManager:
    def __init__(self):
        self.db_name = 'db.json'

    def read_data(self):
        try:
            with open(self.db_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return []

    def write_data(self, data):
        with open(self.db_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
