import dataclasses
import json
import os

PATH = '~/.bp.json'
DEFAULT = {'store': '~/.bp'}

@dataclasses.dataclass
class Config:
  store: str

  @staticmethod
  def load():
    path = os.path.expanduser(PATH)

    if not os.path.exists(path):
      with open(path, 'w') as file:
        json.dump(DEFAULT, file)

    with open(path, 'r') as file:
      return Config(**json.load(file))
