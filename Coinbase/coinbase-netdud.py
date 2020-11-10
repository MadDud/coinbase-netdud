import sys
import configparser

print("Coinbase netdud - v1.0")
print("---")

def getCoinbaseData(path):
    import urllib2, json
    import hmac
    import hashlib
    import base64
    import time
    import json
    import configparser

    # read config
    config = configparser.ConfigParser()
    config.read('coinbase-netdud.conf')

    apiKey = str(config.get('default','apiKey'))
    apiSecret = str(config.get('default','apiSecret'))

    # main
    url = "https://api.coinbase.com%s" % path

    headers = {}

    timestamp = int(time.time())
    headers['CB-ACCESS-KEY'] = apiKey
    headers['CB-ACCESS-TIMESTAMP'] = timestamp
    headers['CB-VERSION'] = '2018-02-01'

    toSign = str(timestamp) + 'GET' + path
    signature = hmac.new(apiSecret, toSign, hashlib.sha256).hexdigest()
    headers['CB-ACCESS-SIGN'] = signature

    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request, timeout=2.5)
        data = json.loads(response.read())
        print json.dumps(data,indent=3)
    except Exception as e:
        print "ERROR: %s" % str(e)

getCoinbaseData('/v2/'+str(sys.argv[1]))

