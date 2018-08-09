from http.client import HTTPConnection
import sys


method = 'GET'
if len(sys.argv) > 1: # so you can  --fail
    method = 'get'

conn =  HTTPConnection('127.0.0.1', 6543)
conn.request(method, '/')
resp = conn.getresponse()
content = resp.read()

assert resp.status == 200, 'KO'
print('OK')
