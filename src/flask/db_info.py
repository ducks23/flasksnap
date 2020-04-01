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
        data_folder = Path("/var/snap/myflask/common/config/")
        file_to_open = data_folder / "text-file.txt"
        return open(file_to_open)

