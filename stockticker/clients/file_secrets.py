from stockticker.clients.base.secrets import SecretsBase
import json


class FileSecrets(SecretsBase):
    def __init__(self, file_path: str):
        self.file_path = file_path
        with open(file_path, "r") as fh:
            self.key_space = json.loads(fh.read())

    def get(self, key: str):
        return self.key_space[key]
