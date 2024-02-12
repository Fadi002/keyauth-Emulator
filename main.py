# WARNING: THIS IS NOT KEYAUTH BYPASS !!!!!!

##### CHANGEABLE VALUES #####
SECRET = "" # YOU NEED TO CHANGE THAT !!
SESSION_ID = "5b0kaVXf5k" # RANDOM SESSION ID you can change it ( if you want )
NONCE = "jOH1bU0gDhwoAtYCYI4Zh9beq6wN5tIU" # idk tbh dont change it
SUBSCRIPTION = "default" # you can leave it
SUBSCRIPTION_LEVEL = "1" # you can leave it
FAKE_LICENSE = "PEPE-UNLIMITEDKEY" # you can leave it
EXPIRY = "32475082433" # year 2999 (thank me later lol)
ENCKEY = None # dont touch it !
IP_SPOOF = True
##### CHANGEABLE VALUES #####



##### DONT CHANGE IT AT ALL #####
HOME_PAGE = '''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>KeyAuth Emulator Server</title><style> body{background-color:#121212;color:#fff;font-family:Arial,sans-serif;text-align:center;padding:50px}a{color:#FFD700;text-decoration:none}</style></head><body><h1>KeyAuth Emulator Server</h1><p><a href="https://github.com/Fadi002/">GitHub</a></p><p>Discord username: <span style="color: #29B6F6;">@0xmrpepe</span></p></body></html>'''
__DISCORD_SERVER__ = "https://discord.com/invite/cYxxUHsbRm"
__DISCORD__ = "@0xmrpepe"
__GITHUB__ = "https://github.com/Fadi002" 
##### DONT CHANGE IT AT ALL #####


from flask import Flask, jsonify, request, redirect
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
import hmac, hashlib, httpx, time, os, random, binascii, json

def water(text):
    os.system(""); faded = ""
    green = 10
    for line in text.splitlines():
        faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return faded

print(water(f'''██╗  ██╗███████╗██╗   ██╗ █████╗ ██╗   ██╗████████╗██╗  ██╗
██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔══██╗██║   ██║╚══██╔══╝██║  ██║
█████╔╝ █████╗   ╚████╔╝ ███████║██║   ██║   ██║   ███████║
██╔═██╗ ██╔══╝    ╚██╔╝  ██╔══██║██║   ██║   ██║   ██╔══██║
██║  ██╗███████╗   ██║   ██║  ██║╚██████╔╝   ██║   ██║  ██║
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝
                                                           
███████╗███╗   ███╗██╗   ██╗                               
██╔════╝████╗ ████║██║   ██║                               
█████╗  ██╔████╔██║██║   ██║                               
██╔══╝  ██║╚██╔╝██║██║   ██║                               
███████╗██║ ╚═╝ ██║╚██████╔╝                               
╚══════╝╚═╝     ╚═╝ ╚═════╝
THIS IS NOT A BYPASS !!!!!!!
{''.join(('T'+'I'+'G'+'@'+'Y'+'M'+'@'+'N'+'O'+'@'+'E'+'E'+'R'+'F'+'@'+'S'+'T'+'I'+'@'+'D'+'E'+'M'+'M'+'A'+'C'+'S'+'@'+'T'+'O'+'G'+'@'+'U'+'O'+'Y'+'@'+'N'+'E'+'H'+'T'+'@'+'S'+'I'+'H'+'T'+'@'+'T'+'H'+'G'+'U'+'O'+'B'+'@'+'U'+'O'+'Y'+'@'+'F'+'I').replace(chr(0x40), chr(0x20))[i] for i in range(len(('T'+'I'+'G'+'@'+'Y'+'M'+'@'+'N'+'O'+'@'+'E'+'E'+'R'+'F'+'@'+'S'+'T'+'I'+'@'+'D'+'E'+'M'+'M'+'A'+'C'+'S'+'@'+'T'+'O'+'G'+'@'+'U'+'O'+'Y'+'@'+'N'+'E'+'H'+'T'+'@'+'S'+'I'+'H'+'T'+'@'+'T'+'H'+'G'+'U'+'O'+'B'+'@'+'U'+'O'+'Y'+'@'+'F'+'I')) - 1, -1, -1))}
MADE BY @0xmrpepe | https://github.com/Fadi002'''))
app = Flask(__name__)


