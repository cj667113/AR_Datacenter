import requests
import json
import re
import time
def prtg_collect():
    global temperature
    prtg_setup=['prtgadmin','985831223','20062'] #Username,#Passhash,#SensorID
    url = "https://monitor.its.ohio.edu/api/table.json?noraw=1&content=channels&sortby=name&columns=name=textraw,minimum,maximum,condition,lastvalue&id=%s&login=%s&passhash=%s" %(prtg_setup[2],prtg_setup[0],prtg_setup[1])
    data_raw = requests.get(url=url)
    data=(json.loads(data_raw.text))
    data=str(data)
    data=re.split("\{|}|\[|]",data)
    options=[''"u'lastvalue': " '' , ''" u'name': " ''] ##Used split along lastvalue and channel names
    search_parm=['Temperature'] ##Specify what channel names to split/channel names needed to be returned
    search_parm_2=[''"u'Temperature'"''] ##Specific unicode pattern to return of channel names
    gather=[]
    format=[]
    for item in data:
        if len(item)>=1:
            item=item.split(",")
            for x in item:
                if re.search(options[0],x):
                    if len(x)>17:
                        z=x.split(options[0])
                        for y in z:
                            if len(y)>0:
                                gather.append((y))      
                for y in search_parm:
                    if re.search(y,x):
                        if len(x)>17:
                            z=x.split(options[1])
                            for y in z:
                                if len(y)>0:
                                    gather.append((y))
    for x in gather:
        for y in search_parm_2:
            if x==y:
                format.append((x,gather[(gather.index(x))-1]))
    temperature=format[0][1]
    temperature=(str(unicode(temperature)).strip("u'"))
while True:
    prtg_collect()
    f = open('data/temperature_LoPRTS.html','w')
    f.write('<a-text id="change" value=%r color="black" position="-.3 .35 1.2"></a-text>'%(temperature))
    f.close()
    time.sleep(1)
