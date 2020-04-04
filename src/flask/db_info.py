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
