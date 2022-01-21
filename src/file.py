import functools
import os
from error import InvalidFileFormat

class Path:
  def __init__(self, path):
    self.path = os.path.expanduser(path)

  def __repr__(self):
    return self.path

  @property
  def last(self):
    return os.path.basename(os.path.normpath(self.path))

  @property
  def filename(self):
    return os.path.splitext(self.last)[0]

  @property
  def ext(self):
    return os.path.splitext(self.last)[1]

class File(Path):
  def __init__(self, path):
    super().__init__(path)
    if self.ext != ".bp":
      raise InvalidFileFormat("File must be a valid `.bp` file.")

  @functools.cached_property
  def env(self):
    env = {'filename': self.filename, 'extension': ''}

    for line in self.content[1:]:
      if line.strip() == "---":
        break
      key, value = line.split(":")
      env[key.strip()] = value.strip()

    return env

  @property
  def end(self):
    for idx, line in enumerate(self.content[1:]):
      if line.strip() == '---':
        return idx + 2

  @property
  def content(self):
    with open(self.path, "r") as file:
      content = file.readlines()
    return content