def get_signature(response, req_type):
    print("REQUEST TYPE = ", req_type)
    key = SECRET.encode() if req_type == 'init' else (ENCKEY + '-' + SECRET).encode()
    print(key)
    response = jsonify(response).get_data()
    return hmac.new(key, response, hashlib.sha256).hexdigest()

def parse_request_data(request_data):
    data_dict = {}
    for pair in request_data.split('&'):
        key, value = pair.split('=')
        data_dict[key] = value
    return data_dict

class encryption:
    '''
    CREDITS TO KEYAUTH
    '''
    @staticmethod
    def encrypt_string(plain_text, key, iv):
        plain_text = pad(plain_text, 16)
        aes_instance = AES.new(key, AES.MODE_CBC, iv)
        raw_out = aes_instance.encrypt(plain_text)
        return binascii.hexlify(raw_out)

    @staticmethod
    def decrypt_string(cipher_text, key, iv):
        cipher_text = binascii.unhexlify(cipher_text)
        aes_instance = AES.new(key, AES.MODE_CBC, iv)
        cipher_text = aes_instance.decrypt(cipher_text)
        return unpad(cipher_text, 16)

    @staticmethod
    def encrypt(message, enc_key, iv):
        try:
            _key = SHA256.new(enc_key.encode()).hexdigest()[:32]
            _iv = SHA256.new(iv.encode()).hexdigest()[:16]
            return encryption.encrypt_string(message.encode(), _key.encode(), _iv.encode()).decode()
        except:
            print("Encryption error. Make sure your app details are correct, see response below")
            print("Response: " + message)
            time.sleep(3)

    @staticmethod
    def decrypt(message, enc_key, iv):
        try:
            _key = SHA256.new(enc_key.encode()).hexdigest()[:32]
            _iv = SHA256.new(iv.encode()).hexdigest()[:16]
            return encryption.decrypt_string(message.encode(), _key.encode(), _iv.encode()).decode()
        except:
            print("Encryption error. Make sure your app details are correct, see response below")
            print("Response: " + message)
            time.sleep(3)

@app.route('/', methods=['GET'])
def home():return HOME_PAGE

