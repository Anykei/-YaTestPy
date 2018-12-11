try :
    sours = open("unix.mailbox")
    client = None
    clientList = dict()
    i = 0
    for line in sours :
        i += 1
        line = line.strip()
        subLine = str(line)
        if subLine.startswith('From '):
            name = subLine[len("From "):len(line):1]
            pos = name.find(" ",0,len(name))
            if pos>0 :
                name = name[0:pos:1]
                if name in clientList:
                    client = clientList[name]
                    client.write(line)
                else:
                    client = open(name+".txt",'w+')
                    client.write(line)
                    clientList[name] = client
        else :
            client.write(line)
        client.write('\n')
        client.flush()
    sours.close()
    for key in clientList :
        client = clientList.get(key)
        client.close()
    clientList.clear()
except IOError :
    print ("error open file")