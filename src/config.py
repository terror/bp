import os

CONFIG = '~/.bp.toml'
DEFAULT = {'store': '~/.bp'}

class Config:
  def __init__(self, store):
    self.store = os.path.expanduser(store)

  @staticmethod
  def load():
    path = os.path.expanduser(CONFIG)

    if not os.path.exists(path):
      with open(path, 'w') as file:
        for key, value in DEFAULT.items():
          file.write("{} = {}".format(key, value))

    with open(path, 'r') as file:
      lines = file.readlines()

    d = {}
    for line in lines:
      key, value = line.split('=')
      d[key.strip()] = value.strip()

    return Config(**d)
