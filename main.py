#!/usr/bin/env python
"""
main program
"""
import sys
import csv
from dbfread import DBF

reload(sys)
sys.setdefaultencoding('utf-8')

table = DBF(sys.argv[1])
b = open(sys.argv[2],'w')
writer = csv.writer(b)
print "Mulai.. sabar mang......"
writer.writerow(table.field_names)
for record in table:
	lst=list(record.values())
	writer.writerow(lst)
b.close()

