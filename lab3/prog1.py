import os
import shutil

class File:
    def __init__(self, name):
        self.name = name

    def open(self, mode):
        self.file = open(self.name, mode)

    def close(self):
        self.file.close()

    def read(self):
        self.open('r')
        info = self.file.read()
        self.close()
        return info

    def write(self, content):
        self.open('w')
        self.file.write(content)
        self.close()

    def append(self, content):
        self.open('a')
        self.file.write(content)
        self.close()

    def rename(self, newname):
        os.rename(self.name, newname)
        self.name = newname
    
    def copy(self, path):
        shutil.copy(self.name, path)    


myfile = File('mydata.txt')
myfile.write('hgfh432')

info = myfile.read()

myfile.copy('werw.txt')

print(f'info: {info}')