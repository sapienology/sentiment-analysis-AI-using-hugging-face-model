import urllib.request, json, sys
payload = json.dumps({"text": "The training was excellent and I learned a lot."}).encode()
req = urllib.request.Request("http://127.0.0.1:8000/predict", data=payload, headers={"Content-Type": "application/json"})
try:
    resp = urllib.request.urlopen(req, timeout=300)
    print(resp.read().decode())
except Exception as e:
    print('ERROR', e)
    sys.exit(1)
