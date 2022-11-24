import json


class Config:
    file_path = None
    dir_path = None
    data = None

    def __init__(self, file_path: str = None):
        if file_path is None or file_path == '':
            raise ValueError('file_path must not be empty')
        else:
            if not file_path.endswith('.json'):
                raise ValueError('file_path must be a json file')
            self.file_path = file_path  # config file path
        self.data = {}
        self.load()

    def add_any(self, key: str, value):
        try:
            self.data[key] = value
        except Exception as e:
            print('error: while adding config value: ' + value, "error value: ", e)

    def add_string(self, key: str, value: str):
        if not isinstance(value, str):
            raise TypeError('value must be string')
        else:
            self.data[key] = value

    def add_int(self, key: str, value: int):
        if not isinstance(value, int):
            raise TypeError('value must be int')
        else:
            self.data[key] = value

    def add_float(self, key: str, value: float):
        if not isinstance(value, float):
            raise TypeError('value must be float')
        else:
            self.data[key] = value

    def add_bool(self, key: str, value: bool):
        if not isinstance(value, bool):
            raise TypeError('value must be bool')
        else:
            self.data[key] = value

    def add_default(self, default: dict):
        for key in default.keys():
            if key not in self.data.keys():
                print('info: adding default config value: ' + key)
                self.data[key] = default[key]

    def add_const(self, const_config: dict):
        for key, value in const_config.items():
            if key not in self.data.keys():
                self.data[key] = value
            else:
                if self.data[key] != value:
                    print("key: " + key + " has been modified, change to default value: " + value)
                    self.data[key] = value

    def get(self, key: str):
        if key in self.data.keys():
            return self.data[key]
        else:
            print("no such key found: " + key)

    def get_all(self):
        return self.data

    def get_all_keys(self):
        return self.data.keys()

    def load(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f) or {}
        except FileNotFoundError:
            try:
                # if not os.path.isdir(self.dir_path):
                #     os.makedirs(self.dir_path)
                with open(self.file_path, 'w'):
                    pass
            except Exception as e:
                print('error: ', e)
                print('error: while creating config file: ' + self.file_path)
        except Exception as e:
            print('error: ', e)
            print('error: while reading config file: ' + self.file_path)

    def save(self):
        try:
            with open(self.file_path, 'w') as f:
                json.dump(self.data, f, sort_keys=True, indent=4)
        except Exception as e:
            print('error: ', e)
            print('error: while saving config file: ' + self.file_path)
