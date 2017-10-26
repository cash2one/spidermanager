# -*- coding: utf-8 -*-
from spidermanager import app
from spidermanager import db

from spidermanager.controller import main, user, login,hivejob

try:
    from spidermanager.controller import item
except:
    pass

from spidermanager.setting import spdmgrport

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=spdmgrport,debug=False)

def main():
    app.run(host='0.0.0.0',port=spdmgrport,debug=False)