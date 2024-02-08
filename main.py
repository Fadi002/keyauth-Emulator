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
import hmac, hashlib, httpx, time, os, random
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

@app.errorhandler(404)
def page_not_found(error):
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
