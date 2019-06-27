#!/usr/bin/python3

import pyodbc
from xls_report import XLSReport

#
# Required Debian packages: build-essential unixodbc-bin unixodbc-dev libsqliteodbc
# See: https://github.com/mkleehammer/pyodbc/wiki/
#

connect = pyodbc.connect("Driver=libsqlite3odbc.so;Database=chinook.sqlite")
cursor = connect.cursor()
report = XLSReport({
    'cursor': cursor,
    'xml': 'test_xls.xml',
    'parameters': {
        'title0': 'Invoices',
        'customer': '',
        'title1': 'Albums',
        'title2': 'Money',
        'title3': 'Sales',
        'title4': 'Customers',
        'artist': ''}
})
report.to_file('test.xls')
cursor.close()
connect.close()