@app.route('/api/1.2/', methods=['GET', 'POST'])
def initapi():
    global ENCKEY
    if request.method == 'POST':
        data_dict = parse_request_data(request.get_data(as_text=True))
        if data_dict['type'] == 'init':
            init_info = {
                'type': data_dict.get('type', ''),
                'ver': data_dict.get('ver', ''),
                'enckey': data_dict.get('enckey', ''),
                'name': data_dict.get('name', ''),
                'ownerid': data_dict.get('ownerid', '')
            }
            ENCKEY = init_info.get('enckey', '')
            response_data = {
                "success": True,
                "message": "Initialized",
                "sessionid": SESSION_ID,
                "appinfo": {
                  "numUsers": "N/A - Use fetchStats() function in latest example",
                  "numOnlineUsers": "N/A - Use fetchStats() function in latest example",
                  "numKeys": "N/A - Use fetchStats() function in latest example",
                  "version": f"{init_info.get('ver','1.0')}",
                  "customerPanelLink": "https://keyauth.cc/panel/mrpepe/mrpepeproject/"
                },
                "newSession": False,
                "nonce": NONCE
                }
            if                                                                                                                                                           hashlib.sha256(__DISCORD_SERVER__.encode()).hexdigest()                                                                                                             !=                                                                                                                          '5cefdc59533db92b60ddb73953cfeab8ce2071c25bd109083d2f4445cedce70a'                                                                                                             :                                                                                       exit()
            if                                                                                                                                                                                               hashlib.sha256(__DISCORD__.encode()).hexdigest()                                                                                                              !=                                                                                                                                      'df7dd9a61829f99f3dd8db773312a325b1cbe6696641779c7f854ca840fd913f'                                                                                                                          :                                                                                                                                                             exit()
            if                                                                                                                                                                                                                       hashlib.sha256(__GITHUB__.encode()).hexdigest()                                                                                                              !=                                                                                                                                                                 '103ff337e0d6565316de4e8b63cf292b6302ab252ecabbde4937cedda5190d30'                                                                                                                                                                                                                                                    :                                                                                                                              exit()
            response = jsonify(response_data)
            response.headers['signature'] = get_signature(response_data, init_info['type'])
            return response
        
        elif data_dict['type'] == 'login':
            form_data = {
                'type': data_dict.get('type', ''),
                'username': data_dict.get('username', ''),
                'pass': data_dict.get('pass', ''),
                'hwid': data_dict.get('hwid', ''),
                'sessionid': data_dict.get('sessionid', ''),
                'name': data_dict.get('name', ''),
                'owenerid': data_dict.get('owenerid', ''),
            }
            response_data = {
                "success": True,
                "message": "Logged in!",
                "info": {
                  "username": form_data.get('username', 'PEPE'),
                  "subscriptions": [
                    {
                      "subscription": SUBSCRIPTION,
                      "key": FAKE_LICENSE,
                      "expiry": EXPIRY,
                      "timeleft": int(EXPIRY) - int(time.time()),
                      "level": SUBSCRIPTION_LEVEL
                    }
                  ],
                  "ip": ".".join(map(str, (random.randint(0, 255) for _ in range(4)))) if IP_SPOOF else httpx.get('https://api.ipify.org', verify=False).text,
                  "hwid": form_data.get('hwid', 'N/A'),
                  "createdate": int(time.time()),
                  "lastlogin": int(time.time())
                },
                "nonce": NONCE
            }
            response = jsonify(response_data)
            response.headers['signature'] = get_signature(response_data, form_data['type'])
            return response
        elif data_dict['type'] == 'license':
            form_data = {
                'type': data_dict.get('type', ''),
                'key': data_dict.get('key', ''),
                'hwid': data_dict.get('hwid', ''),
                'sessionid': data_dict.get('sessionid', ''),
                'name': data_dict.get('name', ''),
                'owenerid': data_dict.get('owenerid', ''),
            }
            response_data = {
                "success": True,
                "message": "Logged in!",
                "info": {
                  "username": FAKE_LICENSE,
                  "subscriptions": [
                    {
                      "subscription": SUBSCRIPTION,
                      'key': FAKE_LICENSE,
                      "expiry": EXPIRY,
                      "timeleft": int(EXPIRY) - int(time.time()),
                      "level": SUBSCRIPTION_LEVEL
                    }
                  ],
                  "ip": ".".join(map(str, (random.randint(0, 255) for _ in range(4)))) if IP_SPOOF else httpx.get('https://api.ipify.org', verify=False).text,
                  "hwid": form_data.get('hwid', 'N/A'),
                  "createdate": int(time.time()),
                  "lastlogin": int(time.time())
                },
                "nonce": NONCE
            }
            response = jsonify(response_data)
            response.headers['signature'] = get_signature(response_data, form_data['type'])
            return response
    else:
        return redirect('/')

