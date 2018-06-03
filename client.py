import httplib
conn = httplib.HTTPConnection("localhost:5000")
conn.request("GET", "/start")
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
while 1:
    print("play action:")
    print "1 - check\n2 - raise\n3 - fold\n4 - show pot\n"
    task = input()
    if task == 1 | task == 2 | task == 3:
        conn.request("GET", "/play")
        r2 = conn.getresponse()
        data1 = r2.read()
    elif task == 4:
        conn.request("GET", "/show")
        r2 = conn.getresponse()
        data2 = r2.read()
        print data2
    else:
        break
conn.close()
