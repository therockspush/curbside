import urllib2
import json




def fresh():
    opener = urllib2.build_opener()
    url = 'http://challenge.shopcurbside.com/'
    url2 = url + 'get-session'
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(url2)
    return response.read()





def doit(addon):
    a = fresh()
    
    
    b = 'http://challenge.shopcurbside.com/'
    
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0'),('Session',a)]
    response = opener.open(b+addon)
    c = response.read()
    data = json.loads(c)
    #print data
    
    for key in data.keys():
        data[key.lower()] = data[key]
    if 'next' in data:
        if isinstance(data['next'],list):
            a = data['next']
            for i in a:
                
                doit(i)
        else:
            
            doit(data['next'])
    else:
        print data['secret'],
        
         
        
    
    
try:
    doit('start')
except:
    pass