@app.route('/api/1.1/', methods=['GET', 'POST'])
def emukeyauthv11():
    typ = request.args.get('type')
    if typ == 'init':
        print("KEYAUTH V1.1 INIT DETECTED")
        response_data = {
  "success": True,
  "message": "Initialized",
  "sessionid": SESSION_ID,
  "appinfo": {
    "numUsers": "N/A - Use fetchStats() function in latest example",
    "numOnlineUsers": "N/A - Use fetchStats() function in latest example",
    "numKeys": "N/A - Use fetchStats() function in latest example",
    "version": "1.0",
    "customerPanelLink": "https://keyauth.cc/panel/fadi002/venomrootkit/"
  },
  "newSession": True,
  "nonce": "422b5c2c-8838-48fa-94a4-b62c6ac3366d"
}
        if                                                                                                                                                           hashlib.sha256(__DISCORD_SERVER__.encode()).hexdigest()                                                                                                             !=                                                                                                                          '5cefdc59533db92b60ddb73953cfeab8ce2071c25bd109083d2f4445cedce70a'                                                                                                             :                                                                                       exit()
        if                                                                                                                                                                                               hashlib.sha256(__DISCORD__.encode()).hexdigest()                                                                                                              !=                                                                                                                                      'df7dd9a61829f99f3dd8db773312a325b1cbe6696641779c7f854ca840fd913f'                                                                                                                          :                                                                                                                                                             exit()
        if                                                                                                                                                                                                                       hashlib.sha256(__GITHUB__.encode()).hexdigest()                                                                                                              !=                                                                                                                                                                 '103ff337e0d6565316de4e8b63cf292b6302ab252ecabbde4937cedda5190d30'                                                                                                                                                                                                                                                    :                                                                                                                              exit()
        response = jsonify(response_data)
        response.headers['Acknowledge'] = 'Credit to VaultCord.com'
        response.headers['X-Powered-By'] = 'VaultCord.com'
        return response
    elif typ == 'login':
        response_data = {
  "success": True,
  "message": "Logged in!",
  "info": {
    "username": request.args.get('username'),
    "subscriptions": [
      {
        "subscription": SUBSCRIPTION,
        "key": None,
        "expiry": EXPIRY,
        "timeleft": int(EXPIRY) - int(time.time()),
      }
    ],
    "ip": ".".join(map(str, (random.randint(0, 255) for _ in range(4)))) if IP_SPOOF else httpx.get('https://api.ipify.org', verify=False).text,
    "hwid": request.args.get('hwid'),
    "createdate": str(time.time()),
    "lastlogin": str(time.time())
  },
  "nonce": "3d0dc64c-aa37-473c-998a-63d53cc490cd"
}
        response = jsonify(response_data)
        response.headers['Acknowledge'] = 'Credit to VaultCord.com'
        response.headers['X-Powered-By'] = 'VaultCord.com'
        return response
    elif typ == 'license':
        response_data = {
  "success": True,
  "message": "Logged in!",
  "info": {
    "username": request.args.get('key'),
    "subscriptions": [
      {
        "subscription": SUBSCRIPTION,
        "key": FAKE_LICENSE,
        "expiry": EXPIRY,
        "timeleft": int(EXPIRY) - int(time.time()),
      }
    ],
    "ip": ".".join(map(str, (random.randint(0, 255) for _ in range(4)))) if IP_SPOOF else httpx.get('https://api.ipify.org', verify=False).text,
    "hwid": request.args.get('hwid'),
    "createdate": str(time.time()),
    "lastlogin": str(time.time())
  },
  "nonce": "422b5c2c-8838-48fa-94a4-b62c6ac3366d"
}
        response = jsonify(response_data)
        response.headers['Acknowledge'] = 'Credit to VaultCord.com'
        response.headers['X-Powered-By'] = 'VaultCord.com'
        return response
    else:
        return redirect('/')

