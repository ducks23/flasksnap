from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from jinja2 import Template


class DB_info:
    def __init__(self):
        self.user = None
        self.password = None
        self.host = None
        self.port = None
        self.dbname = None
        self._file = None
        self.connected = 0;

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    def set_host(self, host):
        self.host = host

    def set_port(self, port):
        self.port = port

    def set_dbname(self, dbname):
        self.dbname = dbname

    def set_file_open(self, _file):
        self._file = _file

    def get_open_file(self):
        return self._file

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def get_dbname(self):
        return self.dbname

    def is_connected(self):
        return self.connected

    def parsefile(self, f):
        while True:
            line = f.readline()
            line = line.split()
            if len(line) > 2:
                if line[0] == 'DB_USER':
                    db.set_user(line[2])
                elif line[0] == 'DB_PASSWORD':
                    db.set_password(line[2][1:-1])

                elif line[0] == 'DB_HOST':
                    db.set_host(line[2][1:-1])

                elif line[0] == 'DB_PORT':
                    db.set_port(line[2][1:-1])

                elif line[0] == 'DB_NAME':
                    db.set_dbname(line[2][1:-1])
            if not line:
                break

    def openFile(self):
        data_folder = Path(f"{os.environ['SNAP_COMMON']}/config/")
        file_to_open = data_folder / "text-file.txt"
        _file = None
        print("right here!!!!!!!!!!")
        try:
            _file = open(file_to_open)
            self.connected = 1
        except:
            print("couldn't open file yet")
            self.connected = 0
        return _file
