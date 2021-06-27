import os

class Path:
  def __init__(self, path):
    self.path = path

  def __repr__(self):
    return self.path

  @property
  def last(self):
    return os.path.basename(os.path.normpath(self.path))

  @property
  def filename(self):
    name, _ = os.path.splitext(self.last)
    return name

  @property
  def ext(self):
    _, ext = os.path.splitext(self.last)
    return ext

class File(Path):
  def __init__(self, path):
    super().__init__(path)
    if self.ext != ".bp":
      raise InvalidFileFormat("File must be a valid `.bp` file.")

  @property
  def env(self):
    env = {'filename': self.filename, 'extension': ''}

    for line in self.content()[1:]:
      if line.strip() == "---":
        break
      key, value = line.split(":")
      env[key.strip()] = value.strip()

    return env

  @property
  def end(self):
    for idx, line in enumerate(self.content()[1:]):
      if line.strip() == '---':
        return idx + 2

  def content(self):
    with open(self.path, "r") as file:
      content = file.readlines()
    return content