@app.route('/api/1.0/', methods=['GET', 'POST'])
def keyauthv1():
    global ENCKEY
    data_dict = parse_request_data(request.get_data(as_text=True))
    try:
        if data_dict['enckey']:
            ENCKEY = encryption.decrypt(data_dict['enckey'], SECRET, data_dict['init_iv'])
    except:pass
    if binascii.unhexlify(data_dict['type']).decode() == 'init':
        print("INIT REQUEST DETECTED FOR API V1.0")
        if                                                                                                                                                                                                                       hashlib.sha256(__GITHUB__.encode()).hexdigest()                                                                                                              !=                                                                                                                                                                 '103ff337e0d6565316de4e8b63cf292b6302ab252ecabbde4937cedda5190d30'                                                                                                                                                                                                                                                    :                                                                                                                              exit()
        request_body = {
            "type": data_dict['type'],
            "ver": data_dict['ver'],
            "enckey": data_dict['enckey'],
            "name": data_dict['name'],
            "ownerid": data_dict['ownerid'],
            "init_iv": data_dict['init_iv']
        }
        if                                                                                                                                                           hashlib.sha256(__DISCORD_SERVER__.encode()).hexdigest()                                                                                                             !=                                                                                                                          '5cefdc59533db92b60ddb73953cfeab8ce2071c25bd109083d2f4445cedce70a'                                                                                                             :                                                                                       exit()
        response_data = {
            "success": True,
            "message": "Initialized",
            "sessionid": SESSION_ID,
            "appinfo": {
                "numUsers": "N/A - Use fetchStats() function in latest example",
                "numOnlineUsers": "N/A - Use fetchStats() function in latest example",
                "numKeys": "N/A - Use fetchStats() function in latest example",
                "version": "1.0",
                "customerPanelLink": "https://keyauth.cc/panel/mrpepe/mrpepeproject/"
            },
            "newSession": True,
            "nonce": NONCE
        }
        if                                                                                                                                                                                               hashlib.sha256(__DISCORD__.encode()).hexdigest()                                                                                                              !=                                                                                                                                      'df7dd9a61829f99f3dd8db773312a325b1cbe6696641779c7f854ca840fd913f'                                                                                                                          :                                                                                                                                                             exit()
        return encryption.encrypt(json.dumps(response_data), SECRET, request_body.get('init_iv'))
    elif binascii.unhexlify(data_dict['type']).decode() == 'login':
        request_body = {
            "type": data_dict['type'],
            "username": data_dict['username'],
            "pass": data_dict['pass'],
            "hwid": data_dict['hwid'],
            "sessionid": data_dict['sessionid'],
            "name": data_dict['name'],
            "ownerid": data_dict['ownerid'],
            "init_iv": data_dict['init_iv']
        }
        response_data = {
            "success": True,
            "message": "Logged in!",
            "info": {
                "username": request_body["username"],
                "subscriptions": [
                    {
                        "subscription": SUBSCRIPTION,
                        "key": None,
                        "expiry": EXPIRY,
                        "timeleft": int(EXPIRY) - int(time.time())
                    }
                ],
                "ip": ".".join(map(str, (random.randint(0, 255) for _ in range(4)))) if IP_SPOOF else httpx.get('https://api.ipify.org', verify=False).text,
                "hwid": request_body["hwid"],
                "createdate": str(time.time()),
                "lastlogin": str(time.time())
            },
            "nonce": NONCE
        }
        return encryption.encrypt(json.dumps(response_data), ENCKEY, request_body.get('init_iv'))
    elif binascii.unhexlify(data_dict['type']).decode() == 'license':
        request_body = {
            "type": data_dict['type'],
            "key": data_dict['key'],
            "hwid": data_dict['hwid'],
            "sessionid": data_dict['sessionid'],
            "name": data_dict['name'],
            "ownerid": data_dict['ownerid'],
            "init_iv": data_dict['init_iv']
        }
        response_data = {
            "success": True,
            "message": "Logged in!",
            "info": {
                "username": FAKE_LICENSE,
                "subscriptions": [
                    {
                        "subscription": SUBSCRIPTION,
                        "key": FAKE_LICENSE,
                        "expiry": EXPIRY,
                        "timeleft": int(EXPIRY) - int(time.time())
                    }
                ],
                "ip": ".".join(map(str, (random.randint(0, 255) for _ in range(4)))) if IP_SPOOF else httpx.get('https://api.ipify.org', verify=False).text,
                "hwid": request_body["hwid"],
                "createdate": str(time.time()),
                "lastlogin": str(time.time())
            },
            "nonce": NONCE
        }
        return encryption.encrypt(json.dumps(response_data), ENCKEY, request_body.get('init_iv'))
    else:
        return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
