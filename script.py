#!/usr/bin/env python

from __future__ import print_function
import sys, os, cgi

print("Blah", file=sys.stderr)
print("Content-type: text/plain")
print("")
print("Help")
print(os.environ)

form = cgi.FieldStorage()
print(form.getvalue("x"))
