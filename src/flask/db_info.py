from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from jinja2 import Template
import os
import sys
import subprocess

class DB_info:
    def __init__(self):
        self.user = None
        self.password = None
        self.host = None
        self.port = None
        self.dbname = None
        self._file = None
        self.connected = 0

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

    def get_file(self):
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

    def parsefile(self):
        text = self.get_file()
        print(text)
        
        '''
        while True:
            if len(line) > 1:
                if line[0] == 'DB_USER':
                    self.set_user(line[1][1:-1])
                elif line[0] == 'DB_PASSWORD':
                    self.set_password(line[1][1:-1])
                elif line[0] == 'DB_HOST':
                    self.set_host(line[1][1:-1])
                elif line[0] == 'DB_PORT':
                    self.set_port(line[1][1:-1])
                elif line[0] == 'DB_NAME':
                    self.set_dbname(line[1][1:-1])
            if not line:
                break
'''
                
    def openFile(self):
        data_folder = Path(f"/var/snap/flasksnap/common/config/")
        file_to_open = data_folder / "thecodes.txt"
        try:
            self._file = open(file_to_open )
            self.connected = 1
        except:
            print("couldn't open file yet")
            self.connected = 0
        
